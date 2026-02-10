from pathlib import Path
import pandas as pd

def load_events(df: pd.DataFrame, output_path: Path) -> None:
    """
    Load cleaned events dataset to output CSV.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
