# data/__init__.py

"""
WeightWise Data Module

Initialize and manage database connections and setup.
"""

from .database import initialize_database, get_connection

def setup_data():
    initialize_database()

def get_db_connection():
    return get_connection()
