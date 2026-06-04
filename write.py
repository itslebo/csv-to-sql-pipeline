import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
df = pd.read_csv('dynamic_pricing.csv') 
print(df.head())

engine = create_engine(os.getenv("DB_URL"))
df.to_sql('dynamic_pricing', con=engine, if_exists='replace', index=False)
print("Data written to the database.")

print(df.shape)
print(df.describe())