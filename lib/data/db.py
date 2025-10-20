import pymysql
import pandas as pd
from sqlalchemy import create_engine

# def query(sql):
#    host,port,db,user,pw=para()
#    engine=create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(user,pw,host,port,db))
#    return (pd.read_sql_query(sql,engine))

def update(sql):
   host,port,db,user,pw=para()
   con=pymysql.connect(host=host,port=port,db=db,user=user,password=pw,charset='utf8')
   with con.cursor() as cursor:
      print('db_upd:',cursor.execute(sql))
      con.commit()

def update2(sql,value):
   host,port,db,user,pw=para()
   con=pymysql.connect(host=host,port=port,db=db,user=user,password=pw,charset='utf8')
   with con.cursor() as cursor:
      print('db_upd:',cursor.executemany(sql,value))
      con.commit()

def para():
   host='127.0.0.1'
   port=23306
   db='growdb'
   user='growdbro'
   pw='foam374:buts'
   return host,port,db,user,pw

from sqlalchemy import create_engine,text
def query(sql):
    host,port,db,user,pw=para()
    engine=create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(user,pw,host,port,db))
    return (pd.read_sql_query(sql=text(sql),con=engine.connect()))