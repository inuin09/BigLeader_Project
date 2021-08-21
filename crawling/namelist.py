import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd


#페이지 자동으로 넘기기
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}


item_pd = pd.DataFrame()  #전체를 저장할 데이터 프레임

name_list = [] #제품명 넣는 리스트

for i in range(1, 16):

    #각자 맡은 농작물로 검색해서 하세요 
    url = "https://www.coupang.com/np/categories/501640?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page={}&channel=user&fromComponent=Y&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=501540&rating=0".format(i) 


    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("dl", attrs={"class":re.compile("baby-product-wrap")})

    for item in items:
        
        #내용긁어오기
        name = item.find("div", attrs={"class":"name"}).get_text() #제품명


        #리스트에 각각 긁어온 내용 넣기
        name_list.append(name)  


        #두개의 리스트 먼저 데이터프레임으로 합치고, 마지막 평점 리스트 합쳐주기
        item_pd = pd.DataFrame(name_list)


#column명 정리해주고, csv파일로 저장
item_pd.columns=['제품명']
item_pd.to_csv("./깐마늘뽑기.csv",encoding="utf-8-sig")


