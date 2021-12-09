import api
import dao


lang = 'RU'
provider = 0
cid = '54ad9a693070426b9aebe23d26ff0b39'


def save_brand_to_file(brand: str):
    file = open('failed.txt', 'w')
    file.write(brand + '\n')
    file.close()


brands = dao.get_brands_article_with_tecdoc_id()
countries = api.get_countries(lang, provider)['data']['array']
brand_not_founded = set()
for country in countries:
    country_code = country['countryCode']

for brand in brands:
    brand_id, name, tecdoc_id = brand
    motor_ids_response = api.get_motor_ids(lang, provider, "RU", tecdoc_id)
    print(name, tecdoc_id)
    if motor_ids_response.status_code == 200:
        motor_ids = motor_ids_response.json()['data']['array']
        for motor_id in motor_ids:
            print('INSERTED ROW ', brand_id, brand, tecdoc_id, motor_id)
            dao.save_motor_id(brand_id, motor_id['motorId'])
    else:
        brand_not_founded.add(name)
        continue

for brand_err in brand_not_founded:
    save_brand_to_file(brand_err)
