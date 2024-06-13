from  lib.logics  import *
from utils import * 



systemaction  = system_actions.SystemAction
useraction  = user_actions.UserActions


def Main():
    info.print_info("*** Welcome to Token Trader ***}")
    print("------------------------------ \n")
    useraction.display_token()
    useraction.user_menu()

    systemaction.create_user("Mary", "mary12345")
    users = useraction()
    users.confirm_login("Mary", "mary12345")
    users.see_personal()


    # while True:
    #     invalue = input("Type a command from the table >>").lower().strip()

    #     if invalue in user_actions.menudata['command']:
    #         if invalue == "create":
    #             username = input("Enter Username >>")
    #             password = input("Enter Password >>")
    #             systemaction.create_user(username, password)
    #         elif invalue == "login":
    #             username = input("Enter Username >>")
    #             password = input("Enter Password >>")
    #             useraction.confirm_login(username,password)
    #         elif invalue == "view_users":
    #             systemaction.see_users()
    #         elif invalue == "view_acc":
    #             useraction.see_personal()
    #         elif invalue == "delete_acc":
    #             useraction.delete_user()
    #         elif invalue == "logout":
    #             useraction.confirm_logout()
    #         elif invalue == "exit":
    #             break



    # if invalue == "create":
    #     username = input("Enter Username >>")
    #     password = input("Enter Password >>")
    #     systemaction.create_user(username, password)

    



    # for val in user_actions.menudata:
    # # useraction.confirm_login(username,password)
    #     print(val)

    



    # # username = input("Enter Username >>")
    # # password = input("Enter Password >>")

    # systemaction.create_user("Mary1", "mary12345")
    # systemaction.create_user("Mary2", "mary12345")
    # systemaction.create_user("Mary3", "mary12345")
    # systemaction.create_user("Mary4", "mary12345")
    # systemaction.create_user("Mary5", "mary12345")
    # systemaction.create_user("ww", "mary12345")


    # # username = input("Enter Username >>")
    # # password = input("Enter Password >>")
    # users = useraction()
    # # indata = useraction.select_records('users')

    # systemaction.see_users()


    # for val in indata:
    #     print(val)


if __name__ == "__main__":
    Main()

