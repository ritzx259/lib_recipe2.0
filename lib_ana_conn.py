import pandas as pd
import sqlalchemy
import pymysql

mydb=sqlalchemy.create_engine('mysql+pymysql://root:Ritz6669@localhost:3306/library')
#mydb=sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}".format(connection_string)')
print(mydb)
authors = pd.read_csv(r'/Users/ritzmk/PycharmProjects/pythonProject/library_management/ipauthors.csv')
publishers = pd.read_csv(r'/Users/ritzmk/PycharmProjects/pythonProject/library_management/ippublishers.csv')
students=pd.read_csv(r'/Users/ritzmk/PycharmProjects/pythonProject/library_management/ipstudent_.csv')
books=pd.read_csv(r'/Users/ritzmk/PycharmProjects/pythonProject/library_management/books.csv')
orders=pd.read_csv(r'/Users/ritzmk/PycharmProjects/pythonProject/library_management/ipstudent_order.csv')#,parse_dates=['order _date']
authors.to_sql(name='authors_details',con=mydb,if_exists='replace',index=False)
publishers.to_sql('publishers_details',mydb,if_exists='replace',index=False)
books.to_sql('books_details',mydb,if_exists='replace',index=False)
students.to_sql('students_details',mydb,if_exists='replace',index=False)
orders.to_sql('order_details',mydb,if_exists='replace',index=False)