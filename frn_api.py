#!/usr/bin/python3

import requests
import json
import os

# RECON
# Organization ID
ORG="eab08818-ac20-40a5-a7a6-9792d0501723"
#API Key
APIKEY = os.getenv('FRN_KEY')


#BASE_URL ="https://api.fortirecon.forticloud.com"

BASE_URL ="https://api.fortirecon.forticloud.com"


def do_something(j):
    for h in j:
        print(h["asset"])

headers={'Authorization': APIKEY}
results = requests.get(BASE_URL+"/orgs",headers=headers) #,json=body)
print(results.text)



url=f'{BASE_URL}/easm/{ORG}/assets/domains'
print(url)
headers={'Authorization': APIKEY}
results = requests.get(url,headers=headers) #,json=body)

if (results.ok):
    r = json.loads(results.text)
    pages=int(r["total"]/r["size"]+0.99)
    do_something(r["hits"])
    
    for page in range(2,pages+1):
        params = {'page': page}
        results = requests.get(url,headers=headers,params=params)
        if (results.ok):
            r = json.loads(results.text)
            do_something(r["hits"])
        else:
            print(results.text)