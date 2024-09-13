# services/weight_service.py

"""
WeightWise Weight Service

Manage weight data, including logging and analysis.
"""

from datetime import datetime
from data.database import get_connection
from models.weight_log import WeightLog
from models.user import User
from models.analysis import Analysis

class WeightService:
    def __init__(self):
        self.connection = get_connection()

    def log_weight(self, user_id, weight):
        """
        Log a new weight entry for a user.
        """
        date = datetime.now().strftime('%Y-%m-%d')
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO weight_logs (user_id, date, weight)
                VALUES (?, ?, ?)
            ''', (user_id, date, weight))
            self.connection.commit()

    def get_weight_logs(self, user_id):
        """
        Retrieve all weight logs for a user.
        """
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT id, user_id, date, weight FROM weight_logs
            WHERE user_id = ?
            ORDER BY date
        ''', (user_id,))
        rows = cursor.fetchall()
        return [WeightLog.from_row(row) for row in rows]

    def analyze_weight(self, user_id):
        """
        Perform analysis on the user's weight logs and generate alerts.
        """
        logs = self.get_weight_logs(user_id)
        weight_logs = [{'weight': log.weight} for log in logs]
        analysis = Analysis(weight_logs)
        changes = analysis.calculate_weekly_changes()
        alerts = analysis.generate_alerts(changes)
        return changes, alerts

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()
