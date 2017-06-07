import os
import sys
import urllib.request
import datetime
import time
import json
from config import *

def get_request_url(url):
    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE 1]
def getGeoData(address):
    
    base = "https://openapi.naver.com/v1/map/geocode"
    node = ""
    parameters = "?query=%s" % urllib.parse.quote(address)
    url = base + node + parameters
    
    retData = get_request_url(url)
    
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def main():

    jsonResult = getGeoData('서울특별시 종로구 사직로 161 경복궁') 

    if 'result' in jsonResult.keys():
        print('총 검색 결과: ', jsonResult['result']['total'])
        print('검색어: ', jsonResult['result']['userquery'])
        
        for item in jsonResult['result']['items']:
            print('=======================')
            print('주소: ', item['address'])
            print('위도: ', str(item['point']['y']))
            print('경도: ', str(item['point']['x']))

if __name__ == '__main__':
    main()



