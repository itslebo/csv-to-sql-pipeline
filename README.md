# Dynamic Pricing — CSV to MySQL Pipeline

This project demonstrates a simple, beginner-friendly workflow that other developers can learn from. It shows one straightforward way to integrate a MySQL database into a Python project — loading data from a CSV file, persisting it to a database, and querying it back out. No complex frameworks, just the essentials.

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
