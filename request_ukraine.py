import requests
import json

API_KEY = '67b2d2a11ee80a10864a77892a1fe300'
response = requests.get(
    "https://a.liveuamap.com/api?a=mpts&resid=0&time=now&key=gt3er6nvbn29mvy7der3amkx63uc4udd&geojson=true"

)
print(response.status_code)
ukraine_info = response.json()


def russian() -> json:
    ukraine_info_list = ukraine_info['features']

    russian_obtained = {'type': 'FeatureCollection', 'features': []}
    for i in ukraine_info_list:
        if i['geometry']['type'] == 'Polygon':
            russian_obtained['features'].append(i)

    return russian_obtained


russian()
