import requests
from bs4 import BeautifulSoup # 사이트 정보 크롤링 

def get_exchange_rate(target1, target2):
    # 헤더를 통해 일반적인 브라우저를 이용하여 접속한 것처럼 보이게 한다 
    # (헤더 없이 접속하면 로봇으로 간주하여 사이트에서 정보를 주지않음) 
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    } 
    #request 라이브러리를 이용하여 사이트에 접속하여 응답값 가져오기
    response = requests.get("http://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)

    #html로 가져오기
    content = BeautifulSoup(response.content, 'html.parser')
    
    #box = content.find("div", {'data-test': 'instrument-header-details'})

    # 마지막 환율 정보 찾기
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)

    #print(content.find_all('span'))


get_exchange_rate('usd', 'krw')