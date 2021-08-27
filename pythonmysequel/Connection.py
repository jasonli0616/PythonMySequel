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
    
    def use_database(self, database:str):
        try:
            self.cursor.execute('USE %(database)s', {'database':database})
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def create_database(self, database:str):
        try:
            self.cursor.execute('CREATE DATABASE %(database)s', {'database':database})
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
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def drop_table(self,
        table
    ):
        execute_data = {}

        if type(table) == Table:
            execute_data['table_name'] = table.table_name
        else:
            execute_data['table_name'] = table

        try:
            self.cursor.execute('DROP TABLE %(table_name)s', execute_data)
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def insert(self,
        row:Row
    ):
        table = row.table
        execute_data = {}

        execute_data['table_name'] = table.table_name
        execute_data['columns'] = ''
        for column_name in row.values.keys():
            execute_data['columns'] += f'{column_name}, '
        execute_data['columns'] = execute_data['columns'].removesuffix(', ')

        execute_data['values'] = ''
        for value in row.values.values():
            execute_data['values'] += f"{value}, "
        execute_data['values'] = execute_data['values'].removesuffix(', ')
        
        try:
            self.cursor.execute('INSERT INTO %(table_name)s (%(columns)s) VALUES (%(values)s)', execute_data)
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def select(self,
        columns,
        table:Table,
        where:str=None
    ):
        execute_data = {}

        if columns == '*':
            execute_data['columns'] = '*'
        elif type(columns) == list:
            execute_data['columns'] = ''
            for column in columns:
                execute_data['columns'] += f'{column}, '
            execute_data['columns'] = execute_data.removesuffix(', ')
        else:
            raise TypeError(f'Incorrect type {type(columns)} for columns')

        execute_data['table'] = table.table_name

        if where:
            execute_data['where'] = where

        try:
            if where:
                self.cursor.execute('SELECT %(columns)s FROM %(table)s WHERE %(where)s', execute_data)
            else:
                self.cursor.execute('SELECT %(columns)s FROM %(table)s', execute_data)
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
        execute_data = {}

        execute_data['table']

        execute_data['set'] = ''
        for column, value in set.items():
            execute_data['set'] += f'{column} = {value}, '
        execute_data['set'] = execute_data['set'].removesuffix(', ')

        if table._has_primary_key():
            execute_data['where'] = f'{table.primary_key}={row.values[table.primary_key]}'

        else:
            warnings.warn(f'Table {table.table_name} has no primary key')

            execute_data['where'] = ''
            for column, v in row.values.items():
                execute_data['where'] += f"{column} = '{v}' AND "
            execute_data['where'] = execute_data['where'].removesuffix(' AND ')

        try:
            self.cursor.execute('UPDATE %(table)s SET %(set)s WHERE %(where)s', execute_data)
        except mysql.connector.Error as e:
            warnings.warn(e)
    
    def delete(self,
        row:Row
    ):
        table = row.table
        execute_data = {}

        execute_data['table'] = table.table_name

        if table._has_primary_key():
            execute_data['where'] = f'{table.primary_key}={row.values[table.primary_key]}'

        else:
            warnings.warn(f'Table {table.table_name} has no primary key')

            execute_data['where'] = ''
            for column, v in row.values.items():
                execute_data['where'] += f"{column} = '{v}' AND "
            execute_data['where'] = execute_data['where'].removesuffix(' AND ')

        try:
            self.cursor.execute('DELETE FROM %(table)s WHERE %(where)s', execute_data)
        except mysql.connector.Error as e:
            warnings.warn(e)