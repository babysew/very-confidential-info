import pandas as pd
# import googlemaps
import requests
# import csv
# import pprint as pp
from time import sleep
import random


http_proxy = 'http://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080'
https_proxy = 'https://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080'

proxies = {
    'http'  : http_proxy,
    'https'  : https_proxy
}

API_KEY = 'AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA' # AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA

PLACES_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

# Make dataframe
df = pd.read_csv('short_merchant.csv', usecols=[0, 1])

# Construct search query
df['search_query'] = df['Merchant_Name'].astype(str) + ' ' + df['City']
# search_query = search_query.str.replace(' ', '+')

random.seed()

for row in df.itertuples():
    search_req = 'query={}&key={}'.format(row.search_query, API_KEY)
    request = PLACES_URL + search_req

    # Place request and store data in 'data'
    result = requests.get(request, proxies=proxies, verify=False)
    data = result.json()

    status = data['status']

    if status == 'OK':
        size_of_result = len(data['results'])
        
        if size_of_result == 0:
            print('No results found for {}.'.format(row.search_query))

        else:

            # Create csv file
            filename = row.search_query + '.csv'
            f = open(filename, 'w', encoding='utf-8')

            size_of_json = len(data['results'])

            for i in range(size_of_json):
                name = data['results'][i]['name']
                address = data['results'][i]['formatted_address']
                latitude = data['results'][i]['geometry']['location']['lat']
                longitude = data['results'][i]['geometry']['location']['lng']

                f.write(row.Merchant_Name + ',' + row.City + ',' + name.replace(',', '') + ',' + address.replace(',', '') + ',' + str(latitude) + ',' + str(longitude) + ',' + str(size_of_result) + '\n')

            f.close()

            print('File successfully saved for "{}".'.format(row.search_query))

            sleep(random.randint(120, 150))

    elif status == 'ZERO_RESULTS':
        print('Zero results for "{}". Moving on..'.format(row.search_query))
        sleep(random.randint(120, 150))
    elif status == 'OVER_QUERY_LIMIT':
        print('Hit query limit! Try after a while. Could not complete "{}".'.format(row.search_query))
        break
    else:
        print(status)
        print('^ Status not okay, try again. Failed to complete "{}".'.format(row.search_query))
        break