
# importing required libraries
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
table1=pd.read_csv('/Users/saivenkat/Downloads/Untitled spreadsheet - Sheet1.csv')
table2=pd.read_csv('/Users/saivenkat/Downloads/Untitled spreadsheet - Sheet1 (1).csv')
table3=pd.read_csv('/Users/saivenkat/Downloads/Untitled spreadsheet - Sheet1 (2).csv')
table4=pd.read_csv('/Users/saivenkat/Desktop/pyhton/work_dummy.csv')
# print(mysql.connector.__file__)
dataBase = create_engine('mysql+mysqlconnector://root:Saivenkat#1@localhost:3306/gfg')

dBase=mysql.connector.connect(
  host='localhost',
  user='root',
  password='Saivenkat#1',
  database='gfg'
)


table1.to_sql(name='employee',con=dataBase,if_exists='replace',index=False)
table2.to_sql(name='employee_address',con=dataBase,if_exists='replace',index=False)
table3.to_sql(name='employee_salary',con=dataBase,if_exists='replace',index=False)
table4.to_sql(name='dummy',con=dataBase,if_exists='replace',index=False)
co=dBase.cursor()
sql="select e.FirstName,ea.City from employee as e join employee_address as ea on e.EmpolyeeID=ea.EmpolyeeID"

co.execute(sql)
ans=co.fetchall()
for i in ans:
  print(i)
co.close()
dataBase.dispose()

