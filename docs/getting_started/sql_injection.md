# SQL Injection

### What is SQL Injection?
Without going into too much detail, SQL injection is when a user inputs SQL code in place of text.

##### Example:
Here is a hypothetical piece of code that could run when a user is asked for their name.\
`{input_first_name}` and `{input_last_name}` are set to exactly what the user inputs.\
```sql
INSERT INTO `users` (`first_name`, `last_name`)
VALUES ('{input_first_name}', '{input_last_name}');
```
Normally, a user would input their name, and the code would run as normal.\
`{input_first_name}` = Bob\
`{input_last_name}` = Jones
```sql
INSERT INTO `users` (`first_name`, `last_name`)
VALUES ('Bob', 'Jones');
```
However, someone could also input SQL code, causing harm to the database.\
`{input_first_name}` = Bob\
`{input_last_name}` = Jones'); DROP TABLE \`users`;
```sql
INSERT INTO `users` (`first_name`, `last_name`)
VALUES ('Bob', 'Jones'); DROP TABLE `users`;');
```
As you can see, the user inputted a query to drop the entire users table.\
The reason that this works is because when the code is run, the `');` that the user inputted ends the `INSERT` statement and starts a new `DROP` statement.

Other examples of SQL injection include using `OR 1=1` (always returns true), using `--` (comments) to block a line of code, and more.

You can see how this is dangerous, because an attacker can gain access to an account, for example, using SQL injection.\
Querying a database with the user inputted username and password:
```sql
SELECT * FROM `accounts`
WHERE username='{input_username}' AND password='{input_password}';
```
Using `OR 1=1`, the attacker is able to gain access to an account without the password./
This works because even if the password is incorrect, `1=1` is always true.

`{input_username}` = bob_jones\
`{input_password}` = incorrect_password' OR 1=1;
```sql
SELECT * FROM `accounts`
WHERE username='bob_jones123' AND password='incorrect_password' OR 1=1;';
```

---

### Preventing SQL Injection
The demostration above uses SQL code, rather than PythonMySequel. This is to demonstrate exactly what SQL injection does.

There is no SQL injection protection in PythonMySequel in order to prevent false positives.\
If an app uses PythonMySequel with their own built-in SQL injection protection, PythonMySequel will not set off a false error (eg. by blocking `;`, or `--`, or `OR 1=1` completely).

**Here are some ways you can prevent SQL injection in your code, by limiting special characters:** \
TLDR: Restrict the use of the characters `;`, `--`, and `=`

##### 1. Semicolons `;`
Semicolons end a statement in SQL.\
This function will check if the user input has a semicolon in it.\
In most scenarios, users will not have to input semicolons.
```python
def possible_sql_injection(user_input:str):
    if ';' in user_input:
        return True
    return False
```
##### 2. Comments `--`
Comments block out a line of code in SQL. SQL uses `--` (two dashes) as comments.\
This function will check if the user input has two dashes in it.\
In most scenarios, users will not have to input two dashes.
```python
def possible_sql_injection(user_input:str):
    if '--' in user_input:
        return True
    return False
```
##### 3. Equals `=`
The equals operator checks if two values are equal. They can be used as a condition, in situations such as querying a database.
This function will check if the user input has an equal sign in it.\
In most scenarios, users will not have to input an equals sign.
```python
def possible_sql_injection(user_input:str):
    if '=' in user_input:
        return True
    return False
```

##### Conclusion
The functions above should be called before inserting into a table.\
If the function(s) return `True`, the data should not be inserted.
```python
if possible_sql_injection(user_input):
    # error handling
else:
    db.insert(pythonmysequel.row(table,
        data=user_input
    ))
```