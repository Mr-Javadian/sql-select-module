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

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2.Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install required libraries:

bash
Copy
Edit
pip install mysql-connector-python python-dotenv
🔐 Environment Variables
Create a .env file in the project root with the following format for each database you want to use:

dotenv
Copy
Edit
# Chat App Database
DB_CHAT_APP_HOST=127.0.0.1
DB_CHAT_APP_PORT=3306
DB_CHAT_APP_USER=root
DB_CHAT_APP_PASSWORD=your_password
DB_CHAT_APP_NAME=chat_app

# Example DB
DB_EXAMPLE_DB_HOST=127.0.0.1
DB_EXAMPLE_DB_PORT=3306
DB_EXAMPLE_DB_USER=root
DB_EXAMPLE_DB_PASSWORD=your_password
DB_EXAMPLE_DB_NAME=example_db
Replace chat_app and example_db with your actual database identifiers.

🧠 Usage
▶️ Example Python Code
python
Copy
Edit
from main import sql_query_select

# Fetch all records
result = sql_query_select("example_db", "users", fetch="all")
print(result)

# Fetch first user by ID
first_user = sql_query_select("chat_app", "users", fetch="first", order_column="id")
print(first_user)

# Fetch last user's email
last_email = sql_query_select("chat_app", "users", fetch="last", column="email", order_column="id")
print(last_email)
🔎 Function Documentation
sql_query_select
python
Copy
Edit
sql_query_select(
    db_key: str,
    table_name: str,
    fetch: str = "all",
    column: str = "*",
    order_column: str = "id"
)
Parameters:
Name	Type	Description
db_key	str	Identifier matching .env prefix (e.g. chat_app)
table_name	str	Table name to query
fetch	str	One of 'all', 'first', 'last'
column	str	Column(s) to select (e.g. "name,email" or "*")
order_column	str	Column to order by when using first or last

Returns:
List of dictionaries (if column="*" or multiple columns)

List of values (if only one column is selected)

Dictionary with "error" key in case of failure

💡 Tips
Make sure your .env is never uploaded publicly (add to .gitignore)

For better performance, limit your queries when possible

You can extend this module to include INSERT, UPDATE, DELETE, and parameterized queries

📄 License
MIT License
