import time
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://heinemann9.github.io')
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.contents)

degree = soup.select(
    'div > div > div > div > h4'
)
meta = soup.select(
    'div > div > div > div > h5'
)
time_ = soup.select(
    'div > div > div > div > div'
)

school = []
for item in zip(degree, meta, time_):
    school.append(
        {
            'degree' : item[0].text,
            'meta' : item[1].text,
            'time' : item[2].text
        }
    )

data = pd.DataFrame(school)
print(data)
data.to_csv('school.csv', encoding='utf-8-sig')

driver.quit()