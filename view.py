import datetime
from os import error
from test_model import edit_message
import time
import sqlite3
from tabulate import tabulate
from clint.textui import puts, colored, indent
from pyfiglet import Figlet
import users
import model

def main():
    x = datetime.datetime.now()

    current_time = x.strftime("%d""-""%B""-""%Y"" ""%H"":""%M")
    current_date = str(current_time)


    # import model

    # model.add_scheduled_message('2','Message to be sent at 6:30','+254700419377','01-July-2021 18:30','01-July-2021 16:37')


    # #================ START OF BANNER TEXT ==========#

    print(colored.green("\n\n\n========================================================================"))

    f = Figlet(font='big')
    print (colored.green(f.renderText('Whatsapp')))

    print(colored.green("========================================================================="))
    print(colored.green("Schedule Whatsapp messages"))
    x = datetime.datetime.now()
    print(colored.green(x.strftime("%d""-""%B""-""%Y"" ""%H"":""%M")))
    print(colored.green("Messages will be sent from +254700419377"))
    print(colored.green("=========================================================================\n\n"))

    print(colored.yellow("Login or Register For an account"))
    # #============= END OF BANNER TEXT ===============#


    def edit_message(rowid):
        edit_options = input("1. Edit the Message \n2.Cancel Message \n3.Edit Time \nEnter Choice: ")
        if(edit_options == '1'):
            message = input(colored.blue('Enter your message: '))
            message_update =model.edit_message_message(rowid,current_time,message)
            print(message_update)
            user_messages()
        elif(edit_options == '2'):
            status = 'Cancelled'
            model.edit_message_status(rowid,status,current_time)
            user_messages()
        elif(edit_options == '3'):
            schedule = input(colored.blue('Enter time to send message (e.g. 02-July-2021 14:35 ): '))
            model.edit_message_schedule(rowid,schedule,current_time)
            user_messages()
        else:
            print(colored.red('Invalid Choice. Try Again'))
            edit_message(user_id)
            



    login_prompt = input("Key in [L] to login and [R] to register: ")

    if(login_prompt == 'l' or 'L'):
        print("Log in to your account")
        prompt_email = input("Enter Email: ")
        prompt_password = input("Enter Password: ")
        user_login = users.User(prompt_email,prompt_password).user_login()
        if (user_login == "Login Successful"):
            user_details = users.User(prompt_email,prompt_password).user_details()
            user_id = user_details[0][0]
            user_first_name = user_details[0][1]
            print(colored.green("\n=========================================================================\n\n"))
            print('Welcome back '+ ' ' + user_first_name)


            def user_messages():
                messages_category =input("View Messages\n1. Add Message \n2. Scheduled Messages \n3. Sent Messages \n4. Cancelled Messages \nEnter Choice:")
                if( messages_category == '1'):
                    print(colored.blue('To add new message'))
                    message = input('Enter your message: ')
                    receiver_number = input('Enter Phone number (e.g. +254700419377): ')
                    time_scheduled = input('Enter the time to send the message (e.g 2-July-2021 20:35): ')
                    model.add_scheduled_message(user_id,message,receiver_number,time_scheduled,current_date)
                    
                    user_messages
                elif (messages_category == '2'):
                    print(colored.green("\n========================================================================="))
                    print(colored.green('All your scheduled messages\n'))

                    scheduled_messages = model.display_scheduled_messages(user_id)
                    print(colored.green("\n=========================================================================\n"))
                    select_message = input("Enter ROWID number to select message: ")
                    single_message = model.display_selected_messages(select_message,user_id)
                    edit_message(user_id)
                elif( messages_category == '4'):
                    model.display_cancelled_messages(user_id)
                else:
                    print('invalid choice')
            user_messages()
        else:
            print(colored.red("Error: Wrong Email/Password"))

    #change message
    #change status
    #edit time
main()