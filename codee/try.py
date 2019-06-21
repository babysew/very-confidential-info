# import pandas as pd
import requests
import googlemaps
import pprint as pp
# import time

proxies = {
    'http': 'http://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080',
    'https': 'http://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080'
    # 'https': 'http://user:pass@10.10.1.0:3128',
}

# Create the session and set the proxies.
s = requests.Session()
s.proxies = proxies



# df = pd.read_csv("short_merchant.csv", usecols=[0, 1])

# search_query = df.Merchant_Name + " " + df.City

# API_KEY = "AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA"

# gmaps = googlemaps.Client(key = API_KEY)

r = s.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=big+bazaar+new+delhi&key=AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA', verify=False)

b = r.json()

pp.pprint(b)

# for search in search_query:
    # filename = search + ".csv"
    # f = open(filename, "w")
    
    # search_result = gmaps.places(query=search)


# filename = "big bazaar new delhi.csv"
# f = open(filename, "w")

# search_result = gmaps.places(query="big bazaar new delhi")  
# r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=big+bazaar+new+delhi&key=AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA') 
# r.status_code() 

# pp.pprint(search_result)

# size_of_json = len(results)

# i = 0

'''
for item in b:
    row = [
        item["results"][0]["formatted_address"], 
        item["results"][0]["geometry"]["location"]["lat"], 
        item["results"][0]["geometry"]["location"]["lng"],
        item["results"][0]["name"]
    ]
    address = row[0]
    latitude = row[1]
    longitude = row[2]
    name = row[3]

    f.write(name + "," + address.replace(",", "|") + "," + latitude + "," + longitude + "\n")
    # f.write(df.Merchant_Name + "," + df.City + "," + name + "," + address.replace(",", "|") + "," + latitude + "," + longitude + "\n")

    # i += 1
        
f.close()
'''

# time.sleep(2)

    # search_result = gmaps.places(page_token=search_result['next_page_token'])