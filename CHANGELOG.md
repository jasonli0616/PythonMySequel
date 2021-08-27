# Changelog
All notable changes will be documented in this file.

---

## v0.2.0 - In development
### Added
- SQL injection protection
- Ability to see last query run in SQL syntax
- Backticks (`` ` ``) when table name used to prevent user error

### Changed
- Most [`pythonmysequel.Connection` method](https://jasonli0616.github.io/PythonMySequel/#/api_reference/connection?id=methods-and-attributes) code, to support SQL injection protection
- Execute query method (removed method, using [native `MySQLCursor.execute()`](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html))
- Create table method (removed [`pythonmysequel.Table._get_create_string()` method](https://jasonli0616.github.io/PythonMySequel/#/api_reference/table?id=methods-and-attributes), modify [`pythonmysequel.Connection.create_table()` method](https://jasonli0616.github.io/PythonMySequel/#/api_reference/connection?id=methods-and-attributes))
- Enabled [MySQLConnection.autocommit](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-autocommit.html)
- Changed [selecting](https://jasonli0616.github.io/PythonMySequel/#/getting_started/examples/query) conditions (`WHERE`)

### Removed
- [`pythonmysequel.Connection._execute()`](https://jasonli0616.github.io/PythonMySequel/#/api_reference/connection?id=methods-and-attributes) method
- [`pythonmysequel.Table._get_create_string()`](https://jasonli0616.github.io/PythonMySequel/#/api_reference/table?id=methods-and-attributes) method

## To-do:
- Add support for SQLite

---

## v0.1.0 - 26/08/2021
### Added
- Connection class for interacting with MySQL DB
- Ability to create, and use databases
- Ability to create, and drop tables
- Ability to insert into table
- Ability to query table
- Ability to update, and delete records