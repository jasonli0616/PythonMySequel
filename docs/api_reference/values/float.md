# Float

```python
class pythonmysequel.values.Float(**options)
```

**Source code**: [pythonmysequel/values/Float.py](https://github.com/jasonli0616/PythonMySequel/blob/main/src/pythonmysequel/values/Float.py)

### Parameters:
- ****options: bool** - Data type options
  - `(NOT_NULL=True)`

### Methods and attributes:
`options -> str`\
Data type options

`PYTHON_TYPE -> type`\
Returns the Python equivalent data type ([float](https://docs.python.org/3/library/functions.html#float))

`SQL_TYPE -> str`\
Returns the SQL equivalent data type ([FLOAT](https://dev.mysql.com/doc/refman/8.0/en/floating-point-types.html))

`_get_options(database:str) -> str` (private method)\
Parses data type options