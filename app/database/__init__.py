"""
This module manages a singleton database connection.
It ensures that only one connection is created and reused across the application.
This method is efficient and prevents unnecessary overhead from multiple connections.
"""

_connection = None

def get_connection():
    global _connection
    if _connection is None:
        print("Connecting to database...")
        _connection = "DB connection"  # replace with actual DB connection
    return _connection

def close_connection():
    global _connection
    if _connection is not None:
        print("Closing database connection...")
        _connection = None  # replace with actual DB disconnection logic

