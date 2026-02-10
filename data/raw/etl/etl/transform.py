import pandas as pd

def transform_events(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raw events into analytics-ready format:
    - Parse timestamps
    - Standardize column types
    - Add derived date column
    - Basic data quality fixes
    """
    df = df.copy()

    # Parse datetime
    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

    # Drop rows with missing critical fields
    df = df.dropna(subset=["user_id", "event_time", "event_name"])

    # Clean strings
    df["event_name"] = df["event_name"].str.strip().str.lower()
    df["platform"] = df["platform"].str.strip().str.lower()
    df["country"] = df["country"].str.strip().str.upper()

    # Derived columns
    df["event_date"] = df["event_time"].dt.date

    # Enforce types
    df["user_id"] = df["user_id"].astype(int)

    return df
