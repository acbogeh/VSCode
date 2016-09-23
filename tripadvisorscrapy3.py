#将前两个爬虫函数化
#抓取tripadvisor.cn的图片，标题，标签
#-*- coding:utf8 -*-
from bs4 import  BeautifulSoup
import  requests
import io
import sys
import time
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST'
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,180,30)]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Cookie':'ServerPool=R; TAUnique=%1%enc%3AVopJqm1GEIZmUhvQ3ORmg%2BqMoK2C5WqgfnlNIsg9zOwYvJ58lDKZ6g%3D%3D; TASSK=enc%3AAETNXfsu%2FwKu%2FaZ0Yq8jbO1BI88koKY0Asoiat4doIYOms72sGz1%2BTyIYkX%2BsbidUXlu0Po6%2FscpsWN%2F1tAS%2BUImpBp3EYaNZq8Be2PhZBH%2BLSRtCjPWXnGvcokarLCkCw%3D%3D; _jzqy=1.1474350120.1474350120.1.jzqsr=baidu|jzqct=tripadvisor.-; _jzqckmp=1; __gads=ID=134543027bebae30:T=1474350120:S=ALNI_MaFgss6y8q1vpeWU_5O3BHcnAnN9w; _smt_uid=57e0cc27.c7fc16e; ki_u=e8a846f5-fa41-2447-3c5f-7010; CommercePopunder=SuppressAll*1474350362549; ki_s=165313%3A1.0.0.0.2%3B165314%3A1.1.0.1.2; _jzqx=1.1474358940.1474362193.2.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.jzqsr=tripadvisor%2Ecn|jzqct=/tourism-g60763-new_york_city_new_york-vacations%2Ehtml; TAAuth2=%1%3%3A121943edad4930eff17ea8fcf7211d63%3AADlVUmEJNLfPUE5fvTQwLpnF82nENigvS4JInYq2blhSzh2ZxWLcTeIgJVxfE4oGQtVhibA476XfFa8IdpUDrYfbp%2FPBSMaDQS5nEDeBYVe1CZA1DPoHNuW9qY0UMksVucybHpGrU24LleBYr6xGtdyRbEfm3rFEdOoNCI6se6wFgrnEBnh03%2FjC36TxTuEgDn%2FQdJfONOjkHShb2JHlE7fplGvPOZHeuLKjyvFvS34Q; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.293920_264l60763_264l105127_264*RS.1; CM=%1%t4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CHomeASess%2C2%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCpmPopunder_1%2C1%2C1474436715%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CViatorMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C2%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CRBAPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; bdshare_firstime=1474362355355; roybatty=TNI1625!AIMyjYvyc1F2EsIYtWdi%2BvBhxv%2FEbmKked%2BjqPqKrfGv3cbvBPXpROFJyUx456DpKJm8KkbXtSx5Z%2FFTylqGsV9%2FKbVTLOnO6FjO6CEflQZb%2BwsSbcL4VAdNMMxHj54Fj6YsV0yVUIO93KC4kwGWxTOYTJDfAbPgmacTpeUti8sx%2C1; ki_t=1474350121333%3B1474350121333%3B1474362376572%3B1%3B8; ki_r=; TASession=%1%V2ID.323A51FB232DCC5614B7FEE03A5D3ECF*SQ.32*MC.16631*PR.427%7C*LS.RecommendedAjax*GR.20*TCPAR.46*TBR.74*EXEX.92*ABTR.92*PPRP.29*PHTB.96*FS.78*CPU.94*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.FF7335BD472126A1B4B9B9DAF1FB95BF*LF.zhCN*FA.1*DF.0*LR.http%3A%2F%2Fbzclk%5C.baidu%5C.com%2Fadrc%5C.php%3Ftpl%3Dtpl_10144_14402_1%3Fl%3D1045915587%3Fie%3DUTF-8%3Ff%3D8%3Ftn%3Dbaidu%3Fwd%3Dtripadvisor%3Foq%3Dtripadvisor%3Frqlang%3Dcn*LP.%2F-a_tttype%5C.text-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.logo-m16631*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1474350117499-1*LG-12259272-2.1.F.*LD-12259273-.....; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1474350120,1474350167; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1474362377; _qzja=1.1202703478.1474350123178.1474358940532.1474362193152.1474362355266.1474362377078..0.0.8.3; _qzjb=1.1474362193152.3.0.0.0; _qzjc=1; _qzjto=8.3.0; _jzqa=1.2838362838848256000.1474350120.1474358940.1474362193.3; _jzqc=1; _jzqb=1.3.10.1474362193.1; NPID='
}

url_saves = 'http://www.tripadvisor.cn/Saves#1'

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    #print(wb_data)   一个response  <Response [200]>

    soup = BeautifulSoup(wb_data.text,'html.parser')
    titles = soup.select('div.property_title > a[target="_blank"]')  #增加[target="_blank"]进一步过滤掉名字带数字的内容
    imgs = soup.select('img[width="160"]') 
    #直接soup.select('img[width="160"]') 被js控制，导致失败
    cates = soup.select('div.p13n_reasoning_v2')
    for title,img,cate in zip(titles,imgs,cates):
        data = {
            '景点':title.get_text(),
            '图片':img.get('src'),
            '标签':list(cate.stripped_strings)  
            #对于1对多的数据结构，使用stripped_strings获取内容，并包成集合
        }   
        print(data)
        time.sleep(2)

def get_favs(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    titles = soup.select('a.location-name')
    imgs = soup.select('div.photo > div.sizedThumb > img')
    locations = soup.select('div.cvs-content > div.info > span')
    for title,img,location in zip(titles,imgs,locations):
        data = {
            'title':title.get_text(),
            'img':img.get('src'),
            'location':location.get_text()
        }
        print(data)

for url_single in urls:
    get_attractions(url_single)

#图片链接都一样，是由于反爬，可爬取移动端的图片解决
#chrome->检查->toggle device mode->iphone6