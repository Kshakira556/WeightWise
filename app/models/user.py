# models/user.py

"""
WeightWise User Model

Define the User model and its operations.
"""

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @classmethod
    def from_row(cls, row):
        return cls(user_id=row[0], name=row[1], email=row[2])
    
    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}', email='{self.email}')"
