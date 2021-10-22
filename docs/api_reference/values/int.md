# Int

```python
class pythonmysequel.values.Int(**options)
```

**Source code**: [pythonmysequel/values/Int.py](https://github.com/jasonli0616/PythonMySequel/blob/main/src/pythonmysequel/values/Int.py)

### Parameters:
- ****options: bool** - Data type options
  - `(NOT_NULL=True)`
  - `(AUTO_INCREMENT=True)` (not supported by [`SQLite_Connector`](api_reference/sqlite_connector.md))
  - `(PRIMARY_KEY=True)`

### Methods and attributes:
`options -> str`\
Data type options

`PYTHON_TYPE -> type`\
Returns the Python equivalent data type ([int](https://docs.python.org/3/library/functions.html#int))

`SQL_TYPE -> str`\
Returns the SQL equivalent data type ([INT](https://dev.mysql.com/doc/refman/8.0/en/integer-types.html))

`_get_options(database:str) -> str` (private method)\
Parses data type options