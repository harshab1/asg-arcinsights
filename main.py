import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&apikey=OPTQ1LNJ9RQTYTKM'
r = requests.get(url)
data = r.json()

print('Keys:', data.keys())

print('Meta Data:', data['Meta Data'])

df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient = "index")
df = df.reset_index(level=0)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

print(df.head())