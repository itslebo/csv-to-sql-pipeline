import os
import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(levelname)s — %(message)s")

CSV_FILE = "data/dynamic_pricing.csv"
TABLE_NAME = "dynamic_pricing"


def load_csv(filepath: str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")
    df = pd.read_csv(filepath)
    logging.info(f"Loaded {len(df)} rows from {filepath}")
    return df


def get_engine():
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL is not set. Check your .env file.")
    return create_engine(db_url)


def write_to_db(df: pd.DataFrame, engine, table: str) -> None:
    with engine.begin() as connection:
        df.to_sql(table, con=connection, if_exists="replace", index=False)
    logging.info(f"Data written to table '{table}' successfully.")


def summarise(df: pd.DataFrame) -> None:
    print("\n--- Preview ---")
    print(df.head())
    print(f"\nShape: {df.shape}")
    print("\n--- Summary Statistics ---")
    print(df.describe())


def main():
    try:
        df = load_csv(CSV_FILE)
        summarise(df)
        engine = get_engine()
        write_to_db(df, engine, TABLE_NAME)
    except (FileNotFoundError, ValueError) as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
