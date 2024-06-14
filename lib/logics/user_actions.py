from lib.backend.connection import DbHandler
# from  lib.logics  import *

from utils import * 

        

class UserActions(DbHandler):
    oneconn = DbHandler()
    def __init__(self):
        super().__init__()
        self.uid = None
        self.uname = None
        self.oneconn = DbHandler()


    def confirm_login(self):
        name = input("Enter Username >> ")
        password = input("Enter Password >> ")
        data = {
            "uname": name,
            "password": password
        }

        response = self.oneconn.select_records('users',data)
        if len(response) > 0 :

            self.uid = response[0]['uid']
            self.uname = response[0]['uname']
            info.print_success(f"Successfully logged in as {self.uname}")
        else:
            info.print_info("Opps your Credentials are Wrong")
    
    def user_menu(menudata):
        info.print_info(" \n**Navigate By Commands**")

        return display.generate_table(menudata)

    # logout
    def confirm_logout(self):
        self.uid = None
        self.uname = None
        info.print_info("Successfully logged out")

    # see available tokens
    def sys_tokens():
        response = UserActions.oneconn.select_records('decentralized')

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
    def sell_tokens(self,token_qty,token_price):
        print("sold tokens")
        pass
    def buy_tokens(self,token_qty,token_price):
        print("bought tokens")
        pass
    def see_personal(self):
        if self.uid:
            info.print_info("**Your Details**")
            response = self.oneconn.select_records('users',{"uid": self.uid})
            display.generate_table(response)
            info.print_info("**Your Balances**")
            response = self.oneconn.select_records('balances',{"b_uid": self.uid})
            display.generate_table(response)
        else:
            return info.print_error("Opps you have to be logged in to ACCESS your details")


    
    def kill(self):
        if not self.uid:
            info.print_error("You have to be logged in to Complete this Action")
            return
        
        where = {
            "uid": self.uid
        }
        
        response = DbHandler().delete_records('users',where)
        
        if response[0]['status']:
            info.print_info(F"Account deleted successfully for at {self.uname} on {self.uid}")
            self.confirm_logout()
        else:
            info.print_error(F"Error: {response.error}")
        pass  
    #buy tokens

    #see market token

    # see balances

    #see his transactions


    # send token






    # cancel trade


    #view personal history


    #delete account