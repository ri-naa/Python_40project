import requests

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'  # 도로명주소
road_type2 = 'PARCEL'  # 지번주소
address = '&address='
keys = '&key='
primary_key = '8F31226A-10D6-3520-B17A-1EA18A2EF1F7'


def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x,y
    else:
        x = 0
        y = 0
        return x,y


x, y = request_geo("서울특별시 서대문구 이화여대길 52 (대현동, 이화여자대학교)")

print(f'x값: {x}')
print(f'y값: {y}')