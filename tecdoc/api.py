import requests

base_url = 'http://localhost:8081/api/tecdoc/'

header = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMyIsImlhdCI6MTYzODk1MzQwMSwiZXhwIjoxNjM5NDMzNDAxLCJyb2xlIjoiQURNSU4iLCJjb21wYW55IjoiRkVOT1giLCJ1c2VybmFtZSI6ImFkbWluIiwiY2lkIjoiNTRhZDlhNjkzMDcwNDI2YjlhZWJlMjNkMjZmZjBiMzkiLCJzdGF0dXMiOiJVTkJMT0NLRUQifQ.BuT22m0_W-YguaE9TYNbiAnbQyK4xfViuIXcPfnbmeQ2brS-uSAb9aLVYz4BPDUQQezVtHIJPfrGoyBXUzvQzw'
}


def get_countries(lang: str, provider: int):
    param = {
        'lang': str(lang),
        'provider': str(provider)
    }
    response = requests.get(base_url + 'countries', headers=header, params=param)
    return response.json()


def get_motor_ids(lang: str, provider: int, country: str, manu_id: int):
    param = {
        'lang': str(lang),
        'provider': provider,
        'manuId': manu_id,
        'country': country
    }
    response = requests.get(base_url + 'motors/ids', params=param, headers=header)
    return response.json()