import pandas as pd
from pathlib import Path

def read_file(path, usecols=None):
    path = Path(path)
    if path.suffix == ".csv":
        return pd.read_csv(path, usecols=usecols, low_memory=False)
    if path.suffix == ".parquet":
        return pd.read_parquet(path, columns=usecols)
    raise ValueError(f"Unsupported file type: {path}")