# Other

Congratulations! You made it to the end of the getting started guide. You have seen everything that PythonMySequel was designed to do.\
Here, we have included some more information on running things with PythonMySequel that it wasn't designed to do, but are still able to handle.

PythonMySequel is designed to be an easy to use library. This means it is unable to do more complex queries such as `ALTER`, or support foreign keys.

If you are looking for a Python library to run complex custom things, we recommend checking out the [Python MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) or [Python SQLite connector](https://docs.python.org/3/library/sqlite3.html).

You are still, however, able to do these things using the [`Connection._execute()`](api_reference/connection.md#methods-and-attributes) method.\
This method allows you to run your own SQL query. This method was designed to be a private method that is only used within library source code, however you are able to use it to run your own queries.

You should be able to pass in your custom SQL query as a string to the method to run it. However, this PythonMySequel will not be able to prevent SQL injection. You can read [our tips](getting_started/sql_injection.md#preventing-sql-injection) on preventing SQL injection. You can also check out the [PythonMySequel native way](getting_started/sql_injection.md#native-way).
