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
        self.initTableWidget()
        self.initfont()
        self.initEmailBox()
        self.initreceiver()
        self.attachList = []  # 附件列表

        # simulate login
        userinfo = database.getUserByusername("skye", "123456")
        if userinfo:
            user.user.setUser(userinfo[0])
        else:
            print("用户名密码错误!")

        # 判断用户权限，如果为普通用户，则将groupbox设置为不可选状态
        if(user.user.identify == "admin"):
            pass
        else:
            self.MailgroupBox.setChecked(False)
            self.MailgroupBox.toggled.connect(self.setuncheckable)

        self.initemailsetting()
        self.initcover()
        self.initdoc_1_tableview()

    def initfont(self):
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.importFile.setFont(font)
        self.label.setFont(font)
        self.label_4.setFont(font)
        self.training.setFont(font)

    def initcover(self):
        self.doc_heading.setText('露天采场矿岩与品位信息报告')
        self.doc_company.setText('露天采场矿岩股份有限公司')
        self.doc_code.setText(helper.Helper.generateTimestamp())
        self.doc_reporter.setText(user.user.username)
        self.doc_date.setText(helper.Helper.getdatetime())
        self.doc_type.setText('常规更新')
        self.doc_filename.setText('demo1')

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
                self.model.setItem(row, 2*column, item)
        for row in range(7, 10):
            item = QStandardItem(tmp[count])
            count += 1
            item.setFlags(Qt.NoItemFlags)
            item.setTextAlignment(Qt.AlignCenter)
            self.model.setItem(row, 0, item)
        self.doc_1_tableview.setModel(self.model)

        # index = self.model.index(0, 0, QModelIndex())
        # str1 = index.data()
        # print(str1)

    def initTableWidget(self):
        minedata = database.getminedata()
        if minedata:
            self.tableWidget.setRowCount(len(minedata))
            self.tableWidget.setColumnCount(len(minedata[0]))
            self.tableWidget.setHorizontalHeaderLabels(['id', 'data1', 'data2', 'data3', 'data4'])
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            for i in range(0, len(minedata)):
                for j in range(0, len(minedata[i])):
                    item = QtWidgets.QTableWidgetItem(str(minedata[i][j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, item)
                    # self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(minedata[i][j])))

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

    # 槽函数会执行2次if不写装饰器@pyqtSlot()
    @pyqtSlot()
    def on_importFile_clicked(self):
        # projectpath = os.getcwd()
        rootpath = '/'
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选择EXCEL文件", rootpath, "(*.xlsx;*.xls)") # 所有文件 (*.*)
        if len(filename) == 0:
            return
        self.path.setText(filename)

    @pyqtSlot()
    def on_training_clicked(self):
        filename = self.path.text()
        if filename == '' or not helper.Helper.validatepath(filename):
            self.importStatus.setText("Error: please choose valid file")
            return
        else:
            data = xlrd.open_workbook(filename)
            print(data.sheet_names())
            names = data.sheet_names()
            for name in names:
                table = data.sheet_by_name(name)
                # print(table.nrows)
                for i in range(1, table.nrows):
                    # print(table.row_values(i))
                    database.insertminedata(table.row_values(i))
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
    def on_doc_source_clicked(self):
        from docx import Document
        document = Document()
        # generate cover
        if self.doc_heading.text() and self.doc_company.text() and self.doc_code.text() and self.doc_type.text() and self.doc_reporter.text() and self.doc_date.text():
            generateDocx.generateCover(document, doc_heading=self.doc_heading.text(), doc_company=self.doc_company.text(), doc_code=self.doc_code.text(),
                                       doc_type=self.doc_type.text(), doc_reporter=self.doc_reporter.text(), doc_date=self.doc_date.text())
        else:
            self.doc_status.setText("Error: Existing blank lable")
            return
        # generate directory
        catalog = []
        catalogContent = []
        if self.doc_1.isChecked():
            catalog.append(1)
            if self.doc_content1.text():
                catalogContent.append(self.doc_content1.text())
            else:
                self.doc_status.setText("Error: Blank CatalogContent")
                return
        if self.doc_2.isChecked():
            catalog.append(2)
            if self.doc_content2.text():
                catalogContent.append(self.doc_content2.text())
            else:
                self.doc_status.setText("Error: Blank CatalogContent")
                return
        if self.doc_3.isChecked():
            catalog.append(3)
            if self.doc_content3.text():
                catalogContent.append(self.doc_content3.text())
            else:
                self.doc_status.setText("Error: Blank CatalogContent")
                return
        if self.doc_4.isChecked():
            catalog.append(4)
            if self.doc_content4.text():
                catalogContent.append(self.doc_content4.text())
            else:
                self.doc_status.setText("Error: Blank CatalogContent")
                return
        generateDocx.generateCatalog(document, catalog, catalogContent, doc_code=self.doc_code.text(), doc_heading=self.doc_heading.text())
        # generate Content 1234 respectively
        if self.doc_1.isChecked():
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
            generateDocx.generateContent1(document, arguments, doc_code=self.doc_code.text(), doc_content1=self.doc_content1.text())
        if self.doc_2.isChecked():
            generateDocx.generateContent2(document)
        if self.doc_3.isChecked():
            generateDocx.generateContent3(document)
        if self.doc_4.isChecked():
            generateDocx.generateContent4(document)
        # save file
        if self.doc_filename.text():
            filename = self.doc_filename.text()
            if self.doc_path.text() and helper.Helper.validatepath(self.doc_path.text()):
                path = self.doc_path.text() + "/" + filename + ".docx"
                print(path)
                # path = '/Users/skye/Desktop/demo1.docx'
                generateDocx.generatedoc(document, path)
                self.doc_status.setText("generate report successfully")
            else:
                self.doc_status.setText("Error: please choose the valid path")
                return
        else:
            self.doc_status.setText("Error: please input valid filename")
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
