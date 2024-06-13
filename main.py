from  lib.logics  import *

systemaction  = system_actions.SystemAction
useraction  = user_actions.UserActions


def Main():
    print("***Welcome to Token Trader***")
    print("------------------------------")
    useraction.display_token()
    useraction.user_menu()

    # # username = input("Enter Username >>")
    # # password = input("Enter Password >>")

    # systemaction.create_user("Mary1", "mary12345")
    # systemaction.create_user("Mary2", "mary12345")
    # systemaction.create_user("Mary3", "mary12345")
    # systemaction.create_user("Mary4", "mary12345")
    # systemaction.create_user("Mary5", "mary12345")
    systemaction.create_user("boscowswrf", "mary12345")


    # # username = input("Enter Username >>")
    # # password = input("Enter Password >>")
    # # useraction.confirm_login(username,password)
    users = useraction()
    users.confirm_login("boscowswrf", "mary12345")
    users.see_personal()
    # # indata = useraction.select_records('users')

    # systemaction.see_users()


    # for val in indata:
    #     print(val)


if __name__ == "__main__":
    Main()

