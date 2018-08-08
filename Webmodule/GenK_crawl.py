from urllib.request import urlopen
import pyexcel
from bs4 import BeautifulSoup
url ="http://genk.vn"
connection= urlopen(url)
raw_data= connection.read()
text = raw_data.decode('utf-8')

soup = BeautifulSoup(text, 'html.parser')



ul_news = soup.find('ul',id="LoadListCate")


news_items =[]
li_list = ul_news.find_all('li')
for li in li_list:
        div = li.div
        if div is not None:
            a = div.a
            link = url + a['href']
            title= a["title"]
        item = {
        "title": title, 
        "Link": link    
        }
        news_items.append(item)   




pyexcel.save_as(records=news_items, dest_file_name="gnk.xlsx")
