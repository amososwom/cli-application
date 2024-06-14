import uuid 

from lib.backend.connection import DbHandler
from utils import * 

class SystemAction(DbHandler):
    def __init__(self):
        super().__init__()
        self.oneconn = DbHandler()
    #  create user
    def create_user(self):
        uname = input("Enter Username >> ")
        password = input("Enter Password >> ")
    
        if not uname or not password:
            info.print_error("fields cant be empty")
            return
        confirmusers = self.oneconn.select_records('users',{"uname": uname})
        if len(confirmusers) > 0:
            info.print_error(f" Hi {uname} Sorry we could not create account since this username exist")
            return
        
        randuid = uuid.uuid4().hex
        
        data = {
            "uid": randuid[0:8],
            "uname": '-'.join(uname.strip().capitalize().split(' ')),
            "password":  password
        }
        balancesdata = {
            "b_uid": randuid[0:8]
        }

        tokeinid = {'token_id': 7902}

        self.oneconn.insert_records('users',data)
        response = self.oneconn.insert_records('balances',balancesdata)

        inf = self.oneconn.select_records('decentralized',tokeinid)


        current = inf[0]['token_qty']

        if(current > 556.3):
            giveaway = current * 0.01
            recivable = inf[0]['token_price'] * 0.05 + inf[0]['token_price']

            self.oneconn.update_records('balances',{'b_token': giveaway},balancesdata)

            tokensub =  {
                'token_qty': current-giveaway,
                'token_price': recivable
            }

            self.oneconn.update_records('decentralized',tokensub,tokeinid)
            info.print_info(f"Hi {uname} you've Received Extra {giveaway:.4f}token worth ${recivable:.2f}")
        else:
            info.print_error(f"Sorry {uname} No token available for now")

        if response[0]['status']:
            info.print_success(F"Account created successfully for {uname}")
        else:
            print(F"Error: {response.error}")

    def see_users(self):
        users = self.oneconn.select_records('users')
        if len(users) > 0:
            info.print_info(f" \n All Token-Trader Users-> {len(users)}")
            display.generate_table(users)
            pass

        else:
            info.print_success("Opps Seems you'll be our first User If you Create an Account")

    def see_market():
        print("market")
        pass
    def see_trans():
        print("all trans")


