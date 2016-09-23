from bs4 import BeautifulSoup
from html.parser import HTMLParser
#from html5lib import html5parser
import io
import sys
import re
from urllib import request

#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

root_url = "http://www.fullgoal.com.cn"
urlcont = request.urlopen(root_url)
soup = BeautifulSoup(urlcont,'html.parser')
urlcont.close()
links = soup.find_all('td')
for link in links:
    print(link.get_text())