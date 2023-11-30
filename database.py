import psycopg2
from con_config import connection
import sql_commands


def connect():
    """
    Initiating a connection to PostgreSQL database.
    Testing connection with the database.
    :return: If successful, returns database version
        and connection parameters.
        Upon failure to connect, returns an error.
        Uses connection parameters set in con_config.py file.

    """

    conn = None
    try:
        # Reading connection parameters
        params = connection()

        # Connecting to database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        print('\t')
        print('Connection successful!')

        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print('PostgreSQL version:', db_version, '\n')

        print('PostgreSQL connection properties:', '\n', conn.get_dsn_parameters())

    except (Exception, psycopg2.Error) as error:
        print('Error while connecting to PostgreSQL:', error)

    # Closing the connection to db
    if conn is not None:
        conn.close()
        print('\t')
        print('Connection closed.')


def create_table():
    """
    Creates a table in PostgreSQL database.
    For connection, uses connection parameters set in con_config.py file.
    To create a table uses SQL statement from sql_commands.py file.
    """

    conn = None
    try:
        # Reading connection parameters
        params = connection()

        # Connecting to database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Creating a table if it does not exist
        table_sql = sql_commands.new_table

        cursor.execute(table_sql)
        conn.commit()
        print('\t')
        print('Table was created successfully.')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # Closing the connection to db
    if conn is not None:
        conn.close()
        cursor.close()
        print('\t')
        print('Connection closed.')


def check_created():
    """
    Checks tables existing in PostgreSQL database.
    For connection, uses connection parameters set in con_config.py file.
    :return: Returns a list of tables.
    """

    conn = None
    try:
        # Reading connection parameters
        params = connection()

        # Connecting to database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Checking what tables are in db
        cursor.execute("SELECT relname FROM pg_class WHERE relkind='r' AND relname !~ '^(pg_|sql_)';")
        print('\t')
        print('Tables in the database:')
        print(cursor.fetchall())

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # Closing the connection to db
    if conn is not None:
        conn.close()
        cursor.close()
        print('\t')
        print('Connection closed.')


def populate_table():
    """
    Populates a table in PostgreSQL database.
    For connection, uses connection parameters set in con_config.py file.
    Before populating a table, truncates it if it was previously populated.
    To populate a table first opens a CSV file in memory and uses
    copy_expert() PostgreSQL function in combination with
    COPY SQL statement from sql_commands.py file.
    """

    conn = None
    try:
        # Reading connection parameters
        params = connection()

        # Connecting to database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Truncating table before populating it again to avoid duplication
        truncate = """TRUNCATE TABLE car_data;"""
        cursor.execute(truncate)
        conn.commit()
        print('\t')
        print('Table truncated!')

        # Populating a table with CSV data
        open_csv = open('csv/car_data_1NF.csv')
        load_csv = sql_commands.load_csv

        cursor.copy_expert(sql=load_csv, file=open_csv)
        conn.commit()
        print('\t')
        print('Copying CSV data!')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # Closing the connection to db
    if conn is not None:
        conn.close()
        cursor.close()
        print('\t')
        print('Connection closed.')


def if_populated():
    """
    Checks the table to see if it was populated with data correctly.
    For connection, uses connection parameters set in con_config.py file.
    :return: Returns the first row of the table.
    """

    conn = None
    try:
        # Reading connection parameters
        params = connection()

        # Connecting to database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Checking if the table is populated with csv data as intended
        table_check = sql_commands.table_check

        cursor.execute(table_check)
        records = cursor.fetchmany(size=cursor.arraysize)
        print('\t')
        print(records)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # Closing the connection to db
    if conn is not None:
        conn.close()
        cursor.close()
        print('\t')
        print('Connection closed.')
