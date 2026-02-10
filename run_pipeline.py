from pathlib import Path
from etl.extract import extract_events
from etl.transform import transform_events
from etl.load import load_events

RAW_EVENTS_PATH = Path("data/raw/events.csv")
OUTPUT_EVENTS_PATH = Path("data/output/events_clean.csv")

def main() -> None:
    # Extract
    raw_df = extract_events(RAW_EVENTS_PATH)

    # Transform
    clean_df = transform_events(raw_df)

    # Load
    load_events(clean_df, OUTPUT_EVENTS_PATH)

    print(f"✅ Pipeline complete. Output saved to: {OUTPUT_EVENTS_PATH}")

if __name__ == "__main__":
    main()
