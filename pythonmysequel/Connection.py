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
    ):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
        )

        self.cursor = self.connection.cursor()

    def _execute(self, query:str, commit=True):
        self.cursor.execute(query)
        if commit:
            self.connection.commit()
    
    def use_database(self, database:str):
        try:
            self._execute(f'USE {database}')
        except mysql.connector.Error as e:
            print(e)
    
    def create_database(self, database:str):
        try:
            self._execute(f'CREATE DATABASE {database}')
        except mysql.connector.Error as e:
            print(e)

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
    
    def select(self,
        columns,
        table:Table,
        where:str=None
    ):
        execute_string = 'SELECT '

        if columns == '*':
            execute_string += '*'
        elif type(columns) == list:
            for column in columns:
                execute_string += f'{column}, '
            execute_string = execute_string.removesuffix(', ')
        else:
            raise TypeError(f'Incorrect type {type(columns)} for columns')

        execute_string += f' FROM {table.table_name}'

        if where:
            execute_string += f' WHERE {where}'

        try:
            self._execute(execute_string, commit=False)
            data = self.cursor.fetchall()

            rows = []

            if columns == '*':

                for row in data:
                    r = Row(table)
                    for value, index in zip(table.values, range(0, len(table.values))):
                        r._add_value({value: row[index]})
                    rows.append(r)

            else:
                for row in data:
                    r = Row(table)
                    for column, index in zip(row, columns):
                        r._add_value({index: column})
                    rows.append(r)

            return rows
        except mysql.connector.Error as e:
            print(e)