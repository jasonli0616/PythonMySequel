# Row

```python
class pythonmysequel.Row(table:pythonmysequel.Table, **values)
```

**Source code**: [pythonmysequel/Row.py](https://github.com/jasonli0616/PythonMySequel/blob/main/pythonmysequel/Row.py)

### Parameters:
- **table: pythonmysequel.Table** - The table that this row/record is in
- ****values: Any** - The data in this record

### Methods and attributes:
`table -> pythonmysequel.Table`\
Returns the table that this record is in

`values -> dict[str, Any]`\
Returns the data of this record

`_add_value() -> None` (protected method)\
Adds values to the record

`_check_value_type() -> None` (private method)\
Checks if the data types in the record matches table columns, else raise error

`__str__() -> str` (private method)\
Returns row in a dictionary-style string, when `print(pythonmysequel.Row)` is called