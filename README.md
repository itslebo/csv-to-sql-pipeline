# Dynamic Pricing — CSV to MySQL Pipeline

This project reads a CSV dataset, loads it into a MySQL database, and queries it back out using Python and pandas.

## Workflow

### 1. Set up the environment

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

### 2. Configure the database connection

Create a `.env` file in the project root with your MySQL connection string:

```
DB_URL="mysql+pymysql://username:password@127.0.0.1:3306/database_name"
```

> Note: Wrap the value in quotes if your password contains special characters like `#`.

Make sure the target database already exists in MySQL, and that the user has write permissions:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
```

### 3. Write the CSV to the database

Run `write.py` to load `dynamic_pricing.csv` into the `dynamic_pricing` table:

```powershell
python write.py
```

This script:
- Reads the CSV using pandas
- Prints a preview and summary of the data
- Connects to MySQL via SQLAlchemy
- Writes the data to the `dynamic_pricing` table (replacing it if it already exists)

### 4. Read data from the database

Run `read.py` to query and display the data from the database:

```powershell
python read.py
```

## Project Structure

```
.
├── write.py              # Loads CSV into MySQL
├── read.py               # Queries data from MySQL
├── dynamic_pricing.csv   # Source dataset (not committed)
├── .env                  # Database credentials (not committed)
├── requirements.txt      # Python dependencies
└── .gitignore
```

## Generating requirements.txt

```powershell
pip freeze > requirements.txt
```
