from .Table import Table
from .values import *

class Row:
    def __init__(self,
        table:Table,
        **values
    ) -> None:
        self.table = table
        self.values = values

        self._check_value_type()
    
    def _check_value_type(self):
        for value_type, value, column_name in zip(self.table.values.values(), self.values.values(), self.values):
            inputted_value_type = type(value)
            python_value_type = value_type.PYTHON_TYPE

            if inputted_value_type !=  python_value_type:
                raise ValueError(f'Incorrect value type {inputted_value_type} for column "{column_name}" {python_value_type}')