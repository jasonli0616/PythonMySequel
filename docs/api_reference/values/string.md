# String

```python
class pythonmysequel.values.String(column_limit:int=255, **options)
```

**Source code**: [pythonmysequel/values/String.py](https://github.com/jasonli0616/PythonMySequel/blob/main/pythonmysequel/values/String.py)

### Parameters:
- **column_limit: int** - `VARCHAR` column limit
- ****options: bool** - Data type options
  - `(NOT_NULL=True)`

### Methods and attributes:
`column_limit -> int`\
Returns the `VARCHAR` column limit

`options -> str`\
Data type options

`PYTHON_TYPE -> type`\
Returns the Python equivalent data type ([str](https://docs.python.org/3/library/stdtypes.html#str))

`SQL_TYPE -> str`\
Returns the SQL equivalent data type ([VARCHAR](https://dev.mysql.com/doc/refman/8.0/en/char.html))

`_column_limit_validation(column_limit:int) -> None` (private method)\
Validates `VARCHAR` column limit

`_get_options(database:str) -> str` (private method)\
Parses data type options