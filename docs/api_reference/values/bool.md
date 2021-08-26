# Bool

```python
class pythonmysequel.values.Bool(**options)
```

**Source code**: [pythonmysequel/values/Bool.py](https://github.com/jasonli0616/PythonMySequel/blob/main/pythonmysequel/values/Bool.py)

### Parameters:
- ****options: bool** - Data type options
  - `(NOT_NULL=True)`

### Methods and attributes:
`options -> str`\
Data type options

`PYTHON_TYPE -> type`\
Returns the Python equivalent data type ([bool](https://docs.python.org/3/library/functions.html#bool))

`SQL_TYPE -> str`\
Returns the SQL equivalent data type ([TINYINT](https://dev.mysql.com/doc/refman/8.0/en/integer-types.html))

`_get_options(database:str) -> str` (private method)\
Parses data type options