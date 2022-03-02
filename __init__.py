
from api.extensions import Extensions
from clint.textui import colored
from pyfiglet import Figlet
import getpass
import os
import logging
import sys 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)

print(__name__)
extensions = Extensions()

def welcome(text):
    result = Figlet()
    return colored.cyan(result.renderText(text))

def auth():
    extensions.auth.username = input("Username: ")
    extensions.auth.password = getpass.getpass("Password: ")
    extensions.auth.fqdn = input("FQDN: ")
    extensions.auth.port = input("Port (defauld: 5001): ") or 5001
    return

def add_one_by_one():

    print('Press CTRL+C to stop.')
    while True:
        os.system('clear')
        number = input('Extension Number: ')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        email = input('Email: ')
        cell_phone = input('Cell Phone: ')
        outb_call_id = input('Outbound Caller ID: ')
        voice_mail_enabled = input('Voice Mail Enabled (y/N): ')
        if voice_mail_enabled.lower() == 'y':
            voice_mail_enabled = True
        else:
            voice_mail_enabled = False
        accept_multiple_calls = input('Accept Multiple Calls (y/N): ')
        if accept_multiple_calls.lower() == 'y':
            accept_multiple_calls = True
        else:
            accept_multiple_calls = False
        extensions.add_extension(number, first_name, last_name, email, cell_phone, outb_call_id, voice_mail_enabled, accept_multiple_calls)
        if input('Add another (y/N): ').lower() == 'n':
            break
        
    

def add_from_list():
    EXTENSIONS = [{'number': '4002', 'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'cell_phone':None, 'outb_call_id':None, 'voice_mail_enabled':None, 'accept_multiple_calls':None,}]
    for i in EXTENSIONS:
        extensions.add_extension(**i)



if __name__ == "__main__":
    try:
        while True:
            print(welcome("3CX Extensions"))
            print("\nChoose service you want to use : ")
            print("""
                1 : Setup 3CX Authenication 
                2 : Add one extension by one
                3 : Add multiple extensions
                4 : Get extension qrcode
                0 : Exit"""
                    )
            choice = input("\nEnter your choice : ")

            if choice == '1':
                auth()
            elif choice == '2' :
                add_one_by_one()
            elif choice == '3' :
                add_from_list()
            elif choice == '4' :
                extensions.get_qrcode(input("Extension Number: "))
            elif choice == '0':
                exit()
    except KeyboardInterrupt:
        print('\nCtrl+C pressed\nQuitting...')

# 
