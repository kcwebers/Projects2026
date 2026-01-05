import requests
import json
import pandas as pd

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

# if response.status_code == 200:
#     data = response.json()  # Extract JSON content
#     scryfall_data = json.dumps(data, indent=4)  # Serialize the extracted data
#     print(scryfall_data)

# with open("card_data.json", "w") as card_data_json:
#     json.dump(card_data, card_data_json, indent=4)




# load json data and convert to excel spreadsheet using pandas
data = response.json()
# Scryfall's API returns cards in a 'data' key
cards = data['data']

# Convert to DataFrame
df = pd.DataFrame(cards)

# You might want to select specific columns since Scryfall returns A LOT of data
# Here are some commonly useful ones:
columns_to_keep = [
    'name', 'collector_number', 'rarity'
]

# Filter to just those columns (only keeping ones that exist)
df_filtered = df[[col for col in columns_to_keep if col in df.columns]]

# Export to Excel
df_filtered.to_excel('my_collection.xlsx', index=False)







# unused trail / error

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
