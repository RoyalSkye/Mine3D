import pymysql

def gerConnection():
    db = pymysql.connect(host="localhost", user="root", password="rx806090733wx", db="qt", port=3306)
    return db, db.cursor()

# def querymyqt():
#     # 打开数据库连接, 使用cursor()方法获取操作游标
#     db, cur = gerConnection()
#
#     # 1.查询操作
#     # 编写sql 查询语句
#     sql = "select * from user"
#     try:
#         cur.execute(sql)  # 执行sql语句
#
#         results = cur.fetchall()  # 获取查询的所有记录
#         print("id", "username", "password")
#         # 遍历结果
#         for row in results:
#             id = row[0]
#             username = row[1]
#             password = row[2]
#             print(id, username, password)
#     except Exception as e:
#         raise e
#     finally:
#         cur.close()
#         db.close()
#     return results

def getminedata():
    db, cur = gerConnection()
    sql = "select * from minedata"
    try:
        cur.execute(sql)
        results = cur.fetchall()
    except Exception as e:
        raise e
    finally:
        cur.close()
        db.close()
    return results

def gettrainingdata():
    db, cur = gerConnection()
    sql = "select * from trainingdata"
    try:
        cur.execute(sql)
        results = cur.fetchall()
    except Exception as e:
        raise e
    finally:
        cur.close()
        db.close()
    return results

def insertminedata(data):
    db, cur = gerConnection()
    try:
        sql = "insert into minedata(data1, data2, data3, data4) values(%f, %f, %f, %f)" % (data[1], data[2], data[3], data[4])
        # print(type(data[1]))
        cur.execute(sql)  # data[1:]
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cur.close()
        db.close()

def inserttrainingdata(data):
    db, cur = gerConnection()
    try:
        sql = "insert into trainingdata(data1, data2, data3, data4) values(%f, %f, %f, %f)" % (data[1], data[2], data[3], data[4])
        # print(type(data[1]))
        cur.execute(sql)  # data[1:]
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cur.close()
        db.close()

def getUserByusername(username, password):  # for login
    db, cur = gerConnection()
    # sql = "select * from user where username = '%s'" % (username)
    # print(sql)
    try:
        # cur.execute(sql)
        row_count = cur.execute("select * from user where username = %s and password = %s", (username, password))  # 防止SQL注入
        print(row_count)
        results = cur.fetchall()
        print(results)
        return results
    except Exception as e:
        raise e
    finally:
        cur.close()
        db.close()