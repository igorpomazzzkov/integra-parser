import requests
from bs4 import BeautifulSoup

res = requests.get('https://xn--90aiim0b.xn--80aa3agllaqi6bg.xn--90ais/schedules?station_from_id=0&station_to_id=0&city_from_id=5&city_to_id=24&date=25.09.2021')

html = BeautifulSoup(res.content)
elements = html.find_all('ul', attrs={'class' : 'sheduleRow'})
for element in elements:
    print(element)