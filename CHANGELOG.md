# Changelog
All notable changes will be documented in this file.

---

## v0.2.0 - In development
### Added
- SQL injection protection
- Ability to see last query run in SQL syntax

### Changed
- Most [pythonmysequel.Connection](https://jasonli0616.github.io/PythonMySequel/#/api_reference/connection) method code, to support SQL injection protection
- Execute query method (removed method, using [native `MySQLCursor.execute()`](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html))
- Enabled [MySQLConnection.autocommit](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-autocommit.html)
- Changed [selecting](https://jasonli0616.github.io/PythonMySequel/#/getting_started/examples/query) conditions (`WHERE`)

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