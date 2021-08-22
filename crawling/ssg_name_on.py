from os import sep
import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import time


#페이지 자동으로 넘기기
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

item_pd = pd.DataFrame()  #전체를 저장할 데이터 프레임

name_list = [] #제품명 넣는 리스트

for i in range(1,8):
    #각자 맡은 농작물로 검색해서 하세요 
    url = "http://emart.ssg.com/disp/category.ssg?dispCtgId=6000096189&page={}".format(i)

    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("cunit_t232")})

    for item in items:
        #내용긁어오기
        name = item.find("div", attrs={"class":"title"}).get_text() #제품명

        name_list.append(name)   

    with open("양파_이마트_이름.csv", 'w', encoding='utf-8-sig') as file:
         writer = csv.writer(file)
         writer.writerow(name_list)



