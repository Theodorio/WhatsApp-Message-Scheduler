import datetime
from os import error
import time
import sqlite3


current_date = datetime.date.today()
current_time = time.localtime()

year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday
hour = current_time.tm_hour
minutes = current_time.tm_min


scheduled_time = year,month,day,hour,minutes
#print time as stringf
#print( f'{year}{month}{day}{hour}{minutes}')
#timer_set = f'{year}{month}{day}{hour}{minutes}'

class User:
    #constructor
    def __init__(self,email,password):
      self.email = email
      self.password = password


        

    def user_login(self):
        conn = sqlite3.connect('database.db')
        db = conn.cursor()
        db.execute("SELECT rowid, first_name, last_name, email, password, created_at FROM users where email = ? AND password = ?;",(self.email,self.password))
        record = db.fetchall()
        if(len(record) == 1):
          response = "Login Successful"
          return response
        else:
          response = "Error Login In"
          return response
        #print(record)

    def user_details(self):
      conn = sqlite3.connect('database.db')
      db = conn.cursor()
      db.execute("SELECT rowid, first_name, last_name, email, password, created_at FROM users where email = ? AND password = ?;",(self.email,self.password))
      record = db.fetchall()   
      return record

#class will create user
class Create_user(User):
    #constructor
     def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

     def create(self):
        conn = sqlite3.connect('database.db')
        db = conn.cursor()
        try:
          db.execute("INSERT INTO users (first_name,last_name,email,password,created_at) VALUES (?,?,?,?,?)",(self.first_name,self.last_name,self.email,self.password,current_date))
          conn.commit()
          response = "Account successfully created"
          return response
        except:
          response = "Error creating account"
          return response

new_user = User('kahenyaa','qwerty')
reg_user = Create_user('john','kahenya','kahenyaa@gmail.com','qwerty').create()
