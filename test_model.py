from _pytest.python_api import raises
import pytest
import model


#test if user table is created
def create_user_table():
    user_table = model.create_user_table()
    return user_table

def test_create_user_table():
    assert model.create_user_table() == 'Users Table already created'


#test if messages table is created
def create_message_table():
    message_table = model.create_message_table()
    return message_table

def test_create_message_table():
    assert model.create_message_table() == 'Message table already created'


#test add message
def add_message():
    add_message = model.add_scheduled_message()
    return add_message

def test_add_message():
    assert model.add_scheduled_message('2','Test at 4:18','+254700419377','01-July-2021 23:10','01-July-2021 16:18') == "Message added Successfully"


#test view all messages from user
def view_all_messages():
    view_all_messages = model.display_all_messages()
    return view_all_messages

def test_view_all_messages():
    assert model.display_all_messages(4) == "Displaying all message"


#test  view scheduled messages from user
def view_scheduled_messages(x):
    view_scheduled_messages = model.display_scheduled_messages
    return view_scheduled_messages

def test_view_scheduled_messages():
    assert model.display_scheduled_messages(4) == "Displaying all message"


#test view cancelled messages
def view_scheduled_messages():
    view_cancelled_messages = model.display_cancelled_messages()
    return view_cancelled_messages

def test_view_cancelled_messages():
    assert model.display_cancelled_messages(4) == "Displaying all message"


#test if selected message is available
def display_selected_message():
    display_selected_message = model.display_selected_messages()
    return display_selected_message

def test_display_selected_message():
    assert model.display_selected_messages(70,2) == "Message Found"


#test if selected message is not found
def display_selected_message_not_found():
    display_selected_message_not_found = model.display_selected_messages()
    return display_selected_message_not_found

def test_display_selected_message_not_found():
    assert model.display_selected_messages(1234,567) == "Message not Found"


#edit message
def edit_message():
     edit_message = model.edit_message_message()
     return edit_message

def test_edit_message():
     assert model.edit_message_message("message changed",71) == "Message Successfully Updated"


#edit status
def edit_status():
    edit_status = model.edit_message_status()
    return edit_status

def test_edit_status():
    assert model.edit_message_status("cancelled",70) == "Status Successfully Updated"


#edit scheduled time
def edit_scheduled_time():
    edit_scheduled_time = model.edit_message_status()
    return edit_scheduled_time

def test_edit_scheduled_time():
    assert model.edit_message_schedule('1','tomorrow') == "Schedule Successfully Updated"