import requests
import json

global api_base_url
global api_key
global headers
api_base_url = "https://servicedesk.consys.it/api/v2"
api_key = "key 4:J52GGYQH2RNDJWPPWCH3RYPAG"
headers = {'Authorization': api_key}

def get_pages_number(api_request,count,extra_params=""):
    api_url = api_base_url + api_request + "?count=" + str(count) + extra_params
    response = requests.get(api_url, headers=headers)
    #print(response.status_code)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)

    try:
        total_pages = data["meta"]["pagination"]["total_pages"]
    except:
        total_pages = 1
    #print("number of pages:",total_pages)
    return total_pages

def get_json_response_by_page(api_request,count,page,extra_params=""):
    api_url = api_base_url + api_request + "?count=" + str(count) + "&page=" + str(page) + extra_params
    response = requests.get(api_url, headers=headers)
    #print(response.status_code)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)
    return data

