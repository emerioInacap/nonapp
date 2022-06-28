import cx_Oracle
import config

class BaseNona:
    #connection = None
    try:
        connection = cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding)

        # show the version of the Oracle Database
        print('\nConectado a Oracle',connection.version)

       


    except cx_Oracle.Error as error:
        print(error)
    """ 
    finally:
        # release the connection
        if connection:
            connection.close()
            """


#BaseNona();

