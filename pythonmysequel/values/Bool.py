from ._ValueType import _ValueType

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
