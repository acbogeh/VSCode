#抓取tripadvisor.cn的图片，标题，标签
#-*- coding:utf8 -*-
from bs4 import  BeautifulSoup
import  requests
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(url)
#print(wb_data)   一个response  <Response [200]>

soup = BeautifulSoup(wb_data.text,'html.parser')
titles = soup.select('div.property_title > a[target="_blank"]')  #增加[target="_blank"]进一步过滤掉名字带数字的内容
imgs = soup.select('img[width="160"]') 
#直接soup.select('img[width="160"]') 被js控制，导致失败
cates = soup.select('div.p13n_reasoning_v2')
for title,img,cate in zip(titles,imgs,cates):
   
    data = {
        'title':title.get_text(),
        'imgs':img.get('src'),
        'cates':list(cate.stripped_strings)  
        #对于1对多的数据结构，使用stripped_strings获取内容，并包成集合
    }   
    print(data)
#使用format方式输出只能输出整段href，无法过滤标签
#print ('title:{0} img:{1} cate:{2}'.format(title,img,cate))