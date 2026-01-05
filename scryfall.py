import requests
import json

# headers = {
#     'user-agent': 'scryfall_data_pull_personal/1.0',
#     'accept': '*/*',
# }

#------------------------------------------------------------
#    Endpoint cards/collection (sample)
#------------------------------------------------------------
# url = 'https://api.scryfall.com/cards/collection'
# params = {
#     "identifiers": [
#         {
#         "id": "683a5707-cddb-494d-9b41-51b4584ded69"
#         },
#         {
#         "name": "Ancient Tomb"
#         },
#         {
#         "set": "mrd",
#         "collector_number": "150"
#         }
#     ]
# }

# api call
# NOTE: json for params, POST not GET response
# response = requests.post(url, json=params)
# print(response.json())

#------------------------------------------------------------
#    Endpoint cards/search 
#------------------------------------------------------------

url = 'https://api.scryfall.com/cards/search'

# NOTE: params need specific spacing w/i strings for key value pairs
params = {
    "q" : "set:tla"
}

response = requests.get(url, params=params)
print(response.json())


# pull data from response and dump it into file for use in spreadsheet ^.^

if response.status_code == 200:
    data = response.json()  # Extract JSON content
    json_data = json.dumps(data, indent=4)  # Serialize the extracted data
    print(json_data)

with open("card_data.json", "w") as card_data_json:
    json.dump(json_data, card_data_json, indent=4)