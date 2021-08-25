'''
A class for connecting to the database
as well as interacting with the database
(eg. creating tables, inserting into tables, etc)
'''

import mysql.connector
from .values import *

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
            database=database)
        self.cursor = self.connection.cursor()
    
    def _execute(self, query:str):
        self.cursor.execute(query)
        self.connection.commit()

    def _check_value_type(self, values:dict):
        for value_name, value_type in values.items():
            if value_type not in APPROVED_TYPES and type(value_type) not in APPROVED_TYPES:
                raise TypeError(f'Unsupported value type {value_type} for {value_name}')
    
    def create_table(self,
        table_name:str,
        **values
    ):
        self._check_value_type(values)

        values_string = ''
        for value_name, value_type in values.items():
            values_string += f'{value_name} {value_type.get_SQL_value()}, '

        execute_string = f'CREATE TABLE {table_name} ({values_string})'.replace(', )', ')')
        
        self._execute(execute_string)
    
    def drop_table(self,
        table_name:str
    ):
        execute_string = f'DROP TABLE {table_name}'
        try:
            self._execute(execute_string)
        except mysql.connector.errors.ProgrammingError as e:
            print(e)