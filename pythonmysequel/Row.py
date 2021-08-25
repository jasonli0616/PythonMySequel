from .values import *

class Row:
    def __init__(self,
        **values
    ) -> None:
        pass
    #     self._check_value_type(values)

    #     values_string = ''
    #     for value_name, value_type in values.items():
    #         values_string += f'{value_name} {value_type.get_SQL_value()}, '

    # def _check_value_type(self, values:dict):
    #     for value_name, value_type in values.items():
    #         if type(value_type) != ValueType:
    #             raise TypeError(f'Unsupported value type {value_type} for {value_name}')