# Table

```python
class pythonmysequel.Table(table_name:str, **values:pythonmysequel.values._ValueType)
```

**Source code**: [pythonmysequel/Table.py](https://github.com/jasonli0616/PythonMySequel/blob/main/pythonmysequel/Table.py)

### Parameters:
- **table_name: str** - Name of the table
- ****values: pythonmysequel.values._ValueType** - Table columns

### Methods and attributes:
`primary_key -> None | str`\
Returns the primary key column name if exists, else None

`table_name -> str`\
Returns the name of the table

`values -> dict[str, pythonmysequel.values._ValueType]`\
Returns the name of the table

`_has_primary_key() -> bool` (protected method)\
Returns true if table has primary key column, else return false