import urllib.request
from bs4 import BeautifulSoup
import time
import os

page_num = 1
count = 0
for page in range(1, 2):
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={page_num}&cnt=1000&SortOrder=1"
    html = urllib.request.urlopen(url).read()
    content = BeautifulSoup(html, "html.parser")

# print(content.title)
# print(content.title.string)
# print(content.title.text)

#print(content.strong)
#print(content.p)
#print(content.a)

#print(content.find_all('a'))
#print(content.find('a', 'bo3'))
# content_a = content.find_all('h3')
# for title in content_a:
#     a_tag = title.find("a")
#     if a_tag:
#         print(title.text)
#         print(title.a.get("href"))
# print(content.get_text())

    # content_a = content.find_all("a", class_="bo3") # class => class_
    # for title in content_a:
    #     count+=1
    #     title_text = title.get_text()
    #     title_link = title.attrs["href"]
    #     print( f"{count}" + ". 제목 : " + title_text + ", 링크 : " + title_link)
    
    content_a = content.find_all(class_="ss_book_box") # class => class_
    # print(content_a)
    for title in content_a:
        count += 1
        title_img = title.find("img", class_="front_cover")
        title_text = title.find("a", class_="bo3")
        title_link = title_text.attrs["href"]
        img_src = title_img.get("src")
        # print(title_img.attrs["src"], title_img.get("src"))
        print( f"{count}" + ". 제목 : " + title_text.text + ", 링크 : " + title_link + ", img link : " + img_src)

        img_fileName = f"aladin_img_{count}.jpg"
        urllib.request.urlretrieve(img_src, img_fileName)
    time.sleep(1)

# time.sleep(30)

# os.remove('*.jpg')
# print(len(content_a))
