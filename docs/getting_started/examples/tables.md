# Creating tables

To create a table, you need to use the [`Table`](api_reference/table.md) class.\
To set the table columns, you need to import and use the [value objects](api_reference/values.md).
```python
import pythonmysequel # main import
from pythonmysequel.values import * # Import value objects
```

Creating an instance of [`Table`](api_reference/table.md) does not add it to the database.\
Creating the instance will let PythonMySequel know that this table exists.
```python
# creating an instance of this class does not add it to the database
# creating the instance will let PythonMySequel know that this table exists

# eg. if there is a pre-existing table in the database, you will need to create the instance
# but you will not need to run the Connection.create_table method
users_table = pythonmysequel.Table('users_table', # table name
    # columns:
    id=Int(PRIMARY_KEY=True, AUTO_INCREMENT=True)
    first_name=String(30, NOT_NULL=True), # VARCHAR(30) NOT NULL
    last_name=String(30), # VARCHAR(30)
    age=Int() # INT
)
```
To add it to the database, call the [`Connection.create_table`](api_reference/connection.md) method.\
You do not need to call this method if you are just adding a pre-existing database to PythonMySequel (creating an instance).
```python
# create database method
db.create_table(users_table)
```
SQL equivalent code:
```sql
CREATE TABLE `users_table` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(30) NOT NULL,
    `last_name` VARCHAR(30),
    `age` INT
);
```