import database

class User:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.password = ""
        self.email = ""
        self.identify = ""
        self.region = ""

    def setUser(self, userinfo):
        self.id = userinfo[0]
        self.username = userinfo[1]
        self.password = userinfo[2]
        self.email = userinfo[3]
        self.identify = userinfo[4]
        self.region = userinfo[5]

user = User()

