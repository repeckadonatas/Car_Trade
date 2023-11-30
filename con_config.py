from configparser import ConfigParser


def connection(filename='credentials.ini', section='postgresql'):
    """
    Function to read configuration parameters from credentials.ini file.
    ConfigParser is used to parse through the credentials.ini values
    and to create connection parameters to use in other functions to
    establish a connection with PostgreSQL database.
    :param filename: Refers to credentials.ini file.
    :param section: Refers to the correct configuration parameters
                    in case there were multiple connection parameters.
    :return: Returns database
    """
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
