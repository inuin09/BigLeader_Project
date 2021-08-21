from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

driver = webdriver.Chrome()

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

item_pd = pd.DataFrame()
day = []

for i in range(1, 201):
    url = "https://www.coupang.com/vp/product/reviews?productId=1496018182&page={}&size=5&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=3&ratingSummary=true".format(i)
    driver.get(url)
    driver.maximize_window()

    html = driver.page_source #페이지의 전체 html source를 가져옴
    res = BeautifulSoup(html, "lxml") 

    time.sleep(5)
    review_day = res.find_all("div",attrs={"class":"sdp-review__article__list__info__product-info__reg-date"})
    time.sleep(3)
    day.append(review_day)
    time.sleep(3)


    with open("깐마늘.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(day)

            