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
`connection -> mysql.connector.MySQLConnection()`\
Returns the MySQL connection

`create_database(database:str) -> None`\
Create a database

`create_table(table:pythonmysequel.Table) -> None`\
Creates a table

`cursor -> mysql.connector.cursor.MySQLCursor()`\
Returns the MySQL cursor

`delete(row:pythonmysequel:Row) -> None`\
Delete record(s) in a table

`drop_table(table:pythonmysequel.Table) -> None`\
Drops/removes a table

`insert(row:pythonmysequel.Row) -> None`\
Inserts a record into a table

`select(columns:list | str, table:pythonmysequel.Table, where:str=None) -> list[pythonmysequel.Row]`\
Finds record(s) in a table

`update(row:pythonmysequel:Row, **set) -> None`\
Update record(s) in a table

`use_database(database:str) -> None`\
Use an existing database

`_execute(query:str, commit=True) -> None` (private method)\
Executes a query