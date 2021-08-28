# Querying/Selecting Records

The [`Connection.select()`](api_reference/connection.md#methods-and-attributes) method will return **a list** of the [`Row`](api_reference/row.md) object.
```python
all_users = db.select('*', users_table)
query2 = db.select(['last_name', 'age'], users_table)
query3 = db.select(['first_name', 'last_name'], users_table, age=25)
```
SQL equivalent code:
```sql
SELECT * FROM `users_table`;
SELECT `last_name`, `age` FROM `users_table`;
SELECT `first_name`, `last_name` FROM `users_table` WHERE age=25;
```

To iterate through the returned list, you can use a for loop. This will loop through each of the [`Row`](api_reference/row.md) objects.
```python
for user in all_users:
    print(user)
```
To return only the first [`Row`](api_reference/row.md), you can use `[0]`, as it is a Python list.
```python
user1 = db.select('*', users_table)[0]
```

See below for more example usages:

---

##### **Examples with more records:**
Inserting more records into the database, to demonstrate querying using PythonMySequel.
```python
db.insert(pythonmysequel.Row(users_table,
    first_name='Bob', last_name='Jones', age=25
))
db.insert(pythonmysequel.Row(users_table,
    first_name='John', last_name='Smith', age=43
))
db.insert(pythonmysequel.Row(users_table,
    first_name='Abi', last_name='Roberts', age=32
))
```
#### Query example 1:
**This example will select all records in the table.**

SQL equivalent:
```sql
SELECT * FROM `users_table`;
```
PythonMySequel code:
```python
all_users = db.select('*', users_table)
```
Returns `-> list[pythonmysequel.Row]`:
```
[
    {'id': 1, 'first_name': 'Bob', 'last_name': 'Jones', 'age': 25}
    {'id': 2, 'first_name': 'John', 'last_name': 'Smith', 'age': 43}
    {'id': 3, 'first_name': 'Abi', 'last_name': 'Roberts', 'age': 32}
]
```
Represented as table:

| id | first_name | last_name | age |
|----|------------|-----------|-----|
| 1  | Bob        | Jones     | 25  |
| 2  | John       | Smith     | 43  |
| 3  | Abi        | Roberts   | 32  |

#### Query example 2:
**This example will select all records in the table, but only the `last_name` and `age` columns.**

SQL equivalent:
```sql
SELECT `last_name`, `age` FROM `users_table`;
```
PythonMySequel code:
```python
query = db.select(['last_name', 'age'], users_table)
```
Returns `-> list[pythonmysequel.Row]`:
```
[
    {'last_name': 'Jones', 'age': 25}
    {'last_name': 'Smith', 'age': 43}
    {'last_name': 'Roberts', 'age': 32}
]
```
Represented as table:

| last_name | age |
|-----------|-----|
| Jones     | 25  |
| Smith     | 43  |
| Roberts   | 32  |

#### Query example 3:
**This example will select all records in the table if the `age` is equal to 25, but only the `first_name` and `last_name` columns.**

SQL equivalent:
```sql
SELECT `first_name`, `last_name` FROM `users_table` WHERE age=25;
```
PythonMySequel code:
```python
query = db.select(['first_name', 'last_name'], users_table, age=25)
```
Returns `-> list[pythonmysequel.Row]`:
```
[
    {'first_name': 'Bob', 'last_name': 'Jones'}
]
```
Represented as table:

| first_name | last_name |
|------------|-----------|
| Bob        | Jones     |
