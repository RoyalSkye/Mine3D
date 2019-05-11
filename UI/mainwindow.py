import os, xlrd
import user, database, helper, generateDocx
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI.quicreator import Ui_QUICreator

class MainWindow(QMainWindow, Ui_QUICreator):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.action_dark.triggered.connect(self.Todarkmodel)
        self.action_light.triggered.connect(self.Tolightmodel)
        self.action_quit.triggered.connect(self.quit)
        self.action_refresh.triggered.connect(self.refresh)
        self.action_changeuser.triggered.connect(self.changeuser)

        # # simulate login
        # userinfo = database.getUserByusername("skye", "123456")
        # if userinfo:
        #     user.user.setUser(userinfo[0])
        # else:
        #     print("用户名密码错误!")

        # 判断用户权限，如果为普通用户，则将groupbox设置为不可选状态
        if(user.user.identify == "admin"):
            self.inituser_manage_table()
        else:
            self.MailgroupBox.setChecked(False)
            self.MailgroupBox.toggled.connect(self.setuncheckable)
            self.groupBox_14.setChecked(False)
            self.groupBox_14.toggled.connect(self.setuncheckable)

        # self.initTableWidget()
        # self.initfont()
        self.initEmailBox()
        self.initreceiver()
        self.initTable_dataset()
        self.initDoc_2_file()
        self.attachList = []  # 附件列表
        self.initemailsetting()
        self.initcover()
        self.initdoc_1_tableview()
        # self.initdoc_2_table()
        # global variables
        self.doc_3_picpath1 = ""
        self.doc_3_picpath2 = ""

        self.animation1 = QPropertyAnimation(self, b"windowOpacity")
        self.animation1.setDuration(500)
        self.animation1.setStartValue(0)
        self.animation1.setEndValue(1)
        self.animation1.start()

        # import Visualization.MyGL as mg
        # self.objFile = self.openGLWidget = mg.OpenGLWidget(self.centralwidget)

    # def initfont(self):
    #     font = QtGui.QFont()
    #     font.setPointSize(12)
    #     self.tableWidget.setFont(font)
    #     self.importFile.setFont(font)
    #     self.label.setFont(font)
    #     # self.label_4.setFont(font)
    #     self.training.setFont(font)

    def inituser_manage_table(self):
        import database
        dataset = database.getAlluser1()
        # print(dataset)
        rowNum = 0
        for info in dataset:
            rowNum = rowNum + 1
        colNum = 8
        self.user_manage.setRowCount(rowNum)
        self.user_manage.setColumnCount(colNum)
        attributes = ['id', 'username', 'password', 'email', 'identity', 'region', 'update', 'delete']
        self.user_manage.setHorizontalHeaderLabels(attributes)
        self.user_manage.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.user_manage.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(0, rowNum):
            for j in range(0, colNum):
                if j == 6:
                    btn = self.GenerateupdateBtn(int(dataset[i][0]))
                    self.user_manage.setCellWidget(i, j, btn)
                    # self.user_manage.setCellWidget(i, j, self.GenerateBtn(str(i)))
                    continue
                if j == 7:
                    btn = self.GeneratedeleteBtn(int(dataset[i][0]))
                    self.user_manage.setCellWidget(i, j, btn)
                    continue
                item = QtWidgets.QTableWidgetItem(str(dataset[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                if j == 0:
                    item.setFlags(~item.flags())
                self.user_manage.setItem(i, j, item)

    def GenerateupdateBtn(self, id):
        userinfo = []
        updateBtn = QtWidgets.QPushButton('update')
        updateBtn.setStyleSheet('''text-align : center; background-color : DarkSeaGreen; color:white;''')
        updateBtn.clicked.connect(lambda: helper.Helper.update_user(self, id))
        # viewBtn.clicked.connect(lambda: self.user_manage(clientid))  # issue: TypeError: 'QTableWidget' object is not callable
        return updateBtn

    def GeneratedeleteBtn(self, id):
        deleteBtn = QtWidgets.QPushButton('delete')
        deleteBtn.setStyleSheet('''text-align : center; background-color : red; color:white;''')
        deleteBtn.clicked.connect(lambda: helper.Helper.delete_user(self, id))
        return deleteBtn

    # def user_manage(self, userinfo):
    #     print("test")
    #     print(userinfo)

    def initcover(self):
        self.doc_heading.setText('露天采场矿岩与品位信息报告')
        self.doc_company.setText('露天采场矿岩股份有限公司')
        self.doc_code.setText(helper.Helper.generateTimestamp())
        self.doc_reporter.setText(user.user.username)
        self.doc_date.setText(helper.Helper.getdatetime())
        self.doc_type.setText('常规更新')
        self.doc_filename.setText('demo1')
        # initCatalog
        self.doc_content1.setText("资料审查报告")
        self.doc_content2.setText("数据图表")
        self.doc_content3.setText("数据分析")
        self.doc_content4.setText("总结")

    def initdoc_1_tableview(self):
        self.model = QStandardItemModel(10, 4)
        tmp = ["矿区名称", "矿区编号", "管理单位", "单位编号", "操作人", "操作类型", "原始数据(个)", "新增数据(个)", "误差(更新前)", "准确率(更新前)",
               "误差(更新后)", "准确率(更新后)", "上次检验日期", "上次检验记录编号", "原始资料审查问题记载", "历次定期检验问题记载", "审核日期(年/月/日)"]
        self.doc_1_tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.doc_1_tableview.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.doc_1_tableview.setSpan(7, 1, 1, 3)
        self.doc_1_tableview.setSpan(8, 1, 1, 3)
        self.doc_1_tableview.setSpan(9, 0, 1, 2)
        self.doc_1_tableview.setSpan(9, 2, 1, 2)
        count = 0
        for row in range(7):
            for column in range(2):
                item = QStandardItem(tmp[count])
                count += 1
                item.setFlags(Qt.NoItemFlags)
                item.setTextAlignment(Qt.AlignCenter)
                # !!! if change to dark model, change to qt.white
                # print(helper.modelversion)
                if helper.modelversion == "light":
                    item.setForeground(Qt.black)
                self.model.setItem(row, 2*column, item)
        for row in range(7, 10):
            item = QStandardItem(tmp[count])
            count += 1
            item.setFlags(Qt.NoItemFlags)
            item.setTextAlignment(Qt.AlignCenter)
            if helper.modelversion == "light":
                item.setForeground(Qt.black)
            self.model.setItem(row, 0, item)
        self.doc_1_tableview.setModel(self.model)

        # index = self.model.index(0, 0, QModelIndex())
        # str1 = index.data()
        # print(str1)

    def initTableWidget(self, file_path):
        import pandas as pd
        df = pd.read_csv(file_path, header=None)
        # print(df)
        dataset = df.values[0:5][:,1:].transpose()[:,[0,2,3,4,1]]
        rowNum = dataset.shape[0]
        colNum = dataset.shape[1]
        # print(dataset)
        self.tableWidget.setRowCount(rowNum)
        self.tableWidget.setColumnCount(colNum)
        self.tableWidget.setHorizontalHeaderLabels(['样本编号', 'x', 'y', 'z', '所属类别'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(0, rowNum):
            for j in range(0, colNum):
                item = QtWidgets.QTableWidgetItem(str(dataset[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

    def initTable_dataset(self):
        from PyQt5.QtWidgets import QFileSystemModel
        model = QFileSystemModel()
        dir = os.getcwd() + '/data/ml_dataset'
        model.setRootPath(dir)
        self.table_dataset.setModel(model)
        self.table_dataset.setColumnWidth(0, 200)
        self.table_dataset.setColumnWidth(1, 150)
        self.table_dataset.setColumnWidth(2, 150)
        self.table_dataset.setRootIndex(model.index(dir))
        self.table_dataset.doubleClicked.connect(lambda: self.showdataset(0))

    def initDoc_2_file(self):
        from PyQt5.QtWidgets import QFileSystemModel
        model = QFileSystemModel()
        dir = os.getcwd() + '/data/ml_dataset'
        model.setRootPath(dir)
        self.doc_2_file.setModel(model)
        self.doc_2_file.setColumnWidth(0, 200)
        self.doc_2_file.setColumnWidth(1, 100)
        self.doc_2_file.setColumnWidth(2, 100)
        self.doc_2_file.setRootIndex(model.index(dir))
        self.doc_2_file.doubleClicked.connect(lambda: self.showdataset(1))

    def showdataset(self, whichone):
        print(whichone)
        if whichone == 0:
            index = self.table_dataset.currentIndex()
        else:
            index = self.doc_2_file.currentIndex()
        model = index.model()
        file_path = model.filePath(index)
        import re
        result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', file_path)
        if '.csv' in result:
            try:
                if whichone == 0:
                    self.initTableWidget(file_path)
                else:
                    self.initdoc_2_table(file_path)
            except:
                print("表格生成: catch exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">表格生成错误，请检查数据格式！', QMessageBox.Ok,
                                            QMessageBox.Ok)
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">不支持的文件格式！', QMessageBox.Ok, QMessageBox.Ok)

    def initEmailBox(self):
        from PyQt5.QtWidgets import QFileSystemModel
        model = QFileSystemModel()
        dir = '/'  # mac根路径
        model.setRootPath(dir)
        self.attachment.setModel(model)
        self.attachment.setColumnWidth(0, 300)
        self.attachment.setColumnWidth(1, 100)
        self.attachment.setColumnWidth(2, 100)
        # self.attachment.setColumnHidden(1, True)
        self.attachment.setRootIndex(model.index(dir))
        self.attachment.doubleClicked.connect(self.getpath)

    def initreceiver(self):
        # self.receiver = QTreeWidget()
        self.receiver.clear()
        self.receiver.setColumnCount(2)
        self.receiver.setColumnWidth(0,300)
        self.receiver.setHeaderLabels(['Username', 'Email'])
        root1 = QTreeWidgetItem(self.receiver)
        root2 = QTreeWidgetItem(self.receiver)
        root1.setText(0, 'Administrator')
        root2.setText(0, 'Staff')
        # get userinfo
        userinfo = database.getAlluser()
        for u in userinfo:
            child = QTreeWidgetItem()
            child.setText(0, u[0])
            child.setText(1, u[1])
            child.setCheckState(0, Qt.Checked)
            if u[-1] == 'admin':
                root1.addChild(child)
            elif u[-1] == 'staff':
                root2.addChild(child)
        self.receiver.expandAll()

    def initemailsetting(self):
        if user.user.smtpserver:
            self.smtpserver.setText(user.user.smtpserver)
        if user.user.port:
            self.port.setText(str(user.user.port))
        if user.user.email:
            self.emailsender.setText(user.user.email)
        if user.user.emailpwd:
            self.emailpwd.setText(user.user.emailpwd)

    def initprediction_table(self, result):
        # print(result)
        self.prediction_table.setRowCount(result.shape[0])
        self.prediction_table.setColumnCount(result.shape[1])
        self.prediction_table.setHorizontalHeaderLabels(['样本编号', 'x', 'y', 'z', '预测结果'])
        self.prediction_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.prediction_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(0, result.shape[0]):
            for j in range(0, result.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(result[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.prediction_table.setItem(i, j, item)

    def initdoc_2_table(self, file_path):
        import pandas as pd
        df = pd.read_csv(file_path, header=None)
        # print(df)
        dataset = df.values[0:5][:, 1:].transpose()[:, [0, 2, 3, 4, 1]]
        rowNum = dataset.shape[0]
        colNum = dataset.shape[1]
        self.doc_2_table.setRowCount(rowNum)
        self.doc_2_table.setColumnCount(colNum)
        self.doc_2_table.setHorizontalHeaderLabels(['样本编号', 'x', 'y', 'z', '所属类别'])
        self.doc_2_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.doc_2_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(0, rowNum):
            self.check = QtWidgets.QTableWidgetItem()
            self.check.setCheckState(Qt.Checked)
            self.check.setText(str(dataset[i][0]))
            self.doc_2_table.setItem(i, 0, self.check)
            for j in range(1, colNum):
                item = QtWidgets.QTableWidgetItem(str(dataset[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.doc_2_table.setItem(i, j, item)
        helper.data_path = file_path
        helper.rownum = rowNum
        # minedata = database.getminedata()
        # if minedata:
        #     self.doc_2_table.setRowCount(len(minedata))
        #     self.doc_2_table.setColumnCount(len(minedata[0]))
        #     self.doc_2_table.setHorizontalHeaderLabels(['checked', 'data1', 'data2', 'data3', 'data4'])
        #     self.doc_2_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #     self.doc_2_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #     # self.doc_2_table.verticalHeader().setVisible(False)
        #     count = 1
        #     for i in range(0, len(minedata)):
        #         self.check = QtWidgets.QTableWidgetItem()
        #         self.check.setCheckState(Qt.Checked)
        #         self.check.setText(str(count))
        #         count += 1
        #         # self.check.setTextAlignment(Qt.AlignCenter)
        #         # self.check.setBackground(Qt.black)
        #         self.doc_2_table.setItem(i, 0, self.check)
        #         for j in range(1, len(minedata[i])):
        #             item = QtWidgets.QTableWidgetItem(str(minedata[i][j]))
        #             item.setTextAlignment(Qt.AlignCenter)
        #             self.doc_2_table.setItem(i, j, item)
        # else:
        #     print("data is null!")


    # 槽函数会执行2次if不写装饰器@pyqtSlot()
    @pyqtSlot()
    def on_importFile_clicked(self):
        # projectpath = os.getcwd()
        rootpath = '/'
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选择csv数据文件", rootpath, "(*.csv)")
        if len(filename) == 0:
            return
        self.path.setText(filename)

    @pyqtSlot()
    def on_button2_1_clicked(self):
        rootpath = '/'
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选择点云数据文件", rootpath, "(*.txt;*.csv)")
        if len(filename) == 0:
            return
        self.filepath2_1.setText(filename)

    @pyqtSlot()
    def on_update3d_clicked(self):
        import pandas as pd
        data_path = self.filepath2_1.text()
        if data_path:
            df = pd.read_csv(data_path, sep=' ', header=None)
            # print(df)
            rowNum = df.shape[0]  # 不包括表头
            colNum = df.columns.size
            if colNum != 3:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">数据格式错误！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                try:
                    pointcloud = df.values
                    print(pointcloud)
                    # pass pointcloud to 3d virtualization with try except
                except:
                    print("update3d catch exception")
                    reply = QMessageBox.warning(self, 'Message', '<font color="black">生成建模错误，请检查数据！', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    import shutil
                    shutil.copy(data_path, "./data/pointcloud/点云数据.csv")
                    self.pointcloud_status.setText("建模生成完毕！")
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">文件路径错误！', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_button2_2_clicked(self):
        if self.filepath2_3.text():
            reply = QMessageBox.warning(self, 'Message', '<font color="black">预测与测试只能选择一个，请删除另一个路径！', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.filepath2_3.clear()
            return
        rootpath = '/'
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选择光谱数据文件", rootpath, "(*.csv)")
        if len(filename) == 0:
            return
        self.filepath2_2.setText(filename)

    @pyqtSlot()
    def on_button2_3_clicked(self):
        if self.filepath2_2.text():
            reply = QMessageBox.warning(self, 'Message', '<font color="black">预测与测试只能选择一个，请删除另一个路径！', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.filepath2_2.clear()
            return
        rootpath = '/'
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选择光谱数据文件", rootpath, "(*.csv)")
        if len(filename) == 0:
            return
        self.filepath2_3.setText(filename)

    @pyqtSlot()
    def on_virtualization_clicked(self):
        if len(helper.predict_result) != 0:
            print(helper.predict_result)
            # pass helper.predict_result to 3d virtualization with try except
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">尚未预测任何数据！', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_prediction_clicked(self):
        self.precision.clear()
        path1 = self.filepath2_2.text()
        path2 = self.filepath2_3.text()
        if path1:
            path = path1
            flag = 1
        else:
            path = path2
            flag = 2
        if path:
            try:
                from ml_data import SVM
                map = SVM.prediction(path, './model/PCA+SVM/svm.pkl', 1)
            except:
                print("prediction catch exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">未训练该类模型或预测数据错误！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                result = map["result"]
                import shutil
                shutil.copy(path, "./data/ml_dataset/" + "PCA+SVM_" + "预测数据集.csv")
                img9 = QImage("./images/prediction/img1.png")
                size = QSize(320, 240)
                pixmap = QPixmap.fromImage(img9.scaled(size, Qt.IgnoreAspectRatio))
                self.pre_pic_1.resize(320, 240)
                self.pre_pic_1.setPixmap(pixmap)
                img10 = QImage("./images/prediction/img2.png")
                size = QSize(320, 240)
                pixmap = QPixmap.fromImage(img10.scaled(size, Qt.IgnoreAspectRatio))
                self.pre_pic_2.resize(320, 240)
                self.pre_pic_2.setPixmap(pixmap)
                self.initprediction_table(result)
                helper.predict_result = result
                if flag == 2:  # 测试，显示测试集准确率
                    text = "模型在测试集上的准确率为: " + str(map["accuracy"])
                    self.precision.setText(text)
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">文件路径错误！', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_prediction1_clicked(self):
        self.precision.clear()
        path1 = self.filepath2_2.text()
        path2 = self.filepath2_3.text()
        if path1:
            path = path1
            flag = 1
        else:
            path = path2
            flag = 2
        if path:
            try:
                from ml_data import SVM
                map = SVM.prediction(path, './model/LDA+SVM/svm.pkl', 2)
            except:
                print("prediction catch exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">未训练该类模型或预测数据错误！', QMessageBox.Ok,
                                            QMessageBox.Ok)
            else:
                result = map["result"]
                import shutil
                shutil.copy(path, "./data/ml_dataset/" + "LDA+SVM_" + "预测数据集.csv")
                img9 = QImage("./images/prediction/img1.png")
                size = QSize(320, 240)
                pixmap = QPixmap.fromImage(img9.scaled(size, Qt.IgnoreAspectRatio))
                self.pre_pic_1.resize(320, 240)
                self.pre_pic_1.setPixmap(pixmap)
                img10 = QImage("./images/prediction/img2.png")
                size = QSize(320, 240)
                pixmap = QPixmap.fromImage(img10.scaled(size, Qt.IgnoreAspectRatio))
                self.pre_pic_2.resize(320, 240)
                self.pre_pic_2.setPixmap(pixmap)
                self.initprediction_table(result)
                helper.predict_result = result
                if flag == 2:  # 测试，显示测试集准确率
                    text = "模型在测试集上的准确率为: " + str(map["accuracy"])
                    self.precision.setText(text)
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">文件路径错误！', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_prediction2_clicked(self):
        self.precision.clear()
        path1 = self.filepath2_2.text()
        path2 = self.filepath2_3.text()
        if path1:
            path = path1
            flag = 1
        else:
            path = path2
            flag = 2
        if path:
            try:
                from ml_data import tensorflow1
                map = tensorflow1.tensorflow_predict(path)
            except:
                print("prediction catch exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">未训练该类模型或预测数据错误！', QMessageBox.Ok,
                                            QMessageBox.Ok)
            else:
                result = map["result"]
                import shutil
                shutil.copy(path, "./data/ml_dataset/" + "LDA+ANN_" + "预测数据集.csv")
                img9 = QImage("./images/prediction/img1.png")
                size = QSize(320, 240)
                pixmap = QPixmap.fromImage(img9.scaled(size, Qt.IgnoreAspectRatio))
                self.pre_pic_1.resize(320, 240)
                self.pre_pic_1.setPixmap(pixmap)
                img10 = QImage("./images/prediction/img2.png")
                size = QSize(320, 240)
                pixmap = QPixmap.fromImage(img10.scaled(size, Qt.IgnoreAspectRatio))
                self.pre_pic_2.resize(320, 240)
                self.pre_pic_2.setPixmap(pixmap)
                self.initprediction_table(result)
                helper.predict_result = result
                if flag == 2:  # 测试，显示测试集准确率
                    text = "模型在测试集上的准确率为: " + str(map["accuracy"])
                    self.precision.setText(text)
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">文件路径错误！', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_training_clicked(self):
        filename = self.path.text()
        # newfilename = './data/' + helper.Helper.generateTimestamp() + '.csv'
        newfilename = './data/ml_dataset/training_tmp_dataset.csv'
        if filename == '' or not helper.Helper.validatepath(filename):
            reply = QMessageBox.warning(self, 'Message', '<font color="black">请选择正确的文件路径！', QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            import shutil
            try:
                shutil.copy(filename, newfilename)
            except:
                print("catch Exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">文件复制出现异常！', QMessageBox.Ok, QMessageBox.Ok)
                return
            else:
                # if import data successfully: 不阻塞主线程,否则需要等待pca+svm
                import threading
                if helper.threadpool:
                    reply = QMessageBox.warning(self, 'Message', '<font color="black">正在导入并训练数据中，请勿重复操作！', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    t1 = threading.Thread(target=self.trainingdata, args=(newfilename, 1))
                    t1.setDaemon(True)
                    t1.start()
                    helper.threadpool.append(t1.getName())
                    self.importStatus.setText("please wait for training ...")

    @pyqtSlot()
    def on_training1_clicked(self):
        filename = self.path.text()
        newfilename = './data/ml_dataset/training_tmp_dataset.csv'
        if filename == '' or not helper.Helper.validatepath(filename):
            reply = QMessageBox.warning(self, 'Message', '<font color="black">请选择正确的文件路径！', QMessageBox.Ok,
                                        QMessageBox.Ok)
            return
        else:
            import shutil
            try:
                shutil.copy(filename, newfilename)
            except:
                print("catch Exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">文件复制出现异常！', QMessageBox.Ok,
                                            QMessageBox.Ok)
                return
            else:
                # if import data successfully: 不阻塞主线程,否则需要等待lda+svm
                import threading
                if helper.threadpool:
                    reply = QMessageBox.warning(self, 'Message', '<font color="black">正在导入并训练数据中，请勿重复操作！',
                                                QMessageBox.Ok, QMessageBox.Ok)
                else:
                    t1 = threading.Thread(target=self.trainingdata, args=(newfilename, 2))
                    t1.setDaemon(True)
                    t1.start()
                    helper.threadpool.append(t1.getName())
                    self.importStatus.setText("please wait for training ...")

    @pyqtSlot()
    def on_training2_clicked(self):
        filename = self.path.text()
        newfilename = './data/ml_dataset/training_tmp_dataset.csv'
        if filename == '' or not helper.Helper.validatepath(filename):
            reply = QMessageBox.warning(self, 'Message', '<font color="black">请选择正确的文件路径！', QMessageBox.Ok,
                                        QMessageBox.Ok)
            return
        else:
            import shutil
            try:
                shutil.copy(filename, newfilename)
            except:
                print("catch Exception")
                reply = QMessageBox.warning(self, 'Message', '<font color="black">文件复制出现异常！', QMessageBox.Ok,
                                            QMessageBox.Ok)
                return
            else:
                # if import data successfully: 不阻塞主线程,否则需要等待lda+svm
                import threading
                if helper.threadpool:
                    reply = QMessageBox.warning(self, 'Message', '<font color="black">正在导入并训练数据中，请勿重复操作！',
                                                QMessageBox.Ok, QMessageBox.Ok)
                else:
                    t1 = threading.Thread(target=self.trainingdata, args=(newfilename, 3))
                    t1.setDaemon(True)
                    t1.start()
                    helper.threadpool.append(t1.getName())
                    self.importStatus.setText("please wait for training ...")

    @pyqtSlot()
    def on_clearflie_clicked(self):
        self.File.clear()
        self.attachList = []

    @pyqtSlot()
    def on_clearemail_clicked(self):
        self.MailContext.clear()
        self.head.setText('请输入标题')
        self.File.clear()
        self.initreceiver()
        self.initEmailBox()
        self.maillabel.setText('发送状态: ')
        self.attachList = []

    @pyqtSlot()
    def on_sendemail_clicked(self):
        from generateEmail import sendmail
        to = []
        rootcount = self.receiver.topLevelItemCount()
        for i in range(0, rootcount):
            root = self.receiver.topLevelItem(i)
            childcount = QTreeWidgetItem.childCount(root)
            for j in range(0, childcount):
                child = QTreeWidgetItem.child(root, j)
                if child.checkState(0) == Qt.Checked:
                    to.append(child.text(1))
        head = self.head.text()
        attachment = self.File.text()
        context = self.MailContext.toPlainText()
        # self.MailContext.document().findBlockByLineNumber(0).text()
        # print(to)
        # print(head)
        # print(attachment)
        # print(context)
        # print(self.attachList)
        if to and head:
            # pass
            msg = sendmail(to, head, self.attachList, context)
            self.maillabel.setText('发送状态: '+msg)
        else:
            self.maillabel.setText('发送状态: 收件人或标题为空！')

    @pyqtSlot()
    def on_accountsource_clicked(self):
        oldpwd = self.oldpwd.text()
        newpwd1 = self.newpwd1.text()
        newpwd2 = self.newpwd2.text()
        if user.user.password != oldpwd:
            self.accountstatus.setText("oldpassword is incorrect!")
        elif len(newpwd1) < 6 or len(newpwd2) < 6:
            self.accountstatus.setText("newpassword is too simple!")
        elif newpwd1 != newpwd2:
            self.accountstatus.setText("two newpasswords not the same!")
        elif user.user.password == newpwd1:
            self.accountstatus.setText("newpassword is the same as the old!")
        else:
            u = user.User()
            u.setUser1(id=user.user.id, password=newpwd1)
            user.user.setUser1(password=newpwd1)
            if database.updateUserpwd(u) == 1:
                self.accountstatus.setText("修改密码成功!")
            else:
                self.accountstatus.setText("MySQLError: 修改密码失败!")

    @pyqtSlot()
    def on_emailsource_clicked(self):
        smtpserver = self.smtpserver.text()
        port = self.port.text()
        sendemail = self.emailsender.text()
        emailpwd = self.emailpwd.text()
        if smtpserver and port and sendemail and emailpwd:
            u = user.User()
            u.setUser1(smtpserver=smtpserver, port=port, email=sendemail, emailpwd=emailpwd, id=user.user.id)
            user.user.setUser1(smtpserver=smtpserver, port=port, email=sendemail, emailpwd=emailpwd)
            if database.updateUserpwd(u) == 1:
                self.emailstatus.setText("修改成功!")
            else:
                self.emailstatus.setText("未进行任何修改 \nor MySQLError: 修改失败!")
        else:
            self.emailstatus.setText("不能为空or输入非法!")

    @pyqtSlot()
    def on_doc_path_button_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "请选择文件夹", "/")
        if len(directory) == 0:
            return
        self.doc_path.setText(directory)

    @pyqtSlot()
    def on_doc_2_button1_clicked(self):
        if helper.data_path == '' or helper.rownum == 0:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">请选择数据文件',
                                        QMessageBox.Ok, QMessageBox.Ok)
        else:
            rowNum = helper.rownum
            try:
                start = int(self.doc_2_start.text())
                end = int(self.doc_2_end.text())
            except:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">please input valid range',
                                            QMessageBox.Ok, QMessageBox.Ok)
                # self.doc_2_status.setText("please input valid range")
            else:
                if start > 0 and start <= rowNum and end > 0 and end <= rowNum:
                    for i in range(start, end + 1):
                        self.doc_2_table.item(i - 1, 0).setCheckState(Qt.Checked)
                    # self.doc_2_status.clear()
                else:
                    reply = QMessageBox.warning(self, 'Message', '<font color="black">please input valid range',
                                                QMessageBox.Ok, QMessageBox.Ok)
                    # self.doc_2_status.setText("please input valid range")

    @pyqtSlot()
    def on_doc_2_button2_clicked(self):
        if helper.data_path == '' or helper.rownum == 0:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">请选择数据文件',
                                        QMessageBox.Ok, QMessageBox.Ok)
        else:
            rowNum = helper.rownum
            for i in range(rowNum):
                self.doc_2_table.item(i, 0).setCheckState(Qt.Checked)

    @pyqtSlot()
    def on_doc_2_button3_clicked(self):
        if helper.data_path == '' or helper.rownum == 0:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">请选择数据文件',
                                        QMessageBox.Ok, QMessageBox.Ok)
        else:
            rowNum = helper.rownum
            for i in range(rowNum):
                self.doc_2_table.item(i, 0).setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def on_doc_3_button1_clicked(self):
        # 'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif'
        # https: // blog.csdn.net / a359680405 / article / details / 45166271
        rootpath = '/'
        filepath, filetype = QFileDialog.getOpenFileName(self,
                                                         "选择图片",
                                                         rootpath,
                                             "(*.jpg;*.bmp;*.png;*.jpeg;*.rgb;*.tif;)")
        if not filepath:
            return
        # import imghdr
        # filetype = imghdr.what(filepath)
        self.doc_3_picpath1 = filepath
        img = QImage(filepath)
        mgnWidth = img.width()
        mgnHeight = img.height()
        # keep the shape of img
        if mgnWidth > mgnHeight:
            scale = mgnWidth / 200
            mgnWidth = 200
            try:
                mgnHeight /= scale
            except:
                print("catch Exception")
                self.doc_3_status.setText("Error: img Width equals to 0")
                mgnHeight = 200
        else:
            scale = mgnHeight / 200
            mgnHeight = 200
            try:
                mgnWidth /= scale
            except:
                print("catch Exception")
                self.doc_3_status.setText("Error: img Width equals to 0")
                mgnWidth = 200
        size = QSize(mgnWidth, mgnHeight)
        pixmap = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio))
        self.doc_3_pic1.resize(mgnWidth, mgnHeight)
        self.doc_3_pic1.setPixmap(pixmap)
        # self.doc_3_pic1.setScaledContents(True)

    @pyqtSlot()
    def on_doc_3_button2_clicked(self):
        rootpath = '/'
        filepath, filetype = QFileDialog.getOpenFileName(self,
                                                         "选择图片",
                                                         rootpath,
                                                         "(*.jpg;*.bmp;*.png;*.jpeg;*.rgb;*.tif;)")
        if not filepath:
            return
        self.doc_3_picpath2 = filepath
        img = QImage(filepath)
        mgnWidth = img.width()
        mgnHeight = img.height()
        # keep the shape of img
        if mgnWidth > mgnHeight:
            scale = mgnWidth / 200
            mgnWidth = 200
            try:
                mgnHeight /= scale
            except:
                print("catch Exception")
                self.doc_3_status.setText("Error: img Width equals to 0")
                mgnHeight = 200
        else:
            scale = mgnHeight / 200
            mgnHeight = 200
            try:
                mgnWidth /= scale
            except:
                print("catch Exception")
                self.doc_3_status.setText("Error: img Width equals to 0")
                mgnWidth = 200
        size = QSize(mgnWidth, mgnHeight)
        pixmap = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio))
        self.doc_3_pic2.resize(mgnWidth, mgnHeight)
        self.doc_3_pic2.setPixmap(pixmap)

    @pyqtSlot()
    def on_doc_clear_clicked(self):
        self.initcover()
        self.initdoc_1_tableview()
        # self.initdoc_2_table()
        self.doc_3_picpath1 = ""
        self.doc_3_picpath2 = ""
        self.doc_path.clear()
        self.doc_2_tablename.clear()
        self.doc_2_text.clear()
        self.doc_2_start.setText("请输入行数")
        self.doc_2_end.setText("请输入行数")
        self.doc_3_pic1.clear()
        self.doc_3_pic2.clear()
        self.doc_3_picname1.setText("图片命名")
        self.doc_3_picname2.setText("图片命名")
        self.doc_3_text.clear()
        self.doc_4_text.clear()
        self.doc_1.setChecked(True)
        self.doc_2.setChecked(True)
        self.doc_3.setChecked(True)
        self.doc_4.setChecked(True)

    @pyqtSlot()
    def on_doc_source_clicked(self):
        from docx import Document
        document = Document()
        # generate cover
        if self.doc_heading.text() and self.doc_company.text() and self.doc_code.text() and self.doc_type.text() and self.doc_reporter.text() and self.doc_date.text():
            generateDocx.generateCover(document, doc_heading=self.doc_heading.text(), doc_company=self.doc_company.text(), doc_code=self.doc_code.text(),
                                       doc_type=self.doc_type.text(), doc_reporter=self.doc_reporter.text(), doc_date=self.doc_date.text())
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: Existing blank lable', QMessageBox.Ok, QMessageBox.Ok)
            # self.doc_status.setText("Error: Existing blank lable")
            return

        # generate directory
        catalog = []
        catalogContent = []
        if self.doc_1.isChecked():
            catalog.append(1)
            if self.doc_content1.text():
                catalogContent.append(self.doc_content1.text())
            else:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: Blank CatalogContent',
                                            QMessageBox.Ok, QMessageBox.Ok)
                # self.doc_status.setText("Error: Blank CatalogContent")
                return
        if self.doc_2.isChecked():
            catalog.append(2)
            if self.doc_content2.text():
                catalogContent.append(self.doc_content2.text())
            else:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: Blank CatalogContent',
                                            QMessageBox.Ok, QMessageBox.Ok)
                # self.doc_status.setText("Error: Blank CatalogContent")
                return
        if self.doc_3.isChecked():
            catalog.append(3)
            if self.doc_content3.text():
                catalogContent.append(self.doc_content3.text())
            else:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: Blank CatalogContent',
                                            QMessageBox.Ok, QMessageBox.Ok)
                # self.doc_status.setText("Error: Blank CatalogContent")
                return
        if self.doc_4.isChecked():
            catalog.append(4)
            if self.doc_content4.text():
                catalogContent.append(self.doc_content4.text())
            else:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: Blank CatalogContent',
                                            QMessageBox.Ok, QMessageBox.Ok)
                # self.doc_status.setText("Error: Blank CatalogContent")
                return
        generateDocx.generateCatalog(document, catalog, catalogContent, doc_code=self.doc_code.text(), doc_heading=self.doc_heading.text())

        # generate Content 1234 respectively
        if self.doc_1.isChecked():
            doc_1_arguments = self.content1helper()
            generateDocx.generateContent1(document, doc_1_arguments, doc_code=self.doc_code.text(), doc_content1=self.doc_content1.text())
        if self.doc_2.isChecked():
            doc_2_arguments = self.content2helper()
            generateDocx.generateContent2(document, doc_2_arguments, doc_content2=self.doc_content2.text())
        if self.doc_3.isChecked():
            doc_3_arguments = self.content3helper()
            generateDocx.generateContent3(document, doc_3_arguments, doc_content3=self.doc_content3.text())
        if self.doc_4.isChecked():
            generateDocx.generateContent4(document, self.doc_4_text.toPlainText(), doc_content4=self.doc_content4.text())
        # save file
        if self.doc_filename.text():
            filename = self.doc_filename.text()
            if self.doc_path.text() and helper.Helper.validatepath(self.doc_path.text()):
                path = self.doc_path.text() + "/" + filename + ".docx"
                print(path)
                # path = '/Users/skye/Desktop/demo1.docx'
                generateDocx.generatedoc(document, path)
                reply = QMessageBox.information(self, 'Message', '<font color="black">报告生成完毕', QMessageBox.Ok, QMessageBox.Ok)
            else:
                reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: please choose the valid path',
                                            QMessageBox.Ok, QMessageBox.Ok)
                # self.doc_status.setText("Error: please choose the valid path")
                return
        else:
            reply = QMessageBox.warning(self, 'Message', '<font color="black">Error: please input valid filename',
                                        QMessageBox.Ok, QMessageBox.Ok)
            # self.doc_status.setText("Error: please input valid filename")
            return

    def getpath(self):
        import re
        index = self.attachment.currentIndex()
        model = index.model()
        file_path = model.filePath(index)
        result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', file_path)
        if result:
            self.attachList.append(file_path)
            if self.File.text():
                self.File.setText(self.File.text() +', ' + file_path)
            else:
                self.File.setText(file_path)

    def setuncheckable(self):
        self.MailgroupBox.setChecked(False)
        self.groupBox_14.setChecked(False)

    def content1helper(self):
        arguments = []
        for i in range(10):
            if i < 7:
                for j in [1, 3]:
                    argument = self.model.index(i, j, QModelIndex()).data()
                    if argument:
                        arguments.append(argument)
                    else:
                        arguments.append("")
            elif i < 9:
                argument = self.model.index(i, 1, QModelIndex()).data()
                if argument:
                    arguments.append(argument)
                else:
                    arguments.append("")
            else:  # 最后一行虽合并了单元格，但索引仍未2/3
                argument = self.model.index(i, 2, QModelIndex()).data()
                if argument:
                    arguments.append(argument)
                else:
                    arguments.append("")
        return arguments

    def content2helper(self):
        arguments = []
        if self.doc_2_tablename.text():
            arguments.append(self.doc_2_tablename.text())
        else:
            arguments.append("")
            # # self.palette1 = QtGui.QPalette()
            # # self.palette1.setColor(QPalette.WindowText, Qt.black)
            # # QMessageBox.setPalette(self, self.palette1)
            # reply = QMessageBox.warning(self, 'Message', '<font color="black">please input the tablename(from Tab2)', QMessageBox.Ok)
            # # if reply == QMessageBox.Ok:
            # #     print("test")
        count = helper.rownum
        nums = []
        for i in range(count):
            # print(self.doc_2_table.item(i, 0).checkState())
            if self.doc_2_table.item(i, 0).checkState() == 2:
                nums.append(i)
        arguments.append(nums)
        if self.doc_2_text.toPlainText():
            arguments.append(self.doc_2_text.toPlainText())
        else:
            arguments.append("")
        print(arguments)
        return arguments

    def content3helper(self):
        arguments = []
        imgpath = []
        imgname = []
        if self.doc_3_picpath1:
            imgpath.append(self.doc_3_picpath1)
        if self.doc_3_picpath2:
            imgpath.append(self.doc_3_picpath2)
        if self.doc_3_picname1:
            imgname.append(self.doc_3_picname1.text())
        else:
            imgname.append("")
        if self.doc_3_picname2:
            imgname.append(self.doc_3_picname2.text())
        else:
            imgname.append("")
        arguments.append(imgpath)
        arguments.append(imgname)
        arguments.append(self.doc_3_text.toPlainText())
        print(arguments)
        return arguments

    def Todarkmodel(self):
        reply = QMessageBox.warning(self, 'Message', '<font color="black">将重新打开窗口!',
                                    QMessageBox.Cancel | QMessageBox.Ok, QMessageBox.Cancel)
        if reply == QMessageBox.Cancel:
            return
        helper.modelversion = "dark"
        helper.threadpool = []
        helper.predict_result = []
        helper.data_path = ''
        helper.rownum = 0
        self.windowList = []
        SecondmainWindow = MainWindow()
        self.windowList.append(SecondmainWindow)
        self.close()
        palette = QtGui.QPalette()
        palette.setColor(SecondmainWindow.backgroundRole(), QtGui.QColor(68, 68, 68))
        SecondmainWindow.setPalette(palette)
        SecondmainWindow.setWindowTitle("Mine Information Management Platform")
        styleFile = './UI/resource/qss/psblack.css'
        Style = helper.Helper.readQss(styleFile)
        SecondmainWindow.setStyleSheet(Style)
        SecondmainWindow.show()

    def Tolightmodel(self):
        reply = QMessageBox.warning(self, 'Message', '<font color="black">将重新打开窗口!',
                                    QMessageBox.Cancel | QMessageBox.Ok, QMessageBox.Cancel)
        if reply == QMessageBox.Cancel:
            return
        helper.modelversion = "light"
        helper.threadpool = []
        helper.predict_result = []
        helper.data_path = ''
        helper.rownum = 0
        self.windowList = []
        SecondmainWindow = MainWindow()
        self.windowList.append(SecondmainWindow)
        self.close()
        palette = QtGui.QPalette()
        palette.setColor(SecondmainWindow.backgroundRole(), QtGui.QColor(255, 255, 255))
        SecondmainWindow.setPalette(palette)
        SecondmainWindow.setFont(QtGui.QFont("Times New Roman", 12))
        SecondmainWindow.setWindowTitle("Mine Information Management Platform")
        SecondmainWindow.show()

    def quit(self):
        reply = QMessageBox.warning(self, 'Message', '<font color="black">是否退出系统？',
                                    QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(500)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.start()
            self.animation.finished.connect(self.close1)

    def close1(self):
        self.hide()
        self.close()

    def refresh(self):
        if helper.modelversion == "light":
            self.Tolightmodel()
        else:
            self.Todarkmodel()

    def changeuser(self):
        reply = QMessageBox.question(self, "Question", '<font color="black">是否确认退出当前账号？',
                                      QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            pass
        else:
            helper.predict_result = []
            helper.threadpool = []
            helper.data_path = ''
            helper.rownum = 0
            from UI.loginMainWindow import loginMainWindow
            self.windowList = []
            FirstmainWindow = loginMainWindow()
            self.windowList.append(FirstmainWindow)
            self.close()
            if helper.modelversion == "light":
                palette = QtGui.QPalette()
                palette.setColor(FirstmainWindow.backgroundRole(), QtGui.QColor(255, 255, 255))
                FirstmainWindow.setPalette(palette)
                FirstmainWindow.setWindowTitle("Mine Information Management Platform")
                FirstmainWindow.setFont(QtGui.QFont("Times New Roman", 12))
                FirstmainWindow.show()
            else:
                palette = QtGui.QPalette()
                palette.setColor(FirstmainWindow.backgroundRole(), QtGui.QColor(68, 68, 68))
                FirstmainWindow.setPalette(palette)
                FirstmainWindow.setWindowTitle("Mine Information Management Platform")
                styleFile = './UI/resource/qss/psblack.css'
                Style = helper.Helper.readQss(styleFile)
                FirstmainWindow.setStyleSheet(Style)
                FirstmainWindow.show()

    def trainingdata(self, filepath, model):
        from ml_data import SVM, LDA, tensorflow1
        # map = SVM.svm1('/Users/skye/PycharmProjects/20190302/data/光谱数据.csv')
        try:
            if model == 1:
                map = SVM.svm1(filepath)
            elif model == 2:
                map = LDA.lda1(filepath)
            elif model == 3:
                map = tensorflow1.tensorflow_ann(filepath)
        except:
            self.importStatus.setText("Error: SVM数据处理错误，请检查文件数据格式！")
            print("catch exception: SVM数据处理错误")
            helper.threadpool = []
            e = Exception("SVM数据处理错误")
            raise e
        else:
            import shutil
            if model == 1:
                self.showimg('PCA+SVM')
                shutil.copy("./data/ml_dataset/training_tmp_dataset.csv", "./data/ml_dataset/"+"PCA+SVM_"+"训练数据集.csv")
            elif model == 2:
                self.showimg('LDA+SVM')
                shutil.copy("./data/ml_dataset/training_tmp_dataset.csv", "./data/ml_dataset/"+"LDA+SVM_"+"训练数据集.csv")
            elif model == 3:
                self.showimg('LDA+ANN')
                shutil.copy("./data/ml_dataset/training_tmp_dataset.csv", "./data/ml_dataset/"+"LDA+ANN_"+"训练数据集.csv")
            helper.threadpool = []
            if model == 3:
                text = 'ANN_tensorflow model 在训练集上的准确率为: ' + str(map['accuracy']) + '\n'
            else:
                text = 'SVM model 在训练集上的准确率为: ' + str(map['accuracy']) + '\n'
            text = text + map['training_report']
            self.training_report.clear()
            self.training_report.appendPlainText(text)
            self.importStatus.setText("training completed!")

    def showimg(self, method):
        img1 = QImage("./images/"+str(method)+"/img1.png")
        size = QSize(320, 240)
        pixmap = QPixmap.fromImage(img1.scaled(size, Qt.IgnoreAspectRatio))
        self.data_pic_1.resize(320, 240)
        self.data_pic_1.setPixmap(pixmap)
        img2 = QImage("./images/"+method+"/img2.png")
        pixmap = QPixmap.fromImage(img2.scaled(size, Qt.IgnoreAspectRatio))
        self.data_pic_2.resize(320, 240)
        self.data_pic_2.setPixmap(pixmap)
        img3 = QImage("./images/"+method+"/img3.png")
        pixmap = QPixmap.fromImage(img3.scaled(size, Qt.IgnoreAspectRatio))
        self.data_pic_3.resize(320, 240)
        self.data_pic_3.setPixmap(pixmap)
        img4 = QImage("./images/"+method+"/img4.png")
        pixmap = QPixmap.fromImage(img4.scaled(size, Qt.IgnoreAspectRatio))
        self.data_pic_4.resize(320, 240)
        self.data_pic_4.setPixmap(pixmap)

    # def initdoc_3_pic(self):
    #     # https: // blog.csdn.net / Victor_zero / article / details / 81532511
    #     # scale = 0.2
    #     img = QImage("/Users/skye/Pictures/profile.jpg")
    #     # mgnWidth = int(img.width() * scale)
    #     # mgnHeight = int(img.height() * scale)
    #     mgnWidth = 200
    #     mgnHeight = 200
    #     size = QSize(mgnWidth, mgnHeight)
    #     pixmap = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio))
    #     self.doc_3_pic1.resize(mgnWidth, mgnHeight)
    #     self.doc_3_pic1.setPixmap(pixmap)
    #     self.doc_3_pic1.setScaledContents(True)