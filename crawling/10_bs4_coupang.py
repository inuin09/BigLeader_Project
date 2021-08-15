import requests
from bs4 import BeautifulSoup
import re

#페이지 자동으로 넘기기
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

for i in range(1, 6): #1페이지부터 5페이지 까지 다섯개의 페이지만 크롤링
    print("페이지 : ",i)

    url = "https://www.coupang.com/np/search?q=%EB%B0%B0%EC%B6%94&channel=user&component=194176&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        #광고 제품은 제외하자
        ad_badge = item.find("span", attrs={"class":"ad-badge-product"})
        if ad_badge:
            continue


        name  = item.find("div", attrs={"class":"name"}).get_text() #제품명
        price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격

        #리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"})#평점

        if rate:
            rate = rate.get_text()
        else:
            #평점 없는 상품 제외
            continue

        rate_total = item.find("span", attrs={"class":"rating-total-count"}) #리뷰 수


        if rate_total:
            rate_total = rate_total.get_text()[1:-1]  #이 상태로 리뷰수를 뽑아내면 (26)이런식으로 나옴. 괄호를 없애줘야한다.
        else:
            #리뷰없는 상품 제외
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_total) >=100:
            #print(name, price, rate, rate_total)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}, 리뷰 {rate_total}개")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("---------------------------------------------------------------")

    print("\n")

