import uuid
from utils import * 

from lib.backend.connection import DbHandler
        
from  lib.logics.system_actions import SystemAction

class UserActions(DbHandler):
    oneconn = DbHandler()

    def __init__(self):
        super().__init__()
        self.uid = None
        self.uname = None
        self.oneconn = DbHandler()

    def confirm_login(self):
        name = input("> Enter Username >> ")
        password = input("> Enter Password >> ")
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
        if self.uid:
            self.uid = None
            self.uname = None
            info.print_info("Successfully logged out")
        else: 
            info.print_info("Your Not logged in")
            

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
    def sell_tokens(self): #,token_qty,token_price):
        if not self.loggedin():
            return

        info.print_info("**Your Current Balances**")
        response = self.oneconn.select_records('balances',{"b_uid": self.uid})
        display.generate_table(response)

        curbal = response[0]['b_amount']
        curtoken = response[0]['b_token']

        if not curtoken > 0:

            info.print_info(f"This Action Cant be accepeted due to low Token_Balance @ {curtoken}")
            return
        
        while True:
            
            token_qty = int(input("> Enter Token-QTY you would like to release >>.. "))
            token_price = int(input("> Enter selling amount for all out token >>.. "))

            if token_qty > curtoken:
                info.print_error(f"You have only {curtoken} token available you cant release more than {curtoken}")
                continue # this will skip the below code and the current illitaration 
            if token_qty < 0:
                info.print_error(f"You have only {curtoken} token available")
                continue # this will skip the below code and the current illitaration 
            break

        usersubdata = {
            "b_token": curtoken - token_qty
        }
        useruid = {
            "b_uid": self.uid
        }
            
        randuid = uuid.uuid4().hex
        marketdata = {
            "m_id": randuid[0:5],
            "m_uid": self.uid,
            "m_token": token_qty,
            "m_price": token_price,
            "m_type": 1
        }
        
        updatedata = self.oneconn.update_records('balances',usersubdata,useruid)

        if updatedata[0]['status']:

            info.print_info("**Your Current Balances**")
            response = self.oneconn.select_records('balances',{"b_uid": self.uid})
            display.generate_table(response)

            self.oneconn.insert_records('markets',marketdata)
            info.print_success(f"Successfully Sold {token_qty} tokens for {info.dollar(token_price,2)}")

    def buy_tokens(self):
        if not self.loggedin():
            return
        
        info.print_info("**Your Current Balances**")
        response = self.oneconn.select_records('balances',{"b_uid": self.uid})
        display.generate_table(response)
        SystemAction().see_market()

        curbal = response[0]['b_amount']
        curtoken = response[0]['b_token']

        alldata = self.oneconn.select_records('markets')


        while True:
            token_id = input("> from the Market table['m_id'] type th ID you would like to purchase >>.. ").strip()

            found = False

            if token_id == 'exit':
                break
            else:
                for values in alldata:
                    if token_id == values['m_id']:
                        tradeid = values['m_id']
                        owneruid = values['m_uid']
                        owner_token_qty = int(values['m_token'])
                        owner_token_price = int(values['m_price'])
                        info.print_success(f"Trade id {token_id} selected Successfully..")
                        info.print_info(f"Attempting Purchase..")
                        
                        found = True
                        break
                if found:
                    break
                else:
                    info.print_error(f"you provided in correct market id please redo")

        if not found:
            info.print_info("Exiting Trade..")
            return
        if curbal > 0 and curbal >= owner_token_price:

            usersubdata = {
                "b_amount": curbal - owner_token_price,
                "b_token": curtoken + owner_token_qty
            }
            self.oneconn.update_records('balances', usersubdata, {"b_uid": self.uid})
            randuid = uuid.uuid4().hex
            usertransdata = {
                "trans_id": randuid[0:9],
                "trans_uid": self.uid,
                "trans_type": 'Bought Token',
                "trans_token": owner_token_price,
                "trans_state": 2
            }
            self.oneconn.insert_records('transactions',usertransdata)

            upline = self.oneconn.select_records('users',{'uid': owneruid})

            if len(upline) > 0:
                ownerdat = {
                    "b_amount": curbal - owner_token_price
                }

                self.oneconn.update_records('balances', ownerdat, {"b_uid": owneruid})
                self.oneconn.delete_records('markets',{'m_id': tradeid})

            info.print_success("Trade completed Succefully")

            info.print_info("**Your Current Balances**")
            response = self.oneconn.select_records('balances',{"b_uid": self.uid})
            display.generate_table(response)


        else:
            info.print_error("Insufficiemt Funds for this please try selling your token to grab more coins") 
        return


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

    def loggedin(self):
        if self.uid:
            return True 
        else: 
            info.print_error("You have to be logged in to Complete this Action")
            return False
    def kill(self):
        if not self.loggedin():
            return
        print("doning")
        where = {
            "uid": self.uid
        }
        
        response = DbHandler().delete_records('users',where)
        
        if response[0]['status']:
            self.confirm_logout()
            info.print_info(F"Account deleted successfully for at {self.uname} on {self.uid}")
        else:
            info.print_error(F"Error: {response.error}")
        pass  
