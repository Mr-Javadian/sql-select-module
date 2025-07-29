# 🔍 SQL Query Utility with Dynamic Environment-based Configuration

A lightweight and extensible Python module for performing safe and structured `SELECT` queries on multiple MySQL databases using `.env` configuration.

## 📦 Features

- Supports querying multiple databases dynamically using environment variables
- Clean and readable interface for `SELECT` queries (`first`, `last`, `all`)
- Automatic error handling and input validation
- Written with extensibility and simplicity in mind
- Safe fallback and descriptive error responses

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.8+
- MySQL server (local or remote)
- Environment variables defined via `.env` file

### 📁 Project Structure

your-project/
├── .env
├── main.py
└── README.md


---

##Clone the repository:

```bash
git clone https://github.com/Mr-Javadian/sql-select-module.git
cd Mr-Javadian/sql-select-module
```

🧠 Usage
▶️ Example Python Code
python
Copy
Edit
from main import sql_query_select

        ##Args:
                db_key (str): The database identifier key corresponding to environment config.
                table_name (str): Name of the table to query.
                fetch (str): Specifies which rows to fetch:  
                             'all' (default) fetches all rows,  
                             'first' fetches the first row ordered by 'order_column' ascending,  
                             'last' fetches the last row ordered by 'order_column' descending.
                column (str): Columns to select, e.g. 'id, name' or '*' for all columns.
                order_column (str): Column used for ordering when fetch is 'first' or 'last'. Default is 'id'.

    ##Returns:
        - If successful and a single column is selected, returns a list of values for that column.
        - If multiple columns or '*' is selected, returns a list of dictionaries (row mappings).
        - On error, returns a dictionary with an "error" key and descriptive message.


📄 License
MIT License
