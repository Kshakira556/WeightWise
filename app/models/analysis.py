# models/analysis.py

"""
WeightWise Analysis Module

Perform weight change analysis and generate alerts.
"""

class Analysis:
    def __init__(self, weight_logs):
        self.weight_logs = weight_logs

    def calculate_weekly_changes(self):
        changes = []
        for i in range(1, len(self.weight_logs)):
            prev_weight = self.weight_logs[i - 1]['weight']
            current_weight = self.weight_logs[i]['weight']
            changes.append(current_weight - prev_weight)
        return changes

    def generate_alerts(self, changes, threshold=1.0):
        alerts = []
        for i, change in enumerate(changes):
            if abs(change) > threshold:
                alerts.append(f"Week {i + 2}: Change of {change:.2f} kg")
        return alerts
