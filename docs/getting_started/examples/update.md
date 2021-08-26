# Updating Records

To update a record, you must first [`select`](getting_started/examples/query.md) a row. Then, you pass in that row as an argument to the [`Connection.update`](api_reference/connection.md#methods-and-attributes) method.

Current table:

| id | first_name | last_name | age |
|----|------------|-----------|-----|
| 1  | Bob        | Jones     | 25  |
| 2  | John       | Smith     | 43  |
| 3  | Abi        | Roberts   | 32  |

```python
# Get a row
bob = db.query('*', users_table, where="first_name='Bob'")[0]
```
Returns:

| id | first_name | last_name | age |
|----|------------|-----------|-----|
| 1  | Bob        | Jones     | 25  |

```python
db.update(bob, age=30)
```
SQL equivalent code:
```sql
UPDATE `users_table`
SET `age`=30
WHERE `id`=1;
```

Updated table:

| id | first_name | last_name | age |
|----|------------|-----------|-----|
| 1  | Bob        | Jones     | 30  |
| 2  | John       | Smith     | 43  |
| 3  | Abi        | Roberts   | 32  |

Though it is recommended to have a [primary key](https://dev.mysql.com/doc/refman/8.0/en/primary-key-optimization.html) column, it is not required in PythonMySequel.\
PythonMySequel will be able to update records without a primary key, but there is a chance of error.\
(If there are two records that have the same data, both will be updated)

Without a primary key, the PythonMySequel code is the same but the SQL equivalent will be:
```sql
UPDATE `users_table`
SET `age`=30
WHERE `first_name`='Bob' AND `last_name`='Jones' AND `age`=25;
```
PythonMySequel will use every column in the table to update the correct record.