from pathlib import Path

import pandas as pd

# Path to data
from motion import Analogs, Markers

if "tests" in f"{Path('.').absolute()}":
    DATA_FOLDER = Path("data")
else:
    DATA_FOLDER = Path("tests") / "data"

MARKERS_CSV = DATA_FOLDER / "markers.csv"
MARKERS_ANALOGS_C3D = DATA_FOLDER / "markers_analogs.c3d"
ANALOGS_CSV = DATA_FOLDER / "analogs.csv"
MARKERS_CSV_WITHOUT_HEADER = DATA_FOLDER / "markers_without_header.csv"
MARKERS_XLSX = DATA_FOLDER / "markers.xlsx"
ANALOGS_XLSX = DATA_FOLDER / "analogs.xlsx"
EXPECTED_VALUES_CSV = DATA_FOLDER / "is_expected_array_val.csv"

MARKERS_DATA = Markers.from_c3d(
    MARKERS_ANALOGS_C3D,
    usecols=["CLAV_post", "PSISl", "STERr", "CLAV_post"],
    prefix_delimiter=":",
)
ANALOGS_DATA = Analogs.from_c3d(
    MARKERS_ANALOGS_C3D,
    usecols=["EMG1", "EMG10", "EMG11", "EMG12"],
    prefix_delimiter=".",
)

EXPECTED_VALUES = pd.read_csv(
    EXPECTED_VALUES_CSV,
    index_col=[0],
    converters={"shape_val": eval, "first_last_val": eval},
).to_dict("index")
