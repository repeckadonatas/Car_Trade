import database

"""
To load cleaned CSV data to PostgreSQL, run this file
"""

database.connect()
database.create_table()
database.check_created()
database.populate_table()
database.if_populated()
