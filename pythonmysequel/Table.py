from pythonmysequel.values import _ValueType


class Table:
    def __init__(self,
        table_name:str,
        **values:_ValueType
    ):
        self.table_name = table_name
        self.values = values
    
    def _get_create_string(self):
        '''
        This method returns the query to create this table
        '''
        values_string = ''
        for value_name, value_type in self.values.items():
            values_string += f'`{value_name}` {value_type.get_SQL_value()}, '

        return f'CREATE TABLE `{self.table_name}` ({values_string})'.replace(', )', ')')