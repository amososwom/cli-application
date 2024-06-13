from  lib.logics  import *

systemaction  = system_actions.SystemAction
useraction  = user_actions.UserActions()


def Main():
    print("Welcome to the Token Trader")

    print("-------------------------------")

    # username = input("Enter Username >>")
    # password = input("Enter Password >>")
    systemaction.create_user("garfield",'password')


    # username = input("Enter Username >>")
    # password = input("Enter Password >>")
    # useraction.confirm_login(username,password)
    useraction.confirm_login("Mary", "mary12345")


if __name__ == "__main__":
    Main()

