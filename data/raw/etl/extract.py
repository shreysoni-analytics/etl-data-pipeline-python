from pathlib import Path
import pandas as pd

def extract_events(raw_path: Path) -> pd.DataFrame:
    """
    Extract raw events data from CSV.
    """
    df = pd.read_csv(raw_path)
    return df
