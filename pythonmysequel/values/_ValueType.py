class _ValueType:
    def get_SQL_value(self):
        return f'{self.SQL_TYPE} {self.options}'.strip()