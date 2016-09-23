#encoding=UTF-8
import mysql.connector
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
conn = mysql.connector.connect(user='otrs', password='otrs', host='192.168.32.164', port='3306', database='otrs',charset='utf8')
cursor = conn.cursor()
cursor.execute('select * from users' )
result = cursor.fetchall()
L=[x[1] for x in result] 
print(L)
cursor.close()
conn.close()