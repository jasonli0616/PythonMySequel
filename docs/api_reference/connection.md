# Connection

```python
class pythonmysequel.Connection(user:str, password:str, host:str='127.0.0.1')
```

**Source code**: [pythonmysequel/Connection.py](https://github.com/jasonli0616/PythonMySequel/blob/main/pythonmysequel/Connection.py)

### Parameters:
- **user: str** - MySQL server username
- **password: str** - MySQL server password
- **host: str** - MySQL server address

### Methods and attributes:
`connection -> mysql.connector.MySQLConnection`\
Returns the [MySQL connection](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection.html)

`create_database(database:str) -> None`\
Create a database

`create_table(table:pythonmysequel.Table) -> None`\
Creates a table

`cursor -> mysql.connector.cursor.MySQLCursor`\
Returns the [MySQL cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

`delete(row:pythonmysequel:Row) -> None`\
Delete record(s) in a table

`drop_table(table:pythonmysequel.Table) -> None`\
Drops/removes a table

`insert(row:pythonmysequel.Row) -> None`\
Inserts a record into a table

`last_query -> str`\
Returns the last query run, in SQL syntax

`select(columns:list | str, table:pythonmysequel.Table, **where) -> list[pythonmysequel.Row]`\
Finds record(s) in a table

`update(row:pythonmysequel:Row, **set) -> None`\
Update record(s) in a table

`use_database(database:str) -> None`\
Use an existing database

`_execute(execute_string:str, execute_data:tuple=None) -> None` (private method)\
Executes a query

---

# SQLite_Connection

```python
class pythonmysequel.SQLite_Connection(database:str)
```
Inherits [`pythonmysequel.Connection`](api_reference/connection.md#connection) object

**Source code**: [pythonmysequel/SQLite_Connection.py](https://github.com/jasonli0616/PythonMySequel/blob/main/pythonmysequel/SQLite_Connection.py)

### Parameters:
- **database: str** - name of database file

### Methods and attributes:
`connection -> sqlite3.Connection`\
Returns the [SQLite connection](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection)

`create_database(database:str) -> None`\
Create a database

`create_table(table:pythonmysequel.Table) -> None`\
Creates a table

`cursor -> sqlite3.Cursor`\
Returns the [SQLite cursor](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor)

`delete(row:pythonmysequel:Row) -> None`\
Delete record(s) in a table

`drop_table(table:pythonmysequel.Table) -> None`\
Drops/removes a table

`insert(row:pythonmysequel.Row) -> None`\
Inserts a record into a table\

`last_query -> str`\
Returns the last query run, in SQL syntax

`select(columns:list | str, table:pythonmysequel.Table, **where) -> list[pythonmysequel.Row]`\
Finds record(s) in a table

`update(row:pythonmysequel:Row, **set) -> None`\
Update record(s) in a table

`use_database(database:str) -> None`\
Use an existing database

`_execute(execute_string:str, execute_data:tuple=None) -> None` (private method)\
Executes a query