from  lib.logics  import *
from utils import * 


systemaction  = system_actions.SystemAction()
useraction  = user_actions.UserActions
users = useraction()

menudata = [
    {"arrow": ">**", "command": "create", "description": "Create Account", "func": "create_user"},
    {"arrow": ">**", "command": "summary", "description": "See current Inflation", "func": "display_token"},
    {"arrow": ">**", "command": "login", "description": "Login To Account", "func": "confirm_login"},
    {"arrow": ">**", "command": "view_market", "description": "View Market Analysis", "func": "see_market"},
    {"arrow": ">**", "command": "view_all_users", "description": "See all users", "func": 'see_users'},
    {"arrow": ">**", "command": "view_all_trans", "description": "See all transactions", "func": 'see_trans'},
    {"arrow": ">**", "command": "view_acc", "description": "Your Account Details", "func": 'see_personal'},
    {"arrow": ">**", "command": "buy_token", "description": "Buy Tokens From Market", "func": "buy_tokens"},
    {"arrow": ">**", "command": "sell_token", "description": "Release Tokens to Market", "func": "sell_tokens"},
    {"arrow": ">**", "command": "send_token", "description": "Send your Tokens to A user", "func": "send_tokens"},
    {"arrow": ">**", "command": "delete_acc", "description": "Delete Your Account", "func": 'kill'},
    {"arrow": ">**", "command": "logout", "description": "Logout From CLI-Application", "func": 'confirm_logout'},
    {"arrow": ">**", "command": "exit", "description": "Exit Application", "func": "Terminate"}
]

def Main():
    print(info.print_r_info("*** Welcome to Token Trader ***"))
    print("------------------------------ \n")
    users.display_token()
    useraction.user_menu(menudata)

    while True:
        invalue = input("\n Execute a Command from the table['command'] or type menu>> ").lower().strip()
        found = False

        if invalue == 'menu':
            useraction.user_menu(menudata)
        elif invalue == 'exit':
                users.confirm_logout()
                systemaction.close_connection()
                info.print_error("Exiting the cli-app...")
                break
        else:
            for menu_item in menudata:
                if invalue == menu_item['command'] and invalue != 'exit':
                    func_name = menu_item['func']

                    if hasattr(useraction, func_name):
                        func = getattr(users, func_name)
                        found = True    
                    elif hasattr(systemaction, func_name):
                        func = getattr(systemaction, func_name)
                        found = True    
            if found:
                func()
            else:
                useraction.user_menu(menudata)
                info.print_info(F"Command >> {invalue} not available in the table please retype")


if __name__ == "__main__":
    Main()

