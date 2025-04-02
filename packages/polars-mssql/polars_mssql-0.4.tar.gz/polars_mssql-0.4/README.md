
# polars_mssql

`polars_mssql` is a Python package designed to simplify working with Microsoft SQL Server databases using the high-performance `polars` DataFrame library. It provides an intuitive and efficient interface for running SQL queries, reading tables, and writing data to SQL Server.

## Features

- **Seamless SQL Server Integration**: Easily connect to SQL Server with options for Windows Authentication or SQL Authentication.
- **Query Execution**: Execute SQL queries and retrieve results as `polars.DataFrame` objects. Use `read_query` for simple query execution or `polars.read_database` for advanced functionality like batch processing and schema customization.
- **Parameterization Support**: Securely execute parameterized queries to prevent accidental SQL injection.
- **Table Operations**: Read and write tables with flexibility and performance.
- **Context Management**: Supports Python's context manager for automatic connection handling.

## Installation

Install the package using pip:

```bash
pip install polars_mssql
```

Ensure the following dependencies are installed:

- `polars` for high-performance DataFrame operations.
- `sqlalchemy` for database connectivity.
- An appropriate ODBC driver for SQL Server (e.g., ODBC Driver 17 or 18).

## Usage

Here is an example of how to use `polars_mssql` to connect to SQL Server and perform various operations:

### 1. Connecting to SQL Server

```python
from polars_mssql import Connection

# Initialize a connection
conn = Connection(
  server="my_server",
    database="my_database",
    # If not specified, driver defaults to "SQL Server"
    # driver = 'ODBC Driver 17 for SQL Server'
)
```
**Driver Defaults**
By default, the driver parameter is set to `"SQL Server"`, which often comes preinstalled on Windows. If you don't have `"SQL Server"` installed or prefer a more recent driver, specify any compatible driver you have installed (e.g., `"ODBC Driver 17 for SQL Server"`) for the database you are trying to connect to. 

### 2. Read Data from SQL Server

#### Execute a SQL Query and Get Results as a DataFrame

```python
query = "SELECT * FROM my_table WHERE col1 = 'a'"
df = conn.read_query(query)
```

For advanced functionality (e.g., batch processing or schema customization), use the polars.read_database function with the engine:

```python
import polars as pl

df = pl.read_database(
    query="SELECT * FROM users",
    connection=conn.engine,
    iter_batches=True,
    batch_size=1000
)

for batch in df:
    print(batch)
```

#### Read an Entire Table

```python
df = conn.read_table("my_table")
```

### 3. Save DataFrame to SQL Server

#### Write a Polars DataFrame to a Table

```python
import polars as pl

# Example DataFrame
data = pl.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
conn.write_table(data, name="my_table", if_exists="replace")
```

### 4. Execute Queries

The `execute_query` method allows you to run any SQL query on your database. It supports parameterized queries to prevent accidental SQL injection and can be used for both retrieval and modification operations such as `INSERT`, `DELETE`, and `DROP`.

#### Example: Run a Simple Query
```python
query = "DELETE FROM users WHERE id = 1"
conn.execute_query(query)
```

#### Example: Insert Data Securely
```python
query = "INSERT INTO users (id, name, email) VALUES (:id, :name, :email)"
params = {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
conn.execute_query(query, params)
```

#### Example: Drop a Table
```python
query = "DROP TABLE users"
conn.execute_query(query)
```

#### Example: Prevent SQL Injection
```python
query = "SELECT * FROM users WHERE name = :name"
params = {"name": "John'; DROP TABLE users; --"}
conn.execute_query(query, params)
```
This safely executes the query without executing malicious SQL commands.

### 5. Using Context Management

```python
with Connection(server="my_server", database="my_database") as conn:
    df = conn.read_query("SELECT * FROM my_table")
    print(df)
```

### 6. Closing the Connection

```python
conn.close()
```

## API Reference

### `Connection` Class

#### Constructor
```python
Connection(server: Optional[str] = None, database: Optional[str] = None, driver: Optional[str] = None, username: Optional[str] = None, password: Optional[str] = None)
```

#### Attributes

- **`server`** (str):
  The name or address of the SQL Server instance.

  - **`database`** (str):
  The name of the connected database.

- **`driver`** (str):
  The ODBC driver being used for the connection (e.g., "ODBC Driver 17 for SQL Server").

- **`connection_string`** (str):
  The full SQLAlchemy connection string used to create the engine. This can be useful for debugging or passing to other tools.

- **`engine`** (`sqlalchemy.engine.base.Engine`):
  The SQLAlchemy engine used for database interactions. Advanced users can use this attribute for custom SQLAlchemy operations or to pass it to functions like `polars.read_database`.

#### Methods

- **`read_query(query: str) -> pl.DataFrame`**:
  Execute a query and return results as a Polars DataFrame.
  - **Parameters:**
    - `query (str)`: The SQL query to execute.
  - **Returns**: pl.DataFrame: The result of the query as a Polars DataFrame.

  - **Example**:
    ```python
    query = "SELECT * FROM my_table WHERE col1 = 'a'"
    df = conn.read_query(query)
    print(df)
    ```

- **`read_table(name: str) -> pl.DataFrame`**:
  Read all rows from a table.
  - **Parameters:**
    - `name (str)`: The name of the table to read from.
  - **Returns**: pl.DataFrame: All rows from the specified table as a Polars DataFrame.

  - **Example**:
    ```python
    df = conn.read_table('my_table')
    print(df)
    ```

- **`write_table(df: pl.DataFrame, name: str, if_exists: str = "fail") -> None`**:
  Save a Polars DataFrame to a specified table in SQL Server.
  - **Parameters**:
    - `df` (pl.DataFrame): The Polars DataFrame to be written.
    - `name` (str): The name of the target table in the database.
    - `if_exists` (str): What to do if the target table already exists. Options:
      - `'fail'` (default): Raise an error.
      - `'append'`: Append the data to the existing table.
      - `'replace'`: Drop the existing table, recreate it, and insert the data.
  - **Raises**:
    - `ValueError`: If `if_exists` is not one of `'fail'`, `'append'`, or `'replace'`.
    - `RuntimeError`: If the write operation fails.
  - **Examples**:
    ```python
    import polars as pl

    # Create a Polars DataFrame
    df = pl.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"]
    })

    # Write the DataFrame to the database
    conn.write_table(df, name="users", if_exists="replace")
    ```

- **`execute_query(query: str, params: Optional[Dict[str, Any]] = None) -> None`**:
  Execute any SQL query. Supports parameterized queries to prevent SQL injection.
  - **Parameters**:
    - `query` (str): The SQL query to execute. Can include placeholders for parameterized queries (e.g., `:param_name`).
    - `params` (dict, optional): A dictionary of parameters to bind to the query.
  - **Examples**:
    ```python
    query = "DELETE FROM users WHERE id = 1"
    conn.execute_query(query)
    ```

    ```python
    query = "INSERT INTO users (id, name) VALUES (:id, :name)"
    params = {"id": 1, "name": "Jane"}
    conn.execute_query(query, params)
    ```

- **`close() -> None`**:
  Dispose of the SQLAlchemy engine and close the connection.
  - **Example**:
    ```python
    conn.close()
    ```

## Requirements

- Python 3.7 or higher
- `polars`
- `sqlalchemy`
- ODBC Driver for SQL Server (17 or 18 recommended)

### Installing the ODBC Driver

#### Windows
Download and install the ODBC Driver from [Microsoft's website](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

#### macOS
Install via Homebrew:
```bash
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install --no-sandbox msodbcsql18
```

#### Linux
Install using the following commands:
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
sudo apt-get update
sudo apt-get install -y mssql-tools unixodbc-dev
```

## Contributing

Contributions are welcome! If you encounter issues or have feature requests, please open an issue or submit a pull request on [GitHub](https://github.com/drosenman/polars_mssql).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This package integrates the efficiency of polars with the versatility of SQL Server, inspired by real-world data engineering needs. As a data engineer, I often need to pull data from SQL Server into polars and export data from polars back to SQL Server. I created this package to streamline these workflows and make the process more efficient.
