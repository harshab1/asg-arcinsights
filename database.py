import sqlalchemy
def database_connection(database_username, database_password, database_ip, database_name):
    return sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(database_username, database_password, database_ip, database_name))
