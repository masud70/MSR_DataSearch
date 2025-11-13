from pathlib import Path

def find_table(data_dir: Path, base: str):
    # prefer parquet, then csv
    for ext in (".parquet", ".csv"):
        p = data_dir / f"{base}{ext}"
        if p.exists():
            return p
    raise FileNotFoundError(f"Could not find {base}.parquet or {base}.csv in {data_dir}")