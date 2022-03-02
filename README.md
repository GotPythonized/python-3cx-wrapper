# python-3cx-wrapper
Simple 3CX API wrapper


 _____  ______  __  _____      _                 _                 
|___ / / ___\ \/ / | ____|_  _| |_ ___ _ __  ___(_) ___  _ __  ___ 
  |_ \| |    \  /  |  _| \ \/ / __/ _ \ '_ \/ __| |/ _ \| '_ \/ __|
 ___) | |___ /  \  | |___ >  <| ||  __/ | | \__ \ | (_) | | | \__ \
|____/ \____/_/\_\ |_____/_/\_\\__\___|_| |_|___/_|\___/|_| |_|___/
                                                                   


Choose service you want to use : 

                1 : Setup 3CX Authenication 
                2 : Add one extension by one
                3 : Add multiple extensions
                4 : Get extension qrcode
                0 : Exit


First thing, you need to authenticate to your PBX
Next, select 2 or 3 for one or more extensions

To add multiple extensions:
vars > number:int, first_name:str, last_name:str, email:str, mobile:str, outb_call_id:str, voice_mail_enabled:bool, accept_multiple_calls:bool

list(
    dict(number=4002, first_name='John', last_name='Doe', email='john.doe@example.com' ),
    dict(number=4003, first_name='Ginette', last_name='Doe', email='gin.doe@example.com' ),
    dict(number=4004, first_name='July', last_name='Doe', email='july.doe@example.com' ),
    )

