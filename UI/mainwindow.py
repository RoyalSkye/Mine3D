import os
import xlrd
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from UI.quicreator import Ui_QUICreator

class MainWindow(QMainWindow, Ui_QUICreator):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initTableWidget()
        self.initfont()
        self.initEmailBox()
        self.initreceiver()
        self.attachList = []  # 附件列表

    def initfont(self):
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.importFile.setFont(font)
        self.label.setFont(font)
        self.label_4.setFont(font)
        self.training.setFont(font)

    def initTableWidget(self):
        import database
        minedata = database.getminedata()
        if minedata:
            self.tableWidget.setRowCount(len(minedata))
            self.tableWidget.setColumnCount(len(minedata[0]))
            self.tableWidget.setHorizontalHeaderLabels(['id', 'data1', 'data2', 'data3', 'data4'])
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            for i in range(0, len(minedata)):
                for j in range(0, len(minedata[i])):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(minedata[i][j])))

            # problem 1: id = QtWidgets.QTableWidgetItem(entry[0])
            # if QtWidgets.QTableWidgetItem(id) the data will not shown on the table
            # i = 0
            # for entry in minedata:
            #     id = entry[0]
            #     #
            #     data1 = QtWidgets.QTableWidgetItem(entry[1])
            #     data2 = QtWidgets.QTableWidgetItem(entry[2])
            #     data3 = QtWidgets.QTableWidgetItem(entry[3])
            #     data4 = QtWidgets.QTableWidgetItem(entry[4])
            #     self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(id)))
            #     self.tableWidget.setItem(i, 1, data1)
            #     self.tableWidget.setItem(i, 2, data2)
            #     self.tableWidget.setItem(i, 3, data3)
            #     self.tableWidget.setItem(i, 4, data4)
            #     i = i + 1
        else:
            print("data is null!")

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
        import database
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


    # 槽函数会执行2次if不写装饰器@pyqtSlot()
    @pyqtSlot()
    def on_importFile_clicked(self):
        projectpath = os.getcwd()
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选择EXCEL文件", projectpath, "(*.xlsx;*.xls)") # 所有文件 (*.*)
        if len(filename) == 0:
            return
        self.path.setText(filename)

    @pyqtSlot()
    def on_training_clicked(self):
        import database as db
        filename = self.path.text()
        if(filename == ''):
            pass
        else:
            data = xlrd.open_workbook(filename)
            print(data.sheet_names())
            names = data.sheet_names()
            for name in names:
                table = data.sheet_by_name(name)
                # print(table.nrows)
                for i in range(1, table.nrows):
                    # print(table.row_values(i))
                    db.insertminedata(table.row_values(i))
            self.importStatus.setText("import successfully!")
            self.initTableWidget()

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
        self.maillabel.clear()
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
            self.maillabel.setText(msg)
        else:
            self.maillabel.setText('发送状态: 收件人或标题为空！')

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