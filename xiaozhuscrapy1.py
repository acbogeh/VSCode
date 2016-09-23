from bs4 import BeautifulSoup
import requests
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')




def scrapy(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    #该也面就一个元素匹配，故直接用[0].text获取
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')[0].text
    departs = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')[0].text.replace("\n","").strip() #replace过滤换行符,strip过滤空格
    prices  = soup.select('#pricePart > div.day_l > span')[0].text
    images = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    owners = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
    host_gender = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')[0].get('class')[0]

    def gender(host_gender):
        if host_gender == "member_girl_ico":
            return "女"
        else:
            return "男"
    gendera = gender(host_gender)

    data = {
        'title':titles,
        'address':departs,
        'price':prices,
        'pic':images,
        'host_name':owners,
        'host_gender':gender(host_gender)
        }
    print(data)


page_link = []
def get_urls(page_number):
    for x in range(1,page_number):
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(x)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'html.parser')
        for link in soup.select('a.resule_img_a'):
            page_link.append(link.get('href'))  #不加'href'无法获取
get_urls(3)

for url in page_link:
    scrapy(url)
   

        
        