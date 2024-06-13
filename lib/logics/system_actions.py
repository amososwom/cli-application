import uuid 

from lib.backend.connection import DbHandler
from utils import * 

class SystemAction(DbHandler):
    def __init__(self):
        super().__init__()
    
    #  create user
    def create_user(uname,password):
        if not uname or not password:
            info.print_error("fields cant be empty")
            return
        confirmusers = DbHandler().select_records('users',{"uname": uname})
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

        DbHandler().insert_records('users',data)
        response = DbHandler().insert_records('balances',balancesdata)

        inf = DbHandler().select_records('decentralized',tokeinid)


        current = inf[0]['token_qty']

        if(current > 556.3):
            giveaway = current * 0.01
            recivable = inf[0]['token_price'] * 0.02 + inf[0]['token_price']

            DbHandler().update_records('balances',{'b_token': giveaway},balancesdata)

            tokensub =  {
                'token_qty': current-giveaway,
                'token_price': recivable
            }

            DbHandler().update_records('decentralized',tokensub,tokeinid)
            info.print_success(f"Hi {uname} you've Received Extra {giveaway:.4f}token worth ${recivable:.2f}")
        else:
            info.print_error(f"Sorry {uname} No token available for now")

        if response[0]['status']:
            info.print_success(F"Account created successfully for {uname}")
        else:
            print(F"Error: {response.error}")

    #  delete users
    def delete_user(uid):
        if not uid:
            info.print_error("fields cant be empty")
            return
        
        where = {
            "uid": uid
        }
        
        response = DbHandler().delete_records('users',where)
        
        if response[0]['status']:
            info.print_success(F"Account deleted successfully for {uid}")
        else:
            info.print_error(F"Error: {response.error}")
    
    def see_users():
        users = DbHandler().select_records('users')
        if len(users) > 0:
            print(f" \n All Token-Trader {len(users)} Users")
            display.generate_table(users)
            pass

        else:
            info.print_success("Opps Seems you'll be our first User If you Create an Account")




