from lib.backend.connection import DbHandler
import uuid 

class SystemAction(DbHandler):
    def __init__(self):
        super().__init__()
    
    #  create user
    def create_user(uname,password):
        if not uname or not password:
            print("fields cant be empty")
            return
        confirmusers = DbHandler().select_records('users',{"uname": uname})[0]['staus']
        if confirmusers:
            retrun 
        
        randuid = uuid.uuid4().hex
        
        data = {
            "uid": randuid[0:8],
            "uname": '-'.join(uname.strip().capitalize().split(' ')),
            "password":  password
        }
        balancesdata = {
            "b_uid": randuid[0:8]
        }

        DbHandler().insert_records('users',data)
        response = DbHandler().insert_records('balances',balancesdata)

        if response[0]['status']:
            print(F"Account created successfully for {uname}")
        else:
            print(F"Error: {response.error}")

    #  delete users
    def delete_user(uid):
        if not uid:
            print("fields cant be empty")
            return
        
        where = {
            "uid": uid
        }
        
        response = DbHandler().delete_records('users',where)
        
        if response[0]['status']:
            print(F"Account deleted successfully for {uid}")
        else:
            print(F"Error: {response.error}")

