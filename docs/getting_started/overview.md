# Overview

### Introduction
PythonMySequel is an object oriented MySQL connector for Python. It's based off of the [MySQL Python connector](https://dev.mysql.com/doc/connector-python/en/).
It is designed to be easy to use, with Python code instead of SQL.

As an example, instead of writing:
```sql
SELECT * FROM `table`;
```
you would write:
```python
db.select('*', table)
```

### What PythonMySequel is:
- A simple to use MySQL connector
- For programs and applications to write to a database
  - Eg. user signup
- For programs and applications to query a database
  - Eg. user login
- For simple automatic database management/creation

### What PythonMySequel is *not*:
- A library to make extensive database changes
  - Anything requiring manual SQL queries
  - Eg. altering, and changing database structure
- Connecting to other SQL servers
  - Eg. PostgreSQL, SQLite
