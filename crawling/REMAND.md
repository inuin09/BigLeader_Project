crawling code는 인터넷, 유튜브 등의 자료들을 참고하고 내가 써야할 상황에 맞게끔 고쳐서 재작성한 code이다.<br>

## review.py
review.py 코드는 쿠팡에서 각 상품의 상품평에 들어가서, 리뷰일자만 가져올 수 있는 크롤러이다.<br>
url이 조금 특이한게, 본 사이트에서 리뷰일자를 가져오는 것이 잘 안되서(자동 스크롤 다운 함수를 사용해야 상품평으로 갈 수 있는데 잘 안되서 지금은 포기했다.(시간관계상)) 리뷰들만 모아놓은 url을 따로 따와서 거기서 page 수만 바꿔가며 리뷰일자를 가져오는 조금 무식한 방법을 사용했다.<br>
나는 이 코드를 이용하여, 쿠팡의 마늘, 무, 양파, 배추의 리뷰일자를 가져왔다.<br>
Ps. 쿠팡의 상품평은 몇개가 쌓여있든 총 1,000개만 보여준다! 7천개가 넘는 상품평이 있길래 시도했지만 무조건 1,000개만 뽑히더라...내가 크롤러 실력이 많이 부족하구나 생각했는데 알고보니 상품평이 몇개든 쿠팡에서 사용자에게 보여주는 총 상품평은  1,000개였다...그래 일반인(?)들이 7천개의 상품평을 다 읽지는 않으니까...^_^<br>
## namelist.py
namelist.py 코드는 쿠팡에서 각 상품의 상품명만을 뽑아내는 코드이다.<br>
해당 상품페이지의 url을 따와서 page={}로 만든후 for문을 이용하여 자동으로 page가 넘어가도록 했다.<br>
10페이지 이상을 넘어갈때도 편했다는 점이 있지만, 페이지 수도 알고 있었어야 한다는 단점아닌 단점이 있다. (이 문제에 대해서는 셀레니움으로 해결할 수 있다라는 것을 알지만 셀레니움 아직 너무 어렵다)<br>
그 제품의 총 갯수를 알아보기 위해 제품명을 뽑아 내었고 결과는 아주 좋았으며 바로 count할 수 있었지만, 제품들 속에 원하지 않는 제품도 있는 경우가 있어 데이터를 전처리 한 후에 count하기로 하였다!