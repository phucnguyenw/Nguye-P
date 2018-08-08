# 1. Download dantri page
from urllib.request import urlopen
import pyexcel
from bs4 import BeautifulSoup
url ="http://dantri.com.vn/"
connection= urlopen(url)
raw_data= connection.read()
text = raw_data.decode('utf-8')

soup = BeautifulSoup(text, 'html.parser')
# print(soup.prettify())
# f= open("dantri.html", "wb")
# f.write(raw_data)
# f.close()


# 2 Find the ROI
ul_news = soup.find('ul',"ul1 ulnew")

# 3. Extract Data
news_items =[]
li_list = ul_news.find_all('li')
for li in li_list:
    a = li.h4.a
    link = url + a['href']
    title=a.text
    item = {
        "Title": title,
        "Link": link    
    }
    news_items.append(item)

print(news_items)

pyexcel.save_as(records=news_items, dest_file_name="dantri.xlsx")



# 4 Save data