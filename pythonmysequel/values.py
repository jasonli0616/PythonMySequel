'''
Custom value type classes for creating tables
'''

class String():
    def __init__(self, character_limit:int = 255, **options) -> None:
        self.SQL_TYPE = f'VARCHAR({character_limit})'
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
    
    def get_SQL_value(self):
        return f'{self.SQL_TYPE} {self.options}'.strip()

class Int:
    def __init__(self, **options) -> None:
        self.SQL_TYPE = 'INT'
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

    def get_SQL_value(self):
        return f'{self.SQL_TYPE} {self.options}'.strip()

class Bool:
    def __init__(self, **options) -> None:
        self.SQL_TYPE = 'BOOLEAN'
        self.options = self.get_options(options)

    def get_options(self, options:tuple):
        options_string = ''
        if 'NOT_NULL' in options and options['NOT_NULL']:
            options_string += 'NOT NULL '
        return options_string.strip()

    def get_SQL_value(self):
        return f'{self.SQL_TYPE} {self.options}'.strip()

APPROVED_TYPES = [
    String,
    Int,
    Bool
]