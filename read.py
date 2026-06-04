import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DB_URL"))

result = pd.read_sql('SELECT * FROM dynamic_pricing', con=engine)
print(result.head())