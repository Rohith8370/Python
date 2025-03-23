import requests

def get_post:
    url = 'https://fakestoreapi.com/products/1'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Parse JSON response
    else:
        print('Failed to retrieve data:', response.status_code)
        return None