# Inserting Records

To insert a record into a table using PythonMySequel, you must create an instance of the [`Row`](api_reference/row.md) class, then call the [`Connection.insert`](api_reference/connection.md#methods-and-attributes) method.
```python
# insert method
db.insert(
    # Row instance
    pythonmysequel.Row(users_table, # table to insert into
        # data:
        first_name='Bob',
        last_name='Jones',
        age=25
    )
)
```
SQL equivalent code:
```sql
INSERT INTO `users_table` (`first_name`, `last_name`, `age`)
VALUES ('Bob', 'Jones', 25);
```
