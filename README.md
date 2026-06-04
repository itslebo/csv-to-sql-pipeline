# Dynamic Pricing — CSV to MySQL Pipeline

A Python project that loads a dynamic pricing dataset from a CSV file into a MySQL database and provides a script to query the data back out.

## What it does

### write.py
Reads `dynamic_pricing.csv` into a pandas DataFrame, prints a preview and statistical summary of the data, then writes the entire dataset to a MySQL table called `dynamic_pricing`. If the table already exists, it is replaced.

### read.py
Connects to the same MySQL database and retrieves all records from the `dynamic_pricing` table, printing the first few rows to the console.

## Requirements

- Python 3.x
- MySQL server with an existing database
- A `.env` file in the project root containing:

```
DB_URL="mysql+pymysql://username:password@host:port/database_name"
```

## Setup

```powershell
pip install -r requirements.txt
```

## Usage

Load data into the database:

```powershell
python write.py
```

Query data from the database:

```powershell
python read.py
```
