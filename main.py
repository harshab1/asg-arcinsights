import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&apikey=$api_key&outputsize=full'
r = requests.get(url)
data = r.json()

print('--------------- \n Json Keys \n---------------')

print(data.keys())

print('--------------- \n Meta Data \n---------------')
print(data['Meta Data'])

# print(data['Time Series (Daily)'])

print('--------------- \n Converting the Dictionary to Data Frame \n---------------')
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient = "index")
df = df.reset_index(level=0)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

print('--------------- \n Data Frame Head\n---------------')
print(df.head())


print('--------------- \n Importing dataframe into MySQL\n---------------')

import sqlalchemy

print('--------------- \n Connecting to DB\n---------------')
database_username = input('Enter DB Username: ')
database_password = input('Enter DB password: ')
database_ip       = "127.0.0.1"
database_name     = "stocks_data"
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
df.to_sql(con=database_connection, name='reliance_data', if_exists='replace')
print('--------------- \n Import Successful\n---------------')


print('--------------- \n Printing Database\n---------------')
sql_query = sqlalchemy.text("SELECT * FROM reliance_data")
result = database_connection.execute(sql_query)
result_as_list = result.fetchall()
print('------------------')
print('Table: Reliance Data')
print('------------------')
for row in result_as_list:
    print(row)


print('--------------- \n Exporting Data to CSV file\n---------------')
df.to_csv('reliance-data.csv')