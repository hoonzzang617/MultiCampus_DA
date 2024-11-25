import csv
import pymysql

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://datalab.naver.com/"
trend_ranking = requests.get(url)
soup = BeautifulSoup(trend_ranking.text, "html.parser")

# trends_el = soup.select('#content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div:nth-child(9) span.title')
days_el = soup.select('#content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel  div.keyword_rank')

shopping_trends_list =[]
for day_el in days_el:
    #content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div:nth-child(10) > div > strong > span
    day = day_el.select_one('strong.rank_title > span')
    # print(day.text)
    #content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div:nth-child(10) > div > div > ul > li:nth-child(1)
    items = day_el.select('ul.rank_list > li span.title')
    # print(items.text)
    day_list = []
    for i,item in enumerate(items):
        # print(i+1,item.text)
        day_list.append(item.text)
    day_list.insert(0, day.text)
    # print(day_list)
    shopping_trends_list.append(day_list)

# df = pd.DataFrame(shopping_trends_list, columns=['Day', '1', '2', '3','4','5','6','7','8','9','10'])
# df = df.set_index('Day')
# df = df.T
# df.index.name = 'Rank'
# df.to_csv('shopping_trends_list.csv', index=True, encoding='utf-8-sig')
df = pd.DataFrame(shopping_trends_list, columns=['Day', '1', '2', '3','4','5','6','7','8','9','10'])
df.to_csv('shopping_trends_list.csv', index=False, encoding='utf-8-sig')

#########################################################################################


config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'my_db'
}

# conn = pymysql.connect(**config)

# cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS trend_item_list (
#             rank INT PRIMARY KEY,
#             title VARCHAR(255),
#             author VARCHAR(255),
#             genre VARCHAR(255),
#             price DECIMAL(10,2)
#         )
#                ''')

# with open('shopping_trends_list.csv', 'r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader) # Skip header row
#     for row in  csv_reader:

df = pd.read_csv('shopping_trends_list.csv', encoding='utf-8-sig')

conn = pymysql.connect(**config)
cursor = conn.cursor()

# 테이블 생성 쿼리 수정
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trend_item_list (
        Day VARCHAR(20) PRIMARY KEY,
        Rank1 VARCHAR(100),
        Rank2 VARCHAR(100),
        Rank3 VARCHAR(100),
        Rank4 VARCHAR(100),
        Rank5 VARCHAR(100),
        Rank6 VARCHAR(100),
        Rank7 VARCHAR(100),
        Rank8 VARCHAR(100),
        Rank9 VARCHAR(100),
        Rank10 VARCHAR(100)
    )
''')

# 데이터 삽입
for i, row in df.iterrows():
    cursor.execute('''
        INSERT INTO trend_item_list (Day, Rank1, Rank2, Rank3, Rank4, Rank5, Rank6, Rank7, Rank8, Rank9, Rank10)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        Rank1=VALUES(Rank1), Rank2=VALUES(Rank2), Rank3=VALUES(Rank3), Rank4=VALUES(Rank4), Rank5=VALUES(Rank5),
        Rank6=VALUES(Rank6), Rank7=VALUES(Rank7), Rank8=VALUES(Rank8), Rank9=VALUES(Rank9), Rank10=VALUES(Rank10)
    ''', tuple(row))

conn.commit()
cursor.close()
conn.close()