import requests

def get_card_data():
    url = 'https://api.scryfall.com/cards/collection'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            card_data = response.json()
            print(card_data)
            return card_data
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    card_data = get_card_data()

    if card_data:
        print('First Post Title:', card_data[0]['title'])
        print('First Post Body:', card_data[0]['body'])
    else:
        print('Failed to fetch card_data from API.')

if __name__ == '__main__':
    main()