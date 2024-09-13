# models/weight_log.py

"""
WeightWise Weight Log Model

Define the WeightLog model and its operations.
"""

class WeightLog:
    def __init__(self, log_id, user_id, date, weight):
        self.log_id = log_id
        self.user_id = user_id
        self.date = date
        self.weight = weight

    @classmethod
    def from_row(cls, row):
        return cls(log_id=row[0], user_id=row[1], date=row[2], weight=row[3])

    def __repr__(self):
        return f"WeightLog(id={self.log_id}, user_id={self.user_id}, date='{self.date}', weight={self.weight:.2f})"
