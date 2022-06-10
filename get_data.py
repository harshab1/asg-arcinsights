import requests
import urllib.request as urllib2
def get_data(base_url, params):
    response =  requests.get(base_url, params = params)
    print(response.url)
    return response
