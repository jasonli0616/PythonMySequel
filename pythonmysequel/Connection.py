'''
A class for connecting to the database
as well as interacting with the database
(eg. creating tables, inserting into tables, etc)
'''

import mysql.connector
from .values import *
from .Row import Row
from .Table import Table

class Connection:
    def __init__(self,
        user:str,
        password:str,
        host:str = '127.0.0.1',
        database:str = None
    ):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        self.cursor = self.connection.cursor()

    def _execute(self, query:str):
        self.cursor.execute(query)
        self.connection.commit()

    def _check_value_type(self, values:dict):
        for value_name, value_type in values.items():
            if type(value_type) != _ValueType:
                raise TypeError(f'Unsupported value type {value_type} for {value_name}')

    def create_table(self,
        table:Table
    ):
        execute_string = table._get_create_string()
        try:
            self._execute(execute_string)
        except mysql.connector.Error as e:
            print(e)
    
    def drop_table(self,
        table
    ):
        if type(table) == Table:
            execute_string = f'DROP TABLE `{table.table_name}`'
        else:
            execute_string = f'DROP TABLE `{table}`'
        try:
            self._execute(execute_string)
        except mysql.connector.Error as e:
            print(e)
    
    def insert(self,
        row:Row
    ):
        table = row.table

        execute_string = f'INSERT INTO `{table.table_name}` ('
        for column_name in row.values.keys():
            execute_string += f'`{column_name}`, '
        execute_string = execute_string.removesuffix(', ')
        execute_string += ') VALUES ('
        for value in row.values.values():
            execute_string += f"'{value}', "
        execute_string = execute_string.removesuffix(', ')
        execute_string += ')'
        
        try:
            self._execute(execute_string)
        except mysql.connector.Error as e:
            print(e)