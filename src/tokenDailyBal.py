import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='Zjj19911031', db='tokenlist')

a = conn.cursor()

sql= 'select * from tokenlist.aion'

a.execute(sql)

countrow = a.execute(sql)
print("Number of rows: ", countrow)
