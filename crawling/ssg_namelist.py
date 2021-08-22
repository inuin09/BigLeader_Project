import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd


#페이지 자동으로 넘기기
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

item_pd = pd.DataFrame()  #전체를 저장할 데이터 프레임

name_list = [] #제품명 넣는 리스트

for i in range(1,8):
    #각자 맡은 농작물로 검색해서 하세요 
    url = "http://emart.ssg.com/disp/category.ssg?dispCtgId=6000096189&page={}".format(i)

    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    name_list = soup.select('a.clickable>em')

    #두개의 리스트 먼저 데이터프레임으로 합치고, 마지막 평점 리스트 합쳐주기
    item_pd = pd.DataFrame(name_list)



# #column명 정리해주고, csv파일로 저장
item_pd.columns=['제품명']
item_pd.to_csv("./이마트양파1_page_상품명.csv",encoding="utf-8-sig")


