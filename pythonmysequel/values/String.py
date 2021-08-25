from ._ValueType import _ValueType

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