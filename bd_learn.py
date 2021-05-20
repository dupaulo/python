import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

df = pd.read_csv('arquivos/brdsPatrocinados1.csv',index_col=False,delimiter=',')



try:
    conn = msql.connect(host='localhost',database='python_lear' ,user='paulo',  password='paulo123')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Database is connected", record)
        cursor.execute('DROP TABLE IF EXISTS brds;')
        print ('Creating table...')
        cursor.execute("create table brds(brd_name varchar(255), codigocvm varchar(255))")
        print ('Tabela criada !')


        for i,row in df.iterrows():
            sql = "insert into python_lear.brds (brd_name,codigocvm) values(%s,'%s')"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)