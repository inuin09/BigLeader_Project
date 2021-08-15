#예제에서는 다음을 이용하였지만, 나는 네이버로 도전!!
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=2021%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.select("div>a>img")

for year in range(2015, 2020):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.select("div>a>img")


    for idx, image in enumerate(images):
        image_url = image["src"]
        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year,idx+1),"wb") as f:
            f.write(image_res.content)

        if idx>=4 : #상위 5개 이미지까지만 다운로드
            break