#데이터를 긁어와서 엑셀.csv파일로 저장하는 크롤링
import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f) #파일 쓰기
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)


for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1:
            continue  #의미없는 데이터 (빈 공백, 줄바꿈등)는 skip

        data = [column.get_text() for column in columns]
        #print(data)
        writer.writerow(data)
