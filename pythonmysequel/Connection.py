'''
A class for connecting to the database
as well as interacting with the database
(eg. creating tables, inserting into tables, etc)
'''

import mysql.connector
import warnings
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
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.last_query = ''
    
    def use_database(self, database:str):
        try:
            self.cursor.execute(f'USE {database}')
            self.last_query = (f'USE {database}')
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def create_database(self, database:str):
        try:
            self.cursor.execute(f'CREATE DATABASE {database}')
            self.last_query = (f'CREATE DATABASE {database}')
        except mysql.connector.Error as e:
            warnings.warn(e)

    def create_table(self,
        table:Table
    ):
        execute_string = table._get_create_string()

        if not table._has_primary_key:
            warnings.warn(f'Table {table.table_name} has no primary key')

        try:
            self.cursor.execute(execute_string)
            self.last_query = (execute_string)
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def drop_table(self,
        table
    ):
        if type(table) == Table:
            execute_string = f'DROP TABLE `{table.table_name}`'
        elif type(table) == str:
            execute_string = f'DROP TABLE `{table}`'
        else:
            raise TypeError(f'Incorrect type {type(table)} for table')

        try:
            self.cursor.execute(exec)
            self.last_query = (execute_string)
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def insert(self,
        row:Row
    ):
        table = row.table

        percent_s = '%s'
        execute_string = f'INSERT INTO {table.table_name} ' + f"{str(tuple(list(i for i in row.values.keys())))} ".replace("'", "") + f'VALUES {str(tuple(list(map(lambda i: percent_s, row.values))))}'.replace("'%s'", "%s")

        execute_data = list(i for i in row.values.values())
        
        try:
            self.cursor.execute(execute_string, execute_data)
            self.last_query = (execute_string % tuple(execute_data))
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def select(self,
        columns,
        table:Table,
        **where
    ):
        if columns != '*' and type(columns) != list:
            raise TypeError(f'Incorrect type {type(columns)} for columns')

        execute_string = f'SELECT {columns} '.replace('[', '').replace(']', '').replace("'", "") + f'FROM {table.table_name}'
        execute_data = []

        percent_s = '%s'
        if where:
            for key, value, times in zip(where.keys(), where.values(), range(len(where))):
                condition_keyword = 'WHERE' if times == 0 else 'AND'
                execute_string += f' {condition_keyword} {key}=%s'
                execute_data.append(value)

        try:
            self.cursor.execute(execute_string, execute_data)
            self.last_query = (execute_string % tuple(execute_data))
            data = self.cursor.fetchall()

            rows = []

            if columns == '*':
                columns = [i for i in table.values.keys()]

            for row in data:
                r = Row(table)
                for column, index in zip(row, columns):
                    r._add_value({index: column})
                rows.append(r)

            return rows
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def update(self,
        row:Row,
        **set
    ):
        table = row.table

        execute_string = f'UPDATE {table.table_name} SET'
        for column in set.keys():
            execute_string += f' {column}=%s,'
        execute_string = execute_string.removesuffix(',')
        execute_data = list(i for i in set.values())

        if table._has_primary_key():
            execute_string += f' WHERE {table.primary_key}=%s'
            execute_data.append(row.values[table.primary_key])

        else:
            warnings.warn(f'Table {table.table_name} has no primary key')

            for column, v, times in zip(row.values.keys(), row.values.items(), range(len(row.values))):
                condition_keyword = 'WHERE' if times == 0 else 'AND'
                execute_string += f" {condition_keyword} {column}=%s"
                execute_data.append(v)

        try:
            self.cursor.execute(execute_string, execute_data)
            self.last_query = (execute_string % tuple(execute_data))
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def delete(self,
        row:Row
    ):
        table = row.table

        execute_string = f'DELETE FROM {table.table_name}'
        execute_data = []

        if table._has_primary_key():
            execute_string += f' WHERE {table.primary_key}=%s'
            execute_data.append(row.values[table.primary_key])

        else:
            warnings.warn(f'Table {table.table_name} has no primary key')

            for column, v, times in zip(row.values.keys(), row.values.items(), range(len(row.values))):
                condition_keyword = 'WHERE' if times == 0 else 'AND'
                execute_string += f" {condition_keyword} {column}=%s"
                execute_data.append(v)

        try:
            self.cursor.execute(execute_string, execute_data)
            self.last_query = (execute_string % tuple(execute_data))
        except mysql.connector.Error as e:
            warnings.warn(e)