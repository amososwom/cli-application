from lib.backend.connection import DbHandler
from utils import * 

menudata = [
        {
            "arrow": ">**",
            "command": "create",
            "description": "Create Account",
            "func": "Accepts Inputs"
        },
        {
            "arrow": ">**",
            "command": "login",
            "description": "Login To Account",
            "func": "Accepts Inputs"
        },   
        {
            "arrow": ">**",
            "command": "view_market",
            "description": "View Market Analysis",
            "func": "Accepts Inputs"
        },   
        {
            "arrow": ">**",
            "command": "view_all_users",
            "description": "See full users",
            "func": "systemaction.see_users"
        },   
        {
            "arrow": ">**",
            "command": "view_acc",
            "description": "Your Account Details",
            "func": "useraction().see_personal"
        },   
        {
            "arrow": ">**",
            "command": "buy_token",
            "description": "Buy Tokens Form Market",
            "func": "useraction().see_personal"
        },   
        {
            "arrow": ">**",
            "command": "sell_token",
            "description": "Realse Tokens to Market",
            "func": "useraction().see_personal"
        },   
        {
            "arrow": ">**",
            "command": "send_token",
            "description": "Send your Tokens to A user",
            "func": "useraction().see_personal"
        },   
        {
            "arrow": ">**",
            "command": "delete_acc",
            "description": "Withdraw Funds",
            "func": "Accepts Withdrawal Inputs"
        },   
        {
            "arrow": ">**",
            "command": "logout",
            "description": "Logout From CLI-Application",
            "func": "useraction().confirm_logout"
        },  
        {
            "arrow": ">**",
            "command": "exit",
            "description": "Exit Application",
            "func": "func"
        }    
    ]
        

class UserActions(DbHandler):
    def __init__(self):
        super().__init__()
        self.uid = None
        self.uname = None


    def confirm_login(self, name, password):
        data = {
            "uname": name,
            "password": password
        }

        response = DbHandler().select_records('users',data)

        if len(response) > 0 :

            self.uid = response[0]['uid']
            self.uname = response[0]['uname']
            info.print_success(f"Successfully logged in as {self.uname}")
        else:
            info.print_info("Opps your Credentials are Wrong")
    
    def user_menu():
        info.print_info(" \n**Navigate By Commands**")

        return display.generate_table(menudata)

    # logout
    def confirm_logout(self):
        self.uid = None
        self.uname = None
        info.print_info("Successfully logged out")

    # see available tokens
    def sys_tokens():
        response = DbHandler().select_records('decentralized')

        return response if response else []
    
    @classmethod
    def display_token(cls):
        response = cls.sys_tokens()

        if len(response) > 0:
            for val in response:

                token_name = f"{val['token_name']} - {val['token_sys']}"
                token_qty = info.dollar(val['token_qty'], 4)
                token_price = info.dollar(val['token_price'], 2)
                
                info.print_info(f"**inflation-Rate @ {info.print_r_success('$ ' + token_price)} {info.print_r_info('**')} \n")
                
                print(f">Token-Name: {info.print_r_success(token_name)}")
                print(f">Token-Qty: {info.print_r_success(token_qty)}")
                print(f">Token @Price: {info.print_r_success('$ ' + token_price)}")
        else:
            print("No tokens available")

    # sell token
    def sell_token(self,token_qty,token_price):
        pass

    def see_personal(self):
        if self.uid:
            print("**Your Details**")
            response = DbHandler().select_records('users',{"uid": self.uid})
            display.generate_table(response)
            print("**Your Balances**")
            response = DbHandler().select_records('balances',{"b_uid": self.uid})
            display.generate_table(response)
        else:
            return info.print_error("Opps you have to be logged in to ACCESS your details")


        
    #buy tokens

    #see market token

    # see balances

    #see his transactions


    # send token






    # cancel trade


    #view personal history


    #delete account