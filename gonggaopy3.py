#-*- coding:utf8 -*-
from bs4 import BeautifulSoup
import datetime, time, codecs
import requests
import os,sys
import smtplib
from email.mime.text import MIMEText    #发送带附件邮件所需
from email.mime.multipart import MIMEMultipart,MIMEBase
from email import encoders

def getInfo(max_index_user=5):
    stock_news_site = "http://ggjd.cnstock.com/gglist/search/ggkx/"
    # 定义抓取网址
    index = 0
    max_index = max_index_user
    num = 1
    temp_time = time.strftime("[%Y-%m-%d]-[%H-%M]", time.localtime())  # 获取当前时间并格式化
    store_filename = "StockNews-%s.log" % temp_time  # 定义输出文件名
    pathname = os.path.join(sub_folder,store_filename)   #用os.path.join拼接文件名避免缺少斜杠等问题
    fOpen = codecs.open(store_filename, 'w', 'utf-8')
    print(fOpen.read)
    # f=open('XXXXX', 'r')
    # content = f.read().decode('utf-8')
    # 更好的方法是使用codecs.open读入时直接解码：
    # f = codecs.open(XXX, encoding='utf-8')
    # content = f.read()
    while index < max_index:#index < max_index情况下为1，则实行后续动作,具体作用为只抓1-5页的公告
        company_news_site = stock_news_site + str(index)#重新拼地址
        raw_content = ""
        r = requests.get(company_news_site)
        soup = BeautifulSoup(r.text, "html.parser") #bs解析内容
        all_content = soup.find_all("span", "time")  #获取公告时间

        for i in all_content:
            #i  格式为<span class="time">09-14 13:04</span>
            news_time = i.string
            #news_time 格式为news_time 09-14 13:04
            node = i.next_sibling
            #返回i的下一个元素
            #node 格式为<a href="http://ggjd.cnstock.com/company/scp_ggjd/tjd_ggkx/201609/3901303.htm" target="_blank" title="首航节能午后临停 拟披露重大事项">首航节能午后临停 拟披露重大事项</a>
            str_temp = "No.%s \n%s\t%s\n---> %s \n\n" % (str(num), news_time, node['title'], node['href'])
            #str_temp 格式为 No.1 09-14 13:04	首航节能午后临停 拟披露重大事项---> http://ggjd.cnstock.com/company/scp_ggjd/tjd_ggkx/201609/3901303.htm
            fOpen.write(str_temp)
            num = num + 1  #控制NO.*的数字

        #print "index %d" %index
        index = index + 1  #获取后一页网页内容

    fOpen.close()

    mailto_list = 'yaoqi@xx.com.cn'
    mail_host = "mail.xx.com.cn"  # 设置服务器
    mail_user = "yaoqi"  # 用户名
    mail_pass = "Password456"  # 口令 
    mail_postfix = "xx.com.cn"  # 发件箱的后缀
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    content = 'This is test mail!'#邮件正文
    msg = MIMEMultipart()
    body = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
    msg.attach(body)
    msg['Subject'] = "Subject Test"  # 设置主题
    msg['From'] = me  
    msg['To'] = 'yaoqi@xx.com.cn'
    #附件内容，若有多个附件，就添加多个part, 如part1，part2，part3
    part = MIMEBase('application', 'octet-stream')
    # 读入文件内容并格式化，此处文件为当前目录下，也可指定目录 例如：open(r'/tmp/123.txt','rb')
    part.set_payload(open(pathname,'rb').read())
    encoders.encode_base64(part)
    ## 设置附件头
    part.add_header('Content-Disposition', 'attachment; filename="test.txt"')
    msg.attach(part)
       
    try:  
        s = smtplib.SMTP_SSL(mail_host)
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  # 发送邮件
        s.close()  
        print('success')
        return True  
    except Exception as e:  
        print (str(e))
        print ('fail')  
        return False
        
def execute_task(n=60):
    period = n
    while True:
        print (datetime.datetime.now())#2016-09-14 14:07:04.902000  格式
        getInfo(3)
        time.sleep(3600 * period)



if __name__ == "__main__":

    sub_folder = os.path.join(os.getcwd(), "stock")  # os.getcwd 获取当前目录  os.path.join 拼接目录和文件名
    if not os.path.exists(sub_folder):#如果sub_folder不存在
        os.mkdir(sub_folder)#建目录
    os.chdir(sub_folder)#cd到sub_folder
    execute_task(12)#调用执行函数，传入分钟数

