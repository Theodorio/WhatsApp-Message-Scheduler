import threading
import time
import schedule
import datetime
import sqlite3
global str

import os
from twilio.rest import Client
account_sid = 'ACe3dfdbc83769dea0f01b42577c74928f' 
auth_token = '08d0064412d04fa478e9f817af12782b' 
client = Client(account_sid, auth_token) 


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

print("Whatsapp Scheduler is running")

def job():

    x = datetime.datetime.now()

    current_time = x.strftime("%d""-""%B""-""%Y"" ""%H"":""%M")
    t = str(current_time)
    print(t)
    p = 'today'
    conn = sqlite3.connect('database.db')
    db = conn.cursor()
    db.execute("SELECT rowid, user_id, message, status, receiver_number, time_scheduled, created_at, updated_at FROM messages WHERE status = 'Scheduled' and time_scheduled = ? ;",[t])
    records = db.fetchall()
    print(records)
    if(len(records) > 0):
        for record in records:
            print(current_time)
            messages = record[2]
            #model.edit_message_status(rowid,'Sent',t)
            phone = record[4]
            rowid = record[0]
            
            time_scheduled = record[5]
            send_ph = 'whatsapp:'+ phone

            #twilio_message = client.messages.create(body= messages,from_='whatsapp:+14155238886',to= send_ph )
            message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=messages,      
                              to=send_ph 
                          ) 
            print(message.sid)
            db.execute("UPDATE messages SET status = 'Sent' AND updated_at = ? WHERE rowid = ?;",(str(t),int(rowid)))
            conn.commit() 
        

        #model.edit_message_status(rowid,'Sent',t)
        else:
            response = "No messages"
            return response
        

    

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(60).seconds.do(run_threaded, job)



while 1:
    schedule.run_pending()
    time.sleep(0)