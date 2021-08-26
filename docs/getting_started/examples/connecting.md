# Connecting to MySQL

To use PythonMySequel, you must have a [MySQL](getting_started/installation.md) server to connect to.

PythonMySequel uses a [`Connection`](api_reference/connection.md) object to manage the database. You can connect to the server when initializing the instance.
```python
import pythonmysequel

db = pythonmysequel.Connection(
    user='root',
    password='password',
    host='127.0.0.1' # Set to localhost by default
)
```

### Use database

Unlike other SQL connectors, PythonMySequel does not support using a database when connecting to the server. This is to prevent user error when connecting to a server without a database.

To create a database, use the [`Connection.create_database`](api_reference/connection.md#methods-and-attributes) method.\
To use a database, use the [`Connection.use_database`](api_reference/connection.md#methods-and-attributes) method.
```python
# Create a database if not already created:
db.create_database('my_website_db') # SQL: CREATE DATABASE `database_name`;

# Connect to database:
db.use_database('my_website_db') # SQL: USE `database_name`;
```
SQL equivalent code:
```sql
CREATE DATABASE `my_website_db`;
USE `my_website_db`;
```