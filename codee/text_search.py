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

df2 = pd.DataFrame(columns=['orig_name', 'orig_city', 'name', 'address', 'latitude', 'longitude', 'no_of_results'])

# Construct search query
df['search_query'] = df['Merchant_Name'].astype(str) + ' ' + df['City']
# search_query = search_query.str.replace(' ', '+')

save_path = 'C:\\Tushar\\notebookk\\new outputs\\29_06\\'

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
            print('No results found for "{}".'.format(row.search_query))
            sleep(random.randint(120, 150))

        elif size_of_result == 20:
            print('Number of results are 20 or more, skipping "{}" for now.'.format(row.search_query))
            sleep(random.randint(120, 150))

        else:

            # Create csv file
            filename = save_path + row.search_query + '.csv'
            # f = open(filename, 'w', encoding='utf-8-sig')

            for i in range(size_of_result):
                name = data['results'][i]['name']
                address = data['results'][i]['formatted_address']
                latitude = data['results'][i]['geometry']['location']['lat']
                longitude = data['results'][i]['geometry']['location']['lng']
                
                df2.loc[i] = [row.Merchant_Name] + [row.City] + [name] + [address] + [str(latitude)] + [str(longitude)] + [str(size_of_result)]
                
                # f.write(row.Merchant_Name + ',' + row.City + ',' + name.replace(',', '') + ',' + address.replace(',', '') + ',' + str(latitude) + ',' + str(longitude) + ',' + str(size_of_result) + '\n')
            
            df2.to_csv(filename, encoding='utf-8-sig', index=False, header=False)
            df2 = df2.iloc[0:0]
            
            # f.close()

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