#%% 공공데이터 API를 이용하여 제공받은 JSON데이터를 CSV파일로 저장하기
from urllib.parse import unquote, urlencode
import requests
import json

url = 'https://apis.data.go.kr/B552061/jaywalking/getRestJaywalking'

queryString = '?' + urlencode(
    {
    'ServiceKey' : unquote('*'), # 인증키 보안상 깃허브에 올릴때 * 로 표현하였음
    'searchYearCd' : '2017',
    'siDo' : '11',
    'guGun' : '680',
    'type' : 'json',
    'numOfRows' : '10',
    'pageNo' : '1' 
    }
   )

queryURL = url + queryString

response = requests.get(queryURL, verify = False)

#--------------------------------------------------------------
# 공공데이터 포털로 부터 제공받은 JSON 데이터에서 원하는 값들만 출력
jsonObj = json.loads(response.text)

# 원하는 정보 가져오기
jsonItems = jsonObj.get('items')
jsonitem = jsonItems.get('item')


# 반복문 첫번쨰 - CSV파일 저장하기 X
for item in jsonitem:
    print(f'{item.get("sido_sgg_nm")},{item.get("spot_nm")}')


#--------------------------------------------------------------
# 공공데이터에서 API를 이용하여 제공받은 JSON 데이터를 CSV파일로 저장하기

f = open('apijson.csv', 'w')
f.write('지역구,사고지역' + '\n')

# 파일에 쓰기
for item in jsonitem:
    f.write(item.get('sido_sgg_nm') + ',' + item.get('spot_nm') + '\n')

f.close()
    