import os
from dotenv import load_dotenv
import mysql.connector
from typing import List, Union, Dict, Any

# Load environment variables from .env file
load_dotenv()

def load_db_config(db_key: str) -> Union[Dict[str, Any], Dict[str, str]]:
    """
    Reads database connection information from environment variables for the specified database key.

    Args:
        db_key (str): Identifier of the target database (e.g. 'chat_app' or 'example_db').
                      This should correspond to environment variable prefixes in uppercase.

    Returns:
        dict: On success, returns a dictionary with connection parameters:
              {
                "host": str,       # Database server address
                "port": int,       # Port number, defaults to 3306 if not set
                "user": str,       # Username for DB login
                "password": str,   # Password for DB login
                "database": str    # Database name
              }
              On failure, returns a dict with "error" key and an error message.

    Possible errors:
        - Missing environment variables (host, user, password, or database) for the given db_key.
        - Invalid port value (not an integer).
        - General exception while loading config.
    """
    key = db_key.upper()
    try:
        config = {
            "host": os.getenv(f"DB_{key}_HOST"),
            "port": int(os.getenv(f"DB_{key}_PORT", 3306)),  # Default port 3306 if not set
            "user": os.getenv(f"DB_{key}_USER"),
            "password": os.getenv(f"DB_{key}_PASSWORD"),
            "database": os.getenv(f"DB_{key}_NAME"),
        }

        if None in config.values():
            return {"error": f"Missing environment variables for database '{db_key}'"}

        return config

    except ValueError:
        return {"error": f"Invalid port value for database '{db_key}'. Port must be an integer."}

    except Exception as e:
        return {"error": f"Failed to load database config: {str(e)}"}


def sql_query_select(
    db_key: str,
    table_name: str,
    fetch: str = "all",
    column: str = "*",
    order_column: str = "id"
) -> Union[List[Any], List[Dict[str, Any]], Dict[str, str]]:
    """
    Executes a SELECT query on the specified MySQL database using environment-based connection config.

    Args:
        db_key (str): The database identifier key corresponding to environment config.
        table_name (str): Name of the table to query.
        fetch (str): Specifies which rows to fetch:  
                     'all' (default) fetches all rows,  
                     'first' fetches the first row ordered by 'order_column' ascending,  
                     'last' fetches the last row ordered by 'order_column' descending.
        column (str): Columns to select, e.g. 'id, name' or '*' for all columns.
        order_column (str): Column used for ordering when fetch is 'first' or 'last'. Default is 'id'.

    Returns:
        - If successful and a single column is selected, returns a list of values for that column.
        - If multiple columns or '*' is selected, returns a list of dictionaries (row mappings).
        - On error, returns a dictionary with an "error" key and descriptive message.

    Possible errors and reasons:
        - Missing environment variables for connection (handled by load_db_config).
        - Invalid 'fetch' parameter value (must be 'all', 'first', or 'last').
        - mysql.connector.Error, e.g.:
          * Table does not exist
          * Column does not exist
          * Authentication failure
          * Network or connection issues
        - Unexpected Python exceptions.

    Important notes:
        - This function uses simple string formatting to build SQL queries; ensure inputs are safe
          to avoid SQL injection vulnerabilities in real applications.
        - The database connection is properly closed after query execution even if errors occur.
        
    ## Writed by Mr.Javadian ##
    """
    db_config = load_db_config(db_key)
    if "error" in db_config:
        return db_config

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        if fetch not in ("all", "first", "last"):
            return {"error": "Invalid fetch type. Use 'all', 'first', or 'last'."}

        if fetch == "first":
            query = f"SELECT {column} FROM {table_name} ORDER BY {order_column} ASC LIMIT 1"
        elif fetch == "last":
            query = f"SELECT {column} FROM {table_name} ORDER BY {order_column} DESC LIMIT 1"
        else:
            query = f"SELECT {column} FROM {table_name}"

        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        if column != "*" and len(columns) == 1:
            # Return a list of values if only one column was selected
            return [row[0] for row in rows]
        else:
            # Return a list of dicts mapping column names to values
            return [dict(zip(columns, row)) for row in rows]

    except mysql.connector.Error as e:
        return {"error": f"MySQL Error: {str(e)}"}

    except Exception as e:
        return {"error": f"Unexpected Error: {str(e)}"}

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()



# MIT License

# Copyright (c) 2025 [sadegh]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
