import os
import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(levelname)s — %(message)s")

TABLE_NAME = "dynamic_pricing"


def get_engine():
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL is not set. Check your .env file.")
    return create_engine(db_url)


def fetch_data(engine, table: str) -> pd.DataFrame:
    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, con=engine)
    logging.info(f"Fetched {len(df)} rows from '{table}'")
    return df


def main():
    try:
        engine = get_engine()
        df = fetch_data(engine, TABLE_NAME)
        print(df.head())
    except ValueError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
