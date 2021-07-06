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
from twilio.rest import Client
from rich.progress import Progress
import random

account_sid = 'ACe3dfdbc83769dea0f01b42577c74928f' 
auth_token = 'c6654224eadf65e549ddccc9fb7129bb' 
client = Client(account_sid, auth_token) 



def main():
   

    x = datetime.datetime.now()

    current_time = x.strftime("%d""-""%B""-""%Y"" ""%H"":""%M")
    current_date = str(current_time)


    # import model

    # model.add_scheduled_message('2','Message to be sent at 6:30','+254700419377','01-July-2021 18:30','01-July-2021 16:37')


    # #================ START OF BANNER TEXT ==========#
    with Progress() as progress:                        
                        task3 = progress.add_task("[cyan]Loading Program ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)

    print(colored.green("\n\n\n========================================================================"))

    f = Figlet(font='big')
    print (colored.green(f.renderText('Whatsapp')))

    print(colored.green("========================================================================="))
    print(colored.green("Schedule Whatsapp messages"))
    x = datetime.datetime.now()
    print(colored.green(x.strftime("%d""-""%B""-""%Y"" ""%H"":""%M")))
    print(colored.green("Messages will be sent from +1 415 523 8886 "))
    print(colored.green("=========================================================================\n\n"))

    print(colored.yellow("Login or Register For an account"))
    # #============= END OF BANNER TEXT ===============#


    def edit_message(rowid):
        
        edit_options = input("1. Edit the Message \n2. Cancel Message \n3. Edit Time \n4. Exit Message Editor \nEnter Choice: ")
        if(edit_options == '1'):
            
            message = input(colored.blue('Enter your message: '))
            message_update = model.edit_message_message(message,rowid)
            print(colored.cyan(message_update))
            user_messages()
        elif(edit_options == '2'):
            status = 'Cancelled'
            status_changed = model.edit_message_status(status,rowid)
            print(colored.cyan(status_changed))
            user_messages()
        elif(edit_options == '3'):
            schedule = input(colored.blue('Enter time to send message (e.g. 02-July-2021 14:35 ): '))
            change_schedule = model.edit_message_schedule(schedule,rowid)
            print(colored.cyan(change_schedule))
            user_messages()
        elif(edit_options == '4'):
            user_messages()
        else:
            print(colored.red('Invalid Choice. Try Again'))
            edit_message(user_id)
            



    login_prompt = input("Key in [L] to login and [R] to register: ")

    if(login_prompt == 'L'):
        print("Log in to your account")
        prompt_email = input("Enter Email: ")
        prompt_password = input("Enter Password: ")
        user_login = users.User(prompt_email,prompt_password).user_login()
        if (user_login == "Login Successful"):
            user_details = users.User(prompt_email,prompt_password).user_details()
            user_id = user_details[0][0]
            user_first_name = user_details[0][1]
            with Progress() as progress:                        
                        task3 = progress.add_task("[cyan]Verifying Credentials ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
            print(colored.green("\n\n========================================================================="))
            print(colored.white('Welcome back, ')+ str.capitalize(user_first_name))

            def user_settings():
                print(colored.green("=========================================================================\n[ Menu ]"))

                settings_option =input(colored.yellow("\n1. View Profile\n2. Change First Name \n3. Change Second Name \n4. Change Phone Number \n5. Change Password \n6. Back to Main Menu \nEnter Choice: "))

                if( settings_option == '1'):
                    print(colored.blue('\nView Profile'))
                    model.display_user_profile(user_id)
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Loading Profile ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    #print(colored.magenta('\n' + message_added))
                    user_settings()
                elif ( settings_option == '2'):
                    print(colored.green("\n========================================================================="))
                    
                    print(colored.green('Change First Name\n'))
                    new_first_name = input("Enter New First Name: ")
                    model.edit_first_name(new_first_name,user_id)

                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Saving First Name ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    user_settings()
                    
                
                    

                elif( settings_option == '3'):
                   
                    print(colored.green("\n========================================================================="))
                    print(colored.green('Change Second Name\n'))
                    new_second_name = input("Enter New Second Name: ")
                    model.edit_last_name(new_second_name,user_id)

                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Saving Last Name...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    user_settings()

                elif( settings_option == '4'):
                    print(colored.green("\n========================================================================="))
                    print(colored.green('Change Phone Number\n'))
                    new_phone = input("Enter New Phone Number: ")
                    
                    model.edit_phone(new_phone,user_id)
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Saving Phone number ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    user_settings()
                
                elif( settings_option == '5'):
                    print(colored.green("\n========================================================================="))
                    print(colored.green('Change Password\n'))
                    new_password = input("Enter New Password: ")
                    model.edit_password(new_password,user_id)
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Saving Password ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    user_settings()

                elif( settings_option == '6'):
                    with Progress() as progress:                        
                        task3 = progress.add_task("[cyan]Loading Menu", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)

                    user_messages()
                else:
                    return 0


            def user_messages():
                print(colored.green("=========================================================================\n[ Menu ]"))

                messages_category =input(colored.yellow("\n1. View Messages\n2. Add Message \n3. Scheduled Messages \n4. Sent Messages \n5. Cancelled Messages \n6. Settings \n7. Log Out \nEnter Choice: "))
                if( messages_category == '2'):
                    print(colored.blue('\nTo add new message'))
                    message = input('Enter your message: ')
                    receiver_number = input('Enter Phone number (e.g. +254700419377): ')
                    time_scheduled = input('Enter the time to send the message (e.g 02-July-2021 20:35): ')
                    message_added = model.add_scheduled_message(user_id,message,receiver_number,time_scheduled,current_date)
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Adding Messages...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    print(colored.magenta('\n' + message_added))
                    user_messages()
                elif (messages_category == '3'):
                    print(colored.green("\n========================================================================="))
                    
                    print(colored.green('All your scheduled messages\n'))

                    scheduled_messages = model.display_scheduled_messages(user_id)
                    print(colored.green("\n=========================================================================\n"))
                    select_message = input("Enter ROWID number to select message: ")
                    
                    single_message = model.display_selected_messages(select_message,user_id)
                    edit_message(select_message)

                elif(messages_category == '1'):
                   
                    print(colored.green("\n========================================================================="))
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Loading Messages...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    print(colored.green('All your messages\n'))

                    scheduled_messages = model.display_all_messages(user_id)
                    print(colored.green("\n=========================================================================\n"))
                    select_message = input("Enter ROWID number to select message: ")
                    single_message = model.display_selected_messages(select_message,user_id)
                    edit_message(select_message)

                elif( messages_category == '4'):
                    print(colored.green("\n========================================================================="))
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Loading Messages...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    print(colored.green('All cancelled messages\n'))
                    print(colored.green("\n========================================================================="))

                    model.display_sent_messages(user_id)
                    user_messages()
                
                elif( messages_category == '5'):
                    print(colored.green("\n========================================================================="))
                    with Progress() as progress:                        
                        task3 = progress.add_task("[green]Loading Messages...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    print(colored.green('All cancelled messages\n'))
                    print(colored.green("\n========================================================================="))

                    model.display_cancelled_messages(user_id)
                    user_messages()

                elif( messages_category == '6'):
                    user_settings()

                elif( messages_category == '7'):
                    with Progress() as progress:                        
                        task3 = progress.add_task("[cyan]Logging Out...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
                    main()
                else:
                    print(colored.red('invalid choice'))

                    user_messages()
            
            user_messages()

            
        else:
            print(colored.red("Error: Wrong Email/Password\n"))
            prompt_reset = input(colored.yellow("Press 1. To Reset Passord \n2. To Try Again"))
            if(prompt_reset == '1'):
                ask_email = input(colored.cyan('Enter your email: '))   
                e = ['a','b','c','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                random.shuffle(e)
                def listToString(e): 
                    easy_password = "" 
                    return (easy_password.join(e))
                password = listToString(e)[:7]

                conn = sqlite3.connect('database.db')
                db = conn.cursor()

                db.execute("SELECT phone FROM users WHERE email = ?;",[ask_email])
                record = db.fetchall()
                print(record[0][0])
                send_ph = 'whatsapp:'+str(record[0][0])

                messages = "*PASSWORD RESET*. Your new password is *" + password + "*"
                message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=messages,      
                              to=send_ph 
                          ) 
        

                model.reset_password(password,ask_email) 
            elif (prompt_reset == '2'):
                     return 1

            else:
                return 0

    elif(login_prompt ==  'R'):
        prompt_first_name = input(colored.cyan("Enter First Name: "))
        prompt_last_name = input(colored.cyan("Enter Last Nme: "))
        prompt_email = input(colored.cyan("Enter Email: "))
        prompt_phone = input(colored.cyan("Enter Phone: "))
        prompt_password = input(colored.cyan("Enter Password: "))
        confirm_password = input(colored.cyan("Enter Confirm Password: "))
        with Progress() as progress:                        
                        task3 = progress.add_task("[cyan]Creating Account ...", total=100)

                        while not progress.finished:
                           
                            progress.update(task3, advance=1.5)
                            time.sleep(0.02)
        if( prompt_password == confirm_password):
            users.Create_user(prompt_first_name,prompt_last_name,prompt_email,prompt_password,prompt_phone).create()
            main()
        else:
            print(colored.red("Error: Passwords do not match, Try Again"))

    #change message
    #change status
    #edit time
main()