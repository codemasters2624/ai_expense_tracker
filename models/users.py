from datetime import date

class User:
    def __init__(self, name: str, id: int, created_at: date=None):
        self.name = name
        self.id = id
        self.created_at = created_at