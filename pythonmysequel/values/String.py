from ._ValueType import _ValueType

class String(_ValueType):
    def __init__(self, column_limit:int = 255, **options) -> None:
        self.SQL_TYPE = f'VARCHAR({column_limit})'
        self.PYTHON_TYPE = str
        
        self.column_limit_validation(column_limit)
        self.column_limit = column_limit

        self.options = self.get_options(options)

    def column_limit_validation(self, column_limit:int):
        if column_limit > 255 or column_limit < 1:
            raise ValueError(f'VARCHAR/String character limit {column_limit} out of range')

    def get_options(self, options:tuple):
        options_string = ''
        if 'NOT_NULL' in options and options['NOT_NULL']:
            options_string += 'NOT NULL '
        return options_string.strip()