# Aims of the assignment 
1. To be able to ingest data using an API
2. To be able to load the ingested data into a database of your choice
3. Export the data to a CSV file

# DATA:

TIME_SERIES_DAILY API returns raw (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering 20+ years of historical data. (Link: https://www.alphavantage.co/documentation/#daily)

## API Parameters
❚ Required: function
The time series of your choice. In this case, function=TIME_SERIES_DAILY

❚ Required: symbol
The name of the equity of your choice. For example: symbol=IBM

❚ Optional: outputsize
By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: datatype
By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

❚ Required: apikey
Your API key.