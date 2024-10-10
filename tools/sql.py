import sqlite3
from langchain.tools import Tool
import os
from pydantic import BaseModel
from typing import List


def connect_to_db(db_path: str) -> sqlite3.Connection:
    """Establish a connection to the SQLite database."""
    try:
        # Use an absolute path for the database
        abs_path = os.path.abspath(db_path)
        print(f"Connecting to database at: {abs_path}")

        # Check if the file exists
        if not os.path.exists(abs_path):
            print(f"Database file not found at: {abs_path}")
            return None

        connection = sqlite3.connect(abs_path)
        print("Connection successful.")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def list_tables(conn: sqlite3.Connection):
    """List all tables in the database for debugging purposes."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    cursor.close()
    return "\n".join([table[0] for table in tables if table[0] is not None])

def describe_tables(conn: sqlite3.Connection, table_names):
    """Describe the tables in the database."""
    cursor = conn.cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name IN ({tables});")
    columns = cursor.fetchall()
    cursor.close()
    return '\n'.join(column[0] for column in columns if column[0] is not None)

def execute_sql_query(conn: sqlite3.Connection, query: str) -> list:
    """Execute a SQL query and return the results."""
    print(f"Executing query: {query}")
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except sqlite3.OperationalError as err:
        return f"Error executing query: {str(err)}"

class RunQueryArgsSchema(BaseModel):
    query: str

def create_sql_tool(conn: sqlite3.Connection) -> Tool:
    """Create a Tool for executing SQL queries."""
    def sql_tool(query: str) -> list:
        return execute_sql_query(conn, query)

    return Tool(
        name="sql",
        description="Use this tool to execute SQL queries on the database.",
        func=sql_tool,
        args_schema=RunQueryArgsSchema,
    )

class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]

def create_describe_tables_tool(conn: sqlite3.Connection) -> Tool:
    """Create a Tool for describing the tables in the database."""
    def describe_tables_tool(table_names: list) -> str:
        return describe_tables(conn, table_names)

    return Tool(
        name="describe_tables",
        description="Use this tool to describe the tables in the database.",
        func=describe_tables_tool,
        args_schema=DescribeTablesArgsSchema,
    )

# Create the SQL tool with a connection to the database
conn = connect_to_db("db.sqlite")  # Use the correct path to the database
if conn:
    sql_tool = create_sql_tool(conn)
    describe_tables_tool = create_describe_tables_tool(conn)
else:
    print("Failed to create SQL tool due to connection issues.")

