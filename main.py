import pandas as pd
import get_data
import sqlalchemy
import database

base_url = 'https://www.alphavantage.co/query'
params = dict()
params["apikey"] = input("Enter your api key: ").upper()
params["outputsize"] = input("Enter the output size [Options: full, compact]: ").lower()
params["function"] = input("Enter the time series of your choice [Options: TIME_SERIES_DAILY, TIME_SERIES_INTRADAY_EXTENDED]: ").upper()
query_symbol = input("Enter the stock symbol [Example: IBM]: ").upper()
query_stock_market_boolean = input("Whether the stock you picked belonged to US market [Options: Yes, No]: ")
if query_stock_market_boolean.upper() == "NO":
    query_stock_market = input("Pick your stock market [options: LON, TRT, TRV, DEX, BSE, SHH, SHZ]: ")
    params["symbol"] = '.'.join([query_symbol, query_stock_market])
elif query_stock_market_boolean.upper() == "YES":
    params["symbol"] = query_symbol

response = get_data.get_data(base_url, params)

print(response.url)
data = response.json()

# keys of the json data 
print(data.keys())

# meta data 
print(data['Meta Data'])

# print(data['Time Series (Daily)'])

# Converting the Dictionary to Data Frame 
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient = "index")
df = df.reset_index(level=0)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
print(df.head())


# Importing dataframe into MySQL

# Connecting to DB
database_username = input('Enter DB Username: ')
database_password = input('Enter DB password: ')
database_ip       = "127.0.0.1"
database_name     = "stocks_data"
table_name = input("Enter the table to be created in the database: ")

database_connection = database.database_connection(database_username, database_password, database_ip, database_name)
df.to_sql(con=database_connection, name=table_name, if_exists='replace')


# # Printing Database
# sql_query = sqlalchemy.text("SELECT * FROM table_name")
# result = database_connection.execute(sql_query)
# result_as_list = result.fetchmany(10)
# print('------------------')
# print('Table: Reliance Data')
# print('------------------')
# for row in result_as_list:
#     print(row)


df.to_csv('data.csv')