import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%B0%B0%EC%B6%94&channel=user&component=194176&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    # #애플 제품은 제외 (예제에서만 적용 가능)
    # if "Apple" in name:
    #     print("애플 제품 제외")
    #     continue

    #광고 제품은 제외하자
    ad_badge = item.find("span", attrs={"class":"ad-badge-product"})
    if ad_badge:
        print("광고 상품 제외")
        continue


    name  = item.find("div", attrs={"class":"name"}).get_text() #제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격

    #리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})#평점

    if rate:
        rate = rate.get_text()
    else:
        #평점 없는 상품 제외
        print("평점 없는 상품 제외")
        continue

    rate_total = item.find("span", attrs={"class":"rating-total-count"}) #리뷰 수


    if rate_total:
        rate_total = rate_total.get_text()  #이 상태로 리뷰수를 뽑아내면 (26)이런식으로 나옴. 괄호를 없애줘야한다.
        rate_total = rate_total[1:-1]  #괄호 제거
        #print("리뷰 수 : ", rate_total)
    else:
        print("리뷰 없는 상품 제외")
        continue

    if float(rate) >= 4.5 and int(rate_total) >=100:
        print(name, price, rate, rate_total)

