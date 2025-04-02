import json
import pathlib
from typing import List, Optional
from typing_extensions import Annotated

import typer

from russian_sme_registry.stages.aggregate import Aggregator
from russian_sme_registry.stages.download import Downloader
from russian_sme_registry.stages.extract import Extractor
from russian_sme_registry.stages.geocode import Geocoder
from russian_sme_registry.stages.panelize import Panelizer
from russian_sme_registry.utils.enums import SourceDatasets, StageNames, Storages


APP_NAME = "russian-sme-registry"

app = typer.Typer(
    help=(
        "A tool to create a geocoded CSV dataset of Russian small and medium-sized "
        "enterprises from Federal Tax Service (FTS) open data"
    ),
    rich_markup_mode="markdown"
)
download_app = typer.Typer()
extract_app = typer.Typer()
aggregate_app = typer.Typer()
app.add_typer(
    download_app,
    name="download",
    help="Download source zipped dataset(s) from FTS open data server (stage 1)",
    rich_help_panel="Stages",
    no_args_is_help=True
)
app.add_typer(
    extract_app,
    name="extract",
    help="Extract data from downloaded source zipped datasets to CSV files (stage 2)",
    rich_help_panel="Stages",
    no_args_is_help=True
)
app.add_typer(
    aggregate_app,
    name="aggregate",
    help="Aggregate extracted data into a single CSV file removing duplicates (stage 3)",
    rich_help_panel="Stages",
    no_args_is_help=True
)

default_config = dict(storage="local", token="", num_workers=1, chunksize=16)

app_dir = typer.get_app_dir(APP_NAME)
app_config_path = pathlib.Path(app_dir) / "config.json"
app_config_path.parent.mkdir(parents=True, exist_ok=True)
try:
    with open(app_config_path) as f:
        app_config = json.load(f)
except:
    app_config = {}
    print("Failed to load config, default options are loaded")
    app_config = default_config


def get_default_path(
    stage_name: str,
    source_dataset: Optional[str] = None,
    filename: Optional[str] = None,
) -> pathlib.Path:
    path = pathlib.Path("russian-sme-registry-data") / stage_name
    if source_dataset is not None:
        path = path / source_dataset
    if filename is not None:
        path = path / filename

    return path


def get_downloader(app_config: dict) -> Downloader:
    storage = app_config.get("storage")
    token = app_config.get("token")

    return Downloader(storage, token)


def get_extractor(app_config: dict) -> Extractor:
    num_workers = app_config.get("num_workers")
    chunksize = app_config.get("chunksize")
    storage = app_config.get("storage")
    token = app_config.get("token")

    return Extractor(storage, num_workers, chunksize, token)


@download_app.command("all", rich_help_panel="Source dataset(s)")
def download_all(
    download_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to the directory to store downloaded files. Sub-directories *sme*, *revexp*, and *empl* for respective datasets will be created automatically"
        )
    ] = get_default_path(StageNames.download.value)
):
    """
    Download all three source dataset(s)
    """
    d = get_downloader(app_config)
    for source_dataset in SourceDatasets:
        args = dict(
            download_dir=str(download_dir / source_dataset.value),
            source_dataset = source_dataset.value
        )
        d(**args)


@download_app.command("sme", rich_help_panel="Source dataset(s)")
def download_sme(
    download_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to the directory to store downloaded files"
        )
    ] = get_default_path(StageNames.download.value, SourceDatasets.sme.value)
):
    """
    Download **s**mall&**m**edium-sized **e**nterprises registry
    """
    d = get_downloader(app_config)
    d(SourceDatasets.sme.value, str(download_dir))


@download_app.command("revexp", rich_help_panel="Source dataset(s)")
def download_revexp(
    download_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to the directory to store downloaded files"
        )
    ] = get_default_path(StageNames.download.value, SourceDatasets.revexp.value)
):
    """
    Download data on **rev**enue and **exp**enditure of companies
    """
    d = get_downloader(app_config)
    d(SourceDatasets.revexp.value, str(download_dir))


@download_app.command("empl", rich_help_panel="Source dataset(s)")
def download_empl(
    download_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to the directory to store downloaded files"
        )
    ] = get_default_path(StageNames.download.value, SourceDatasets.empl.value)
):
    """
    Download data on number of **empl**oyees in companies
    """
    d = get_downloader(app_config)
    d(SourceDatasets.empl.value, str(download_dir))


@extract_app.command("all", rich_help_panel="Source dataset(s)")
def extract_all(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to downloaded source files. Usually the same as *download_dir* on download stage. Expected to contain *sme*, *revexp*, *empl* sub-folders"
        )
    ] = get_default_path(StageNames.download.value),
    out_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save extracted CSV files. Sub-folders *sme*, *revexp*, *empl* for respective datasets will be created automatically"
        )
    ] = get_default_path(StageNames.extract.value),
    clear: Annotated[
        bool, typer.Option(help="Clear *out_dir* (see above) before processing")
    ] = False,
    ac: Annotated[
        Optional[List[str]],
        typer.Option(
            help="**A**ctivity **c**ode(s) to filter SME source dataset by. Can be either activity group code, e.g. *--ac A*, or exact digit code, e.g. *--ac 01.10*. Multiple codes or groups can be specified by multiple *ac* options, e.g. *--ac 01.10 --ac 69.20*. Top-level codes include child codes, i.e. *--ac 01.10* selects 01.10.01, 01.10.02, 01.10.10 (if any children are present). If not specified, filtering is disabled",
            show_default="no filtering by activity code(s)"
        )
    ] = None,
):
    """
    Extract data from all three downloaded source datasets
    """
    e = get_extractor(app_config)
    for source_dataset in SourceDatasets:
        args = dict(
            in_dir=str(in_dir / source_dataset.value),
            out_dir=str(out_dir / source_dataset.value),
            source_dataset=source_dataset.value,
            clear=clear,
            activity_codes=ac,
        )
        e(**args)


@extract_app.command("sme", rich_help_panel="Source dataset(s)")
def extract_sme(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to downloaded source files. Usually the same as *download_dir* on download stage"
        )
    ] = get_default_path(StageNames.download.value, SourceDatasets.sme.value),
    out_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save extracted CSV files"
        )
    ] = get_default_path(StageNames.extract.value, SourceDatasets.sme.value),
    clear: Annotated[
        bool, typer.Option(help="Clear *out_dir* (see above) before processing")
    ] = False,
    ac: Annotated[
        Optional[List[str]],
        typer.Option(
            help="**A**ctivity **c**ode(s) to filter SME source dataset by. Can be either activity group code, e.g. *--ac A*, or exact digit code, e.g. *--ac 01.10*. Multiple codes or groups can be specified by multiple *ac* options, e.g. *--ac 01.10 --ac 69.20*. Top-level codes include child codes, i.e. *--ac 01.10* selects 01.10.01, 01.10.02, 01.10.10 (if any children are present). If not specified, filtering is disabled",
            show_default="no filtering by activity code(s)"
        )
    ] = None,
):
    """
    Extract data from downloaded *zip* archives of SME registry to *csv* files,
    optionally filtering by activity code (stage 2)
    """
    e = get_extractor(app_config)
    e(str(in_dir), str(out_dir), SourceDatasets.sme.value, clear, ac)


@extract_app.command("revexp", rich_help_panel="Source dataset(s)")
def extract_revexp(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to downloaded source files. Usually the same as *download_dir* on download stage"
        )
    ] = get_default_path(StageNames.download.value, SourceDatasets.revexp.value),
    out_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save extracted CSV files"
        )
    ] = get_default_path(StageNames.extract.value, SourceDatasets.revexp.value),
    clear: Annotated[
        bool, typer.Option(help="Clear *out_dir* (see above) before processing")
    ] = False
):
    """
    Extract data from downloaded *zip* archives of revexp data to *csv* files
    """
    e = get_extractor(app_config)
    e(str(in_dir), str(out_dir), SourceDatasets.revexp.value, clear)


@extract_app.command("empl", rich_help_panel="Source dataset(s)")
def extract_empl(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to downloaded source files. Usually the same as *download_dir* on download stage"
        )
    ] = get_default_path(StageNames.download.value, SourceDatasets.empl.value),
    out_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save extracted CSV files"
        )
    ] = get_default_path(StageNames.extract.value, SourceDatasets.empl.value),
    clear: Annotated[
        bool, typer.Option(help="Clear *out_dir* (see above) before processing")
    ] = False
):
    """
    Extract data from downloaded *zip* archives of empl data to *csv* files
    """
    e = get_extractor(app_config)
    e(str(in_dir), str(out_dir), SourceDatasets.empl.value, clear)


@aggregate_app.command("all", rich_help_panel="Source dataset(s)")
def aggregate_all(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to extracted CSV files. Usually the same as *out_dir* on extract stage. Expected to contain *sme*, *revexp*, *empl* sub-folders"
        )
    ] = get_default_path(StageNames.extract.value),
    out_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save aggregated CSV files. Sub-folders *sme*, *revexp*, *empl* for respective datasets will be created automatically"
        )
    ] = get_default_path(StageNames.aggregate.value)
):
    """
    Aggregate all three source datasets
    """
    a = Aggregator()
    for source_dataset in SourceDatasets:
        args = dict(
            in_dir=str(in_dir / source_dataset.value),
            out_file=str(out_dir / source_dataset.value / "agg.csv"),
            source_dataset=source_dataset.value,
        )
        if source_dataset.value in ("revexp", "empl"):
            args["sme_data_file"] = str(out_dir / SourceDatasets.sme.value / "agg.csv")
        a(**args)


@aggregate_app.command("sme", rich_help_panel="Source dataset(s)")
def aggregate_sme(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to extracted CSV files. Usually the same as *out_dir* on extract stage"
        )
    ] = get_default_path(StageNames.extract.value, SourceDatasets.sme.value),
    out_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save aggregated CSV files"
        )
    ] = get_default_path(StageNames.aggregate.value, SourceDatasets.sme.value, "agg.csv")
):
    """
    Aggregate SME dataset
    """
    a = Aggregator()
    a(str(in_dir), str(out_file), SourceDatasets.sme.value)


@aggregate_app.command("revexp", rich_help_panel="Source dataset(s)")
def aggregate_revexp(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to extracted CSV files. Usually the same as *out_dir* on extract stage"
        )
    ] = get_default_path(StageNames.extract.value, SourceDatasets.revexp.value),
    out_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save aggregated CSV files"
        )
    ] = get_default_path(StageNames.aggregate.value, SourceDatasets.revexp.value, "agg.csv"),
    sme_data_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to **already processed SME file** that is used to filter aggregated values in revexp or empl file",
            exists=True,
            file_okay=True,
            readable=True
        )
    ] = None
):
    """
    Aggregate revexp dataset
    """
    a = Aggregator()
    if sme_data_file is not None:
        sme_data_file = str(sme_data_file)

    a(str(in_dir), str(out_file), SourceDatasets.revexp.value, sme_data_file)


@aggregate_app.command("empl", rich_help_panel="Source dataset(s)")
def aggregate_empl(
    in_dir: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to extracted CSV files. Usually the same as *out_dir* on extract stage"
        )
    ] = get_default_path(StageNames.extract.value, SourceDatasets.empl.value),
    out_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save aggregated CSV files"
        )
    ] = get_default_path(StageNames.aggregate.value, SourceDatasets.empl.value, "agg.csv"),
    sme_data_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to **already processed SME file** that is used to filter aggregated values in revexp or empl file",
            exists=True,
            file_okay=True,
            readable=True
        )
    ] = None
):
    """
    Aggregate empl dataset
    """
    a = Aggregator()
    if sme_data_file is not None:
        sme_data_file = str(sme_data_file)

    a(str(in_dir), str(out_file), SourceDatasets.empl.value, sme_data_file)


@app.command(rich_help_panel="Stages")
def geocode(
    in_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to a CSV file. Usually the same as *out_file* on aggregate sme stage. CSV file must include at least *region_name*, *district_name*, *city_name*, *settlement_name* fields",
            exists=True,
            file_okay=True,
            readable=True
        )
    ] = get_default_path(StageNames.aggregate.value, SourceDatasets.sme.value, "agg.csv"),
    out_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save geocoded CSV file"
        )
    ] = get_default_path(StageNames.geocode.value, SourceDatasets.sme.value, "geocoded.csv")
):
    """
    Geocode SME aggregated data (stage 4) OR geocode *any other dataset with a similar structure of address fields*
    """
    g = Geocoder()
    g(str(in_file), str(out_file))


@app.command(rich_help_panel="Stages")
def panelize(
    sme_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to geocoded CSV file. Usually the same as *out_file* on geocode stage",
            exists=True,
            file_okay=True,
            readable=True
        )
    ] = get_default_path(StageNames.geocode.value, SourceDatasets.sme.value, "geocoded.csv"),
    out_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to save panel CSV file"
        )
    ] = get_default_path(StageNames.panelize.value, "panel.csv"),
    revexp_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to aggregated CSV revexp file. Usually the same as *out_file* on aggregate revexp stage",
            exists=True,
            file_okay=True,
            readable=True
        )
    ] = get_default_path(StageNames.aggregate.value, SourceDatasets.revexp.value, "agg.csv"),
    empl_file: Annotated[
        Optional[pathlib.Path],
        typer.Option(
            help="Path to aggregated CSV empl file. Usually the same as *out_file* on aggregate empl stage",
            exists=True,
            file_okay=True,
            readable=True
        )
    ] = get_default_path(StageNames.aggregate.value, SourceDatasets.empl.value, "agg.csv"),
):
    """
    Make panel dataset based on geocoded SME data and aggregated revexp and empl tables (stage 5)
    """
    p = Panelizer()
    p(str(sme_file), str(out_file), str(revexp_file), str(empl_file))


@app.command(rich_help_panel="Configuration", no_args_is_help=True)
def config(
    show: Annotated[
        bool,
        typer.Option(
            "--show",
            help="Only show current config without updating",
            show_default="false",
            rich_help_panel="Control")
    ] = False,
    chunksize: Annotated[
        int,
        typer.Option(help="Chunk size for extractor", rich_help_panel="Available options")
    ] = 16,
    num_workers: Annotated[
        int,
        typer.Option(help="Number of workers = processes for extractor", rich_help_panel="Available options")
    ] = 1,
    storage: Annotated[
        Storages,
        typer.Option(help="Place to download source datasets (note: *source datasets only* rather than all other files)", rich_help_panel="Available options")
    ] = Storages.local.value,
    ydisk_token: Annotated[
        str,
        typer.Option(help="Token for Yandex Disk; used if *storage* is *ydisk*", rich_help_panel="Available options")
    ] = "",
):
    """
    Show or set global options for all commands
    """
    if show:
        print("Current configuration")
        for key, value in app_config.items():
            print(key, value)

        return

    app_config["token"] = ydisk_token
    app_config["num_workers"] = num_workers
    app_config["chunksize"] = chunksize
    app_config["storage"] = storage.value

    with open(app_config_path, "w") as f:
        json.dump(app_config, f)

    print("Configuration updated")


@app.command(rich_help_panel="Magic command")
def process(
    download: Annotated[
        bool,
        typer.Option(
            help="Download source datasets before processing. If False, the application expects that source datasets have already been downloaded to *rmsp-data/download/sme*, *rmsp-data/download/revexp*, and rmsp-data/download/empl*"
        )
    ] = False,
    ac: Annotated[
        Optional[List[str]],
        typer.Option(
            help="**A**ctivity **c**ode(s) to filter SME source dataset by. Can be either activity group code, e.g. *--ac A*, or exact digit code, e.g. *--ac 01.10*. Multiple codes or groups can be specified by multiple *ac* options, e.g. *--ac 01.10 --ac 69.20*. Top-level codes include child codes, i.e. *--ac 01.10* selects 01.10.01, 01.10.02, 01.10.10 (if any children are present). If not specified, filtering is disabled",
            show_default="no filtering by activity code(s)"
        )
    ] = None
):
    """
    Process the source data with this single command
    """
    if download:
        download_all()

    extract_all(ac=ac)
    aggregate_all()
    geocode()
    panelize()
