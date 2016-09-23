from bs4 import BeautifulSoup
import requests
import time
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#异步加载型网页，通过chrome F12获取
#network -->XHR-->下拉网页观察地址变化
url = 'https://knewone.com/discover?page='

def get_page(url,data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    imgs = soup.select('a.cover-inner > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')

    if data==None:
        for img,title,link in zip(imgs,titles,links):
            data = {
                'img':img.get('src'),
                'title':title.get('title'),
                'link':link.get('href')
            }
            print(data)


def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)


get_more_pages(1,10)