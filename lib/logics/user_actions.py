from lib.backend.connection import DbHandler


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

            self.uid = response[1][0]
            self.uname = response[1][1]
            print(
                self.uid,
                self.uname
            )
            print("Yeah your data was found and logged in")
        else:
            print("Opps your Credentials are Wrong")


# see available tokens


#see market token

# see balances

#see his transactions


# send token


#buy tokens


# sell token


# cancel trade


#view personal history


#delete account