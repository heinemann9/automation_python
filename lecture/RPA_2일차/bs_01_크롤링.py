import urllib.request #파이썬 모듈(웹스크랩핑)
from bs4 import BeautifulSoup
import time #딜레이타임

count = 1

for page_num in range(1,3):
    url = f"https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={page_num}&cnt=1000&SortOrder=1"
    html = urllib.request.urlopen(url).read() #url의 코드를 가져와서 html에 삽입. 내용이 바이트(byte)형식으로 저장
    content = BeautifulSoup(html, "html.parser")

    content_a = content.find_all(class_="ss_book_box") 
                #웹페이지에 class찾을 때 class는 예약어기 때문에 _를 붙여서 사용

    #print(content_a)
    
    for title in content_a:
        title_img = title.find("img", class_="front_cover")
        title_text = title.find("a", class_="bo3")
        
        print(count, "책제목 :",title_text.text)
        print("이미지주소 :",title_img.get("src"))
        print("링크 :",title_text.attrs["href"])
        
        img_src = title_img.get("src")

        #이미지 파일명을 만들어서 다운로드
        img_filename = f"aladin_img_{count}.jpg"
        urllib.request.urlretrieve(img_src, img_filename) #이미지 다운로드

        count += 1

    #time.sleep(3) #시간 지연
        


