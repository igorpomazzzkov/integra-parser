import api
import dao


lang = 'RU'
provider = 0
cid = '54ad9a693070426b9aebe23d26ff0b39'


brands = dao.get_brands_article_with_tecdoc_id()
countries = api.get_countries(lang, provider)['data']['array']
for country in countries:
    country_code = country['countryCode']

for brand in brands:
    for country in countries:
        country_code = country['countryCode']
        brand_id, name, tecdoc_id = brand
        print(country_code, lang, tecdoc_id, name)
        motor_ids = api.get_motor_ids(lang, provider, country_code, tecdoc_id)['data']['array']
        for motor_id in motor_ids:
            dao.save_motor_id(brand_id, motor_id['motorId'])


