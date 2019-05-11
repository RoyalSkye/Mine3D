class Helper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

    @staticmethod
    def generateTimestamp():
        import time
        t = time.time()
        timestamp = int(t)
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%Y%m%d_%H%M%S", timeArray)
        return otherStyleTime

    @staticmethod
    def getdatetime():
        import time
        t = time.time()
        timestamp = int(t)
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%Y.%m.%d", timeArray)
        return otherStyleTime

    @staticmethod
    def validatepath(path):
        import os
        path = path.strip()
        isExists = os.path.exists(path)
        return isExists

    @staticmethod
    def readpcd(file_path):
        # import pointcloud dataset to Excel

        file_path = '/Users/skye/Desktop/s_MineOne.pcd'
        with open(file_path) as file_object:
            # contents = file_object.read()
            # for line in file_object:
            #     print(line.rstrip())
            lines = file_object.readlines()
        data = []
        for line in lines[11:]:
            # print(line.rstrip())
            data.append(line.rstrip())
        return data

    @staticmethod
    def writeToexcel(file_path):
        import xlwt
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('PointData')
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = 'Times New Roman'
        font.bold = False  # 黑体
        font.underline = False  # 下划线
        font.italic = False  # 斜体字
        style.font = font  # 设定样式

        file_path = '/Users/skye/Desktop/s_MineOne.pcd'
        data = Helper.readpcd(file_path)
        # print(type(data))

        worksheet.write(0, 0, 'x', style)
        worksheet.write(0, 1, 'y', style)
        worksheet.write(0, 2, 'z', style)
        worksheet.write(0, 3, 'intensity', style)

        for i in range(len(data)):
            a = data[i].split()
            for j in range(len(a)):
                worksheet.write(i + 1, j, float(a[j]), style)  # 带样式的写入

        workbook.save('/Users/skye/Desktop/pointcloud.xls')  # 保存文件
        print("write to file completed!")

    @staticmethod
    def ReadPCAdata(filepath):
        import xlrd
        filepath = '/Users/skye/Desktop/铁矿石132+围岩.xls'
        data = xlrd.open_workbook(filepath)
        table = data.sheet_by_index(0)
        samples = table.row_values(0)[1:]
        # print(samples)

        pcadata = [[] for row in range(3, table.nrows)]
        # print(len(pcadata))
        n = 0
        for i in range(3, table.nrows):
            pcadata[n] = table.row_values(i)[1:]
            n = n + 1
        # print(pcadata)

        dataset = {'waves': len(pcadata), 'samples': samples, 'pcadata': pcadata}
        return dataset

    @staticmethod
    def update_user(mainself, id):
        import database
        from PyQt5.QtWidgets import QMessageBox
        try:
            user = database.getUserByid(id)
            if user[0][4] == 'admin':
                reply = QMessageBox.critical(mainself, 'Message', '<font color="black">无权限修改管理员资料！', QMessageBox.Ok,
                                             QMessageBox.Ok)
                mainself.inituser_manage_table()
                return
            else:
                row = mainself.user_manage.rowCount()
                userinfo = []
                for r in range(row):
                    if mainself.user_manage.item(r, 0).text() == str(id):
                        for i in range(1, 6):
                            userinfo.append(mainself.user_manage.item(r, i).text())
                        print(userinfo)
                        break
                res = database.updateUser(userinfo, id)
        except:
            reply = QMessageBox.critical(mainself, 'Message', '<font color="black">数据更新失败！', QMessageBox.Ok,
                                        QMessageBox.Ok)
            print("update user catch exception")
        else:
            reply = QMessageBox.information(mainself, 'Message', '<font color="black">数据修改成功！', QMessageBox.Ok,
                                            QMessageBox.Ok)
        finally:
            mainself.inituser_manage_table()

    @staticmethod
    def delete_user(mainself, id):
        import database
        from PyQt5.QtWidgets import QMessageBox
        try:
            user = database.getUserByid(id)
            # print(user[0][4])
            if user[0][4] == 'admin':
                reply = QMessageBox.critical(mainself, 'Message', '<font color="black">无权限删除管理员！', QMessageBox.Ok,
                                             QMessageBox.Ok)
                mainself.inituser_manage_table()
                return
            else:
                res = database.deleteuser(id)
        except:
            reply = QMessageBox.critical(mainself, 'Message', '<font color="black">数据删除失败！', QMessageBox.Ok,
                                        QMessageBox.Ok)
            print("delete user catch exception")
        finally:
            mainself.inituser_manage_table()

global modelversion
modelversion = "light"
global threadpool
threadpool = []
global predict_result
predict_result = []
global data_path
data_path = ''
global rownum
rownum = 0
global tensor
tensor = 0