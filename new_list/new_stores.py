import pandas as pd
import requests
from time import sleep
import random


http_proxy = 'http://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080'
https_proxy = 'https://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080'

proxies = {
    'http'  : http_proxy,
    'https'  : https_proxy
}

API_KEY = 'AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA' # AIzaSyAO6e32mq3LQaOY6T323x_AFUoSEwHn2hA

GEO_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

df = pd.read_csv('new_stores1.csv', usecols=[6])
df2 = pd.DataFrame(columns=['Address', 'Latitude', 'Longitude'])

for row in df.itertuples():
    search_req = 'address={}&key={}'.format(row.Store_Address, API_KEY)
    request = GEO_URL + search_req

    # Place request and store data in 'data'
    result = requests.get(request, proxies=proxies, verify=False)
    data = result.json()

    status = data['status']

    if status == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        
        # df2.loc[i] = [row.Store_Address] + [latitude] + [longitude]
        df2 = df2.append({'Address' : row.Store_Address , 'Latitude' : latitude, 'Longitude' : longitude} , ignore_index=True)

        print('Result successfully saved for "{}".'.format(row.Store_Address))

        sleep(random.randint(120, 150))

    elif status == 'ZERO_RESULTS':
        print('Zero results for "{}". Moving on..'.format(row.Store_Address))
        sleep(random.randint(120, 150))
    else:
        print(status)
        print('^ Status not okay, try again. Failed to complete "{}".'.format(row.Store_Address))
        break

df2.to_csv('output.csv', encoding='utf-8-sig', index=False, header=False)