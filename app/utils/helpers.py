# utils/helpers.py

"""
WeightWise Helpers

Utility functions for formatting and calculations.
"""

from datetime import datetime

def format_date(date_str):
    """
    Convert a date string from 'YYYY-MM-DD' to a more readable format.
    
    :param date_str: Date string in 'YYYY-MM-DD' format
    :return: Formatted date string
    """
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date.strftime('%B %d, %Y')
    except ValueError:
        return "Invalid Date"

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: BMI value
    """
    if height <= 0:
        return None
    return round(weight / (height ** 2), 1)
