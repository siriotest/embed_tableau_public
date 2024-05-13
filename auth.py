import pymysql
import configparser
from configparser import ConfigParser

def login(username,password):
   conn = pymysql.connect(host="database-1.c7cge6um0ivl.eu-west-1.rds.amazonaws.com",
   user="admin", 
   password='ii!NkkH9p!WnzMR4BcHVGQ', 
   db='streamlit')
   cursor = conn.cursor() 
 #query = “”
 #values = (username, password)
   query = """call CheckUsers_1 (%s, %s)"""
   values = (username, password)
   cursor.execute(query, values)
   record = cursor.fetchone()
   return record[0]