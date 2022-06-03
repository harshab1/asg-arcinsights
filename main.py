import requests
import pandas as pd
import getpass

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&apikey=$stocks_apikey'
r = requests.get(url)
data = r.json()

print('Keys:', data.keys())

print('Meta Data:', data['Meta Data'])

df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient = "index")
df = df.reset_index(level=0)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

print(df.head())

# Import dataframe into MySQL
import sqlalchemy

database_username = input('Enter DB Username')
database_password = input('Enter DB password')
database_ip       = "127.0.0.1"
database_name     = "stock_data"
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
df.to_sql(con=database_connection, name='reliance_data', if_exists='replace')


sql_query = sqlalchemy.text("SELECT * FROM reliance_data")
result = database_connection.execute(sql_query)
result_as_list = result.fetchall()
print('------------------')
print('Table: Reliance Data')
print('------------------')
for row in result_as_list:
    print(row)
