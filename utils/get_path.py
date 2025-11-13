from pathlib import Path

def get_path(data_dir: Path, base: str):
    # prefer parquet, then csv
    ext = base.split('.')[-1]
    if ext in (".parquet", "parquet", ".csv", "csv"):
        candidate = data_dir / base
        if candidate.exists():
            return candidate
        else:
            raise FileNotFoundError(f"No table found for specified file: {base}")
    for ext in (".parquet", ".csv"):
        candidate = data_dir / f"{base}{ext}"
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"No table found for base name: {base}")