'''
Custom value type classes for creating tables
'''

class _ValueType:
    def get_SQL_value(self):
        return f'{self.SQL_TYPE} {self.options}'.strip()

class String(_ValueType):
    def __init__(self, character_limit:int = 255, **options) -> None:
        self.SQL_TYPE = f'VARCHAR({character_limit})'
        self.PYTHON_TYPE = str
        
        self.character_limit_validation(character_limit)
        self.character_limit = character_limit

        self.options = self.get_options(options)

    def character_limit_validation(self, character_limit:int):
        if character_limit > 255 or character_limit < 1:
            raise ValueError(f'VARCHAR/String character limit {character_limit} out of range')

    def get_options(self, options:tuple):
        options_string = ''
        if 'NOT_NULL' in options and options['NOT_NULL']:
            options_string += 'NOT NULL '
        return options_string.strip().strip()

class Int(_ValueType):
    def __init__(self, **options) -> None:
        self.SQL_TYPE = 'INT'
        self.PYTHON_TYPE = int

        self.options = self.get_options(options)

    def get_options(self, options:tuple):
        options_string = ''
        if 'NOT_NULL' in options and options['NOT_NULL']:
            options_string += 'NOT NULL '
        if 'AUTO_INCREMENT' in options and options['AUTO_INCREMENT']:
            options_string += 'AUTO_INCREMENT '
        if 'PRIMARY_KEY' in options and options['PRIMARY_KEY']:
            options_string += 'PRIMARY KEY '
        return options_string.strip()

class Float(_ValueType):
    def __init__(self, **options) -> None:
        self.SQL_TYPE = 'FLOAT'
        self.PYTHON_TYPE = float

        self.options = self.get_options(options)

    def get_options(self, options:tuple):
        options_string = ''
        if 'NOT_NULL' in options and options['NOT_NULL']:
            options_string += 'NOT NULL '
        return options_string.strip()

class Bool(_ValueType):
    def __init__(self, **options) -> None:
        self.SQL_TYPE = 'BOOLEAN'
        self.PYTHON_TYPE = self.PYTHON_TYPE = bool

        self.options = self.get_options(options)

    def get_options(self, options:tuple):
        options_string = ''
        if 'NOT_NULL' in options and options['NOT_NULL']:
            options_string += 'NOT NULL '
        return options_string.strip()
