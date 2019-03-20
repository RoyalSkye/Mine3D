import database
import user as u

username = "skye"
password = "123456"
usertmp = database.getUserByusername(username, password)
if usertmp:
    print("login successfully!")
    userinfo = usertmp[0]
    # (1, 'skye', '123456', 'a@qq.com', 'admin', 'mine1')
    u.user.id = userinfo[0]
    u.user.username = userinfo[1]
    u.user.password = userinfo[2]
    u.user.email = userinfo[3]
    u.user.identify = userinfo[4]
    u.user.region = userinfo[5]
else:
    print("username or password is wrong!")

