
class User:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.password = ""
        self.email = ""
        self.identify = ""
        self.region = ""
        self.smtpserver = ""
        self.emailpwd = ""
        self.port = 0

    def setUser(self, userinfo):
        self.id = userinfo[0]
        self.username = userinfo[1]
        self.password = userinfo[2]
        self.email = userinfo[3]
        self.identify = userinfo[4]
        self.region = userinfo[5]
        self.smtpserver = userinfo[6]
        self.emailpwd = userinfo[7]
        self.port = userinfo[8]

    def setUser1(self, id="", username="", password="", email="", identify="", region="", smtpserver="", emailpwd="", port=""):
        if id:
            self.id = id
        if username:
            self.username = username
        if email:
            self.email = email
        if password:
            self.password = password
        if identify:
            self.identify = identify
        if region:
            self.region = region
        if smtpserver:
            self.smtpserver = smtpserver
        if emailpwd:
            self.emailpwd = emailpwd
        if port:
            self.port = port

    # def getUser(id="", username="", password="", email="", identify="", region="", smtpserver="", emailpwd="", port=""):
    #     return User().setUser1(id=id, username=username, password=password, email=email, identify=identify, region=region, smtpserver=smtpserver, emailpwd=emailpwd, port=port)


user = User()

