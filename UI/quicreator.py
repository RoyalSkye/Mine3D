# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quicreator.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QUICreator(object):
    def setupUi(self, QUICreator):
        QUICreator.setObjectName("QUICreator")
        QUICreator.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(QUICreator)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.objFile = QtWidgets.QOpenGLWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objFile.sizePolicy().hasHeightForWidth())
        self.objFile.setSizePolicy(sizePolicy)
        self.objFile.setMinimumSize(QtCore.QSize(600, 600))
        self.objFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.objFile.setObjectName("objFile")
        self.horizontalLayout_9.addWidget(self.objFile)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.dataTab = QtWidgets.QWidget()
        self.dataTab.setObjectName("dataTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dataTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.dataTab)
        self.groupBox.setStyleSheet("")
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lab = QtWidgets.QLabel(self.groupBox)
        self.lab.setAlignment(QtCore.Qt.AlignCenter)
        self.lab.setObjectName("lab")
        self.gridLayout_2.addWidget(self.lab, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 6)
        self.rbtn1 = QtWidgets.QRadioButton(self.groupBox)
        self.rbtn1.setObjectName("rbtn1")
        self.gridLayout_2.addWidget(self.rbtn1, 1, 0, 1, 1)
        self.rbtn2 = QtWidgets.QRadioButton(self.groupBox)
        self.rbtn2.setObjectName("rbtn2")
        self.gridLayout_2.addWidget(self.rbtn2, 1, 1, 1, 1)
        self.ck1 = QtWidgets.QCheckBox(self.groupBox)
        self.ck1.setObjectName("ck1")
        self.gridLayout_2.addWidget(self.ck1, 1, 2, 1, 1)
        self.ck2 = QtWidgets.QCheckBox(self.groupBox)
        self.ck2.setChecked(False)
        self.ck2.setObjectName("ck2")
        self.gridLayout_2.addWidget(self.ck2, 1, 3, 1, 1)
        self.ck3 = QtWidgets.QCheckBox(self.groupBox)
        self.ck3.setObjectName("ck3")
        self.gridLayout_2.addWidget(self.ck3, 1, 4, 1, 1)
        self.cbox1 = QtWidgets.QComboBox(self.groupBox)
        self.cbox1.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cbox1.setObjectName("cbox1")
        self.gridLayout_2.addWidget(self.cbox1, 1, 5, 1, 1)
        self.cbox2 = QtWidgets.QComboBox(self.groupBox)
        self.cbox2.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cbox2.setObjectName("cbox2")
        self.gridLayout_2.addWidget(self.cbox2, 1, 6, 1, 1)
        self.btnInfo = QtWidgets.QPushButton(self.groupBox)
        self.btnInfo.setObjectName("btnInfo")
        self.gridLayout_2.addWidget(self.btnInfo, 2, 0, 1, 1)
        self.btnQuestion = QtWidgets.QPushButton(self.groupBox)
        self.btnQuestion.setObjectName("btnQuestion")
        self.gridLayout_2.addWidget(self.btnQuestion, 2, 1, 1, 1)
        self.btnError = QtWidgets.QPushButton(self.groupBox)
        self.btnError.setObjectName("btnError")
        self.gridLayout_2.addWidget(self.btnError, 2, 2, 1, 1)
        self.btnInput = QtWidgets.QPushButton(self.groupBox)
        self.btnInput.setObjectName("btnInput")
        self.gridLayout_2.addWidget(self.btnInput, 2, 3, 1, 1)
        self.btnInputPwd = QtWidgets.QPushButton(self.groupBox)
        self.btnInputPwd.setObjectName("btnInputPwd")
        self.gridLayout_2.addWidget(self.btnInputPwd, 2, 4, 1, 1)
        self.btnInputcbox = QtWidgets.QPushButton(self.groupBox)
        self.btnInputcbox.setObjectName("btnInputcbox")
        self.gridLayout_2.addWidget(self.btnInputcbox, 2, 5, 1, 1)
        self.btnWidget = QtWidgets.QPushButton(self.groupBox)
        self.btnWidget.setObjectName("btnWidget")
        self.gridLayout_2.addWidget(self.btnWidget, 2, 6, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 3, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 3, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 3, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 3, 3, 1, 2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 3, 5, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 18))
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 4, 3, 1, 4)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 5, 0, 1, 7)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 4, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.dataTab, "")
        self.importTab = QtWidgets.QWidget()
        self.importTab.setObjectName("importTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.importTab)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.path = QtWidgets.QLineEdit(self.importTab)
        self.path.setObjectName("path")
        self.gridLayout_4.addWidget(self.path, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.importTab)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.importTab)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.importTab)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.importFile = QtWidgets.QPushButton(self.importTab)
        self.importFile.setObjectName("importFile")
        self.gridLayout_4.addWidget(self.importFile, 0, 2, 1, 1)
        self.data = QtWidgets.QLabel(self.importTab)
        self.data.setText("")
        self.data.setObjectName("data")
        self.gridLayout_4.addWidget(self.data, 2, 1, 1, 1)
        self.training = QtWidgets.QPushButton(self.importTab)
        self.training.setObjectName("training")
        self.gridLayout_4.addWidget(self.training, 1, 2, 1, 1)
        self.importStatus = QtWidgets.QLabel(self.importTab)
        self.importStatus.setText("")
        self.importStatus.setObjectName("importStatus")
        self.gridLayout_4.addWidget(self.importStatus, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.importTab, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.treeView = QtWidgets.QTreeView(self.tab4)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_3.addWidget(self.treeView)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab4, "")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MailgroupBox = QtWidgets.QGroupBox(self.tab5)
        self.MailgroupBox.setFlat(False)
        self.MailgroupBox.setCheckable(True)
        self.MailgroupBox.setChecked(True)
        self.MailgroupBox.setObjectName("MailgroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.MailgroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.MailContext = QtWidgets.QPlainTextEdit(self.MailgroupBox)
        self.MailContext.setOverwriteMode(False)
        self.MailContext.setObjectName("MailContext")
        self.gridLayout.addWidget(self.MailContext, 4, 0, 1, 3)
        self.attachment = QtWidgets.QTreeView(self.MailgroupBox)
        self.attachment.setObjectName("attachment")
        self.gridLayout.addWidget(self.attachment, 3, 0, 1, 3)
        self.receiver = QtWidgets.QTreeWidget(self.MailgroupBox)
        self.receiver.setObjectName("receiver")
        self.receiver.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.receiver, 1, 0, 1, 3)
        self.maillabel = QtWidgets.QLabel(self.MailgroupBox)
        self.maillabel.setObjectName("maillabel")
        self.gridLayout.addWidget(self.maillabel, 5, 0, 1, 1)
        self.sendemail = QtWidgets.QPushButton(self.MailgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendemail.sizePolicy().hasHeightForWidth())
        self.sendemail.setSizePolicy(sizePolicy)
        self.sendemail.setObjectName("sendemail")
        self.gridLayout.addWidget(self.sendemail, 5, 2, 1, 1)
        self.clearemail = QtWidgets.QPushButton(self.MailgroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearemail.sizePolicy().hasHeightForWidth())
        self.clearemail.setSizePolicy(sizePolicy)
        self.clearemail.setCheckable(False)
        self.clearemail.setChecked(False)
        self.clearemail.setObjectName("clearemail")
        self.gridLayout.addWidget(self.clearemail, 5, 1, 1, 1)
        self.clearflie = QtWidgets.QPushButton(self.MailgroupBox)
        self.clearflie.setIconSize(QtCore.QSize(16, 16))
        self.clearflie.setObjectName("clearflie")
        self.gridLayout.addWidget(self.clearflie, 2, 2, 1, 1)
        self.head = QtWidgets.QLineEdit(self.MailgroupBox)
        self.head.setClearButtonEnabled(True)
        self.head.setObjectName("head")
        self.gridLayout.addWidget(self.head, 0, 0, 1, 3)
        self.File = QtWidgets.QLineEdit(self.MailgroupBox)
        self.File.setReadOnly(True)
        self.File.setObjectName("File")
        self.gridLayout.addWidget(self.File, 2, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.MailgroupBox)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab5, "")
        self.tab6 = QtWidgets.QWidget()
        self.tab6.setObjectName("tab6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.emailsetting = QtWidgets.QGroupBox(self.tab6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailsetting.sizePolicy().hasHeightForWidth())
        self.emailsetting.setSizePolicy(sizePolicy)
        self.emailsetting.setCheckable(False)
        self.emailsetting.setObjectName("emailsetting")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.emailsetting)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.emailstatus = QtWidgets.QLabel(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailstatus.sizePolicy().hasHeightForWidth())
        self.emailstatus.setSizePolicy(sizePolicy)
        self.emailstatus.setText("")
        self.emailstatus.setObjectName("emailstatus")
        self.gridLayout_3.addWidget(self.emailstatus, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.emailsender = QtWidgets.QLineEdit(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailsender.sizePolicy().hasHeightForWidth())
        self.emailsender.setSizePolicy(sizePolicy)
        self.emailsender.setClearButtonEnabled(True)
        self.emailsender.setObjectName("emailsender")
        self.gridLayout_3.addWidget(self.emailsender, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.emailsetting)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.smtpserver = QtWidgets.QLineEdit(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smtpserver.sizePolicy().hasHeightForWidth())
        self.smtpserver.setSizePolicy(sizePolicy)
        self.smtpserver.setClearButtonEnabled(True)
        self.smtpserver.setObjectName("smtpserver")
        self.gridLayout_3.addWidget(self.smtpserver, 0, 1, 1, 1)
        self.emailsource = QtWidgets.QPushButton(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailsource.sizePolicy().hasHeightForWidth())
        self.emailsource.setSizePolicy(sizePolicy)
        self.emailsource.setObjectName("emailsource")
        self.gridLayout_3.addWidget(self.emailsource, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.emailpwd = QtWidgets.QLineEdit(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailpwd.sizePolicy().hasHeightForWidth())
        self.emailpwd.setSizePolicy(sizePolicy)
        self.emailpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.emailpwd.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.emailpwd.setClearButtonEnabled(True)
        self.emailpwd.setObjectName("emailpwd")
        self.gridLayout_3.addWidget(self.emailpwd, 3, 1, 1, 1)
        self.port = QtWidgets.QLineEdit(self.emailsetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setClearButtonEnabled(True)
        self.port.setObjectName("port")
        self.gridLayout_3.addWidget(self.port, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.emailsetting)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.emailsetting)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab6)
        self.groupBox_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.accountstatus = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountstatus.sizePolicy().hasHeightForWidth())
        self.accountstatus.setSizePolicy(sizePolicy)
        self.accountstatus.setText("")
        self.accountstatus.setObjectName("accountstatus")
        self.gridLayout_5.addWidget(self.accountstatus, 5, 1, 1, 1)
        self.accountsource = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountsource.sizePolicy().hasHeightForWidth())
        self.accountsource.setSizePolicy(sizePolicy)
        self.accountsource.setObjectName("accountsource")
        self.gridLayout_5.addWidget(self.accountsource, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(158, 21))
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.oldpwd = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldpwd.sizePolicy().hasHeightForWidth())
        self.oldpwd.setSizePolicy(sizePolicy)
        self.oldpwd.setMinimumSize(QtCore.QSize(158, 0))
        self.oldpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldpwd.setClearButtonEnabled(True)
        self.oldpwd.setObjectName("oldpwd")
        self.gridLayout_5.addWidget(self.oldpwd, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 1)
        self.newpwd1 = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newpwd1.sizePolicy().hasHeightForWidth())
        self.newpwd1.setSizePolicy(sizePolicy)
        self.newpwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpwd1.setClearButtonEnabled(True)
        self.newpwd1.setObjectName("newpwd1")
        self.gridLayout_5.addWidget(self.newpwd1, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)
        self.newpwd2 = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newpwd2.sizePolicy().hasHeightForWidth())
        self.newpwd2.setSizePolicy(sizePolicy)
        self.newpwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpwd2.setObjectName("newpwd2")
        self.gridLayout_5.addWidget(self.newpwd2, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 6, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab6, "")
        self.horizontalLayout_9.addWidget(self.tabWidget)
        QUICreator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QUICreator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 22))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_B = QtWidgets.QMenu(self.menubar)
        self.menu_B.setObjectName("menu_B")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        QUICreator.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(QUICreator)
        self.action.setObjectName("action")
        self.action_O = QtWidgets.QAction(QUICreator)
        self.action_O.setObjectName("action_O")
        self.action_S = QtWidgets.QAction(QUICreator)
        self.action_S.setObjectName("action_S")
        self.action_C = QtWidgets.QAction(QUICreator)
        self.action_C.setObjectName("action_C")
        self.action_X = QtWidgets.QAction(QUICreator)
        self.action_X.setObjectName("action_X")
        self.action_C_2 = QtWidgets.QAction(QUICreator)
        self.action_C_2.setObjectName("action_C_2")
        self.action_V = QtWidgets.QAction(QUICreator)
        self.action_V.setObjectName("action_V")
        self.actionGouj = QtWidgets.QAction(QUICreator)
        self.actionGouj.setObjectName("actionGouj")
        self.action_T = QtWidgets.QAction(QUICreator)
        self.action_T.setObjectName("action_T")
        self.action_A = QtWidgets.QAction(QUICreator)
        self.action_A.setObjectName("action_A")
        self.actionshengcheng = QtWidgets.QAction(QUICreator)
        self.actionshengcheng.setObjectName("actionshengcheng")
        self.actiond = QtWidgets.QAction(QUICreator)
        self.actiond.setObjectName("actiond")
        self.menu_F.addAction(self.action)
        self.menu_F.addAction(self.action_O)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_S)
        self.menu_F.addAction(self.action_C)
        self.menu_E.addAction(self.action_X)
        self.menu_E.addAction(self.action_C_2)
        self.menu_E.addAction(self.action_V)
        self.menu_B.addAction(self.actionGouj)
        self.menu_B.addAction(self.actiond)
        self.menu_H.addAction(self.action_T)
        self.menu_H.addAction(self.action_A)
        self.menu.addAction(self.actionshengcheng)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_B.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(QUICreator)
        self.tabWidget.setCurrentIndex(5)
        self.horizontalSlider.valueChanged['int'].connect(self.progressBar.setValue)
        QtCore.QMetaObject.connectSlotsByName(QUICreator)

    def retranslateUi(self, QUICreator):
        _translate = QtCore.QCoreApplication.translate
        QUICreator.setWindowTitle(_translate("QUICreator", "MainWindow"))
        self.groupBox.setTitle(_translate("QUICreator", "分组框"))
        self.lab.setText(_translate("QUICreator", "飞扬青云"))
        self.lineEdit.setText(_translate("QUICreator", "拿人钱财替人消灾,人生江湖如此,程序江湖亦如此."))
        self.rbtn1.setText(_translate("QUICreator", "单选框1"))
        self.rbtn2.setText(_translate("QUICreator", "单选框2"))
        self.ck1.setText(_translate("QUICreator", "复选框1"))
        self.ck2.setText(_translate("QUICreator", "复选框2"))
        self.ck3.setText(_translate("QUICreator", "复选框3"))
        self.btnInfo.setText(_translate("QUICreator", "信息框"))
        self.btnQuestion.setText(_translate("QUICreator", "提示框"))
        self.btnError.setText(_translate("QUICreator", "错误框"))
        self.btnInput.setText(_translate("QUICreator", "标准输入框"))
        self.btnInputPwd.setText(_translate("QUICreator", "密码输入框"))
        self.btnInputcbox.setText(_translate("QUICreator", "下拉输入框"))
        self.btnWidget.setText(_translate("QUICreator", "新窗体"))
        self.plainTextEdit.setPlainText(_translate("QUICreator", "每个人心中都有一段鲜不为人知的故事，\n"
"如果不是某一天，\n"
"某个不经意的回头一瞥，\n"
"那段往事，\n"
"就只能永远埋在记忆的最深处，\n"
"那是回忆的尽头，\n"
"可就无法避免那一触，\n"
"无论你在上面用怎样淤厚的冷漠层层包裹，\n"
"却总在瞬间崩溃。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), _translate("QUICreator", "当前数据"))
        self.label_4.setText(_translate("QUICreator", "导入状态："))
        self.label.setText(_translate("QUICreator", "文件路径："))
        self.importFile.setText(_translate("QUICreator", "选择文件"))
        self.training.setText(_translate("QUICreator", "导入/训练"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.importTab), _translate("QUICreator", "导入数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("QUICreator", "数据报表"))
        self.label_3.setText(_translate("QUICreator", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("QUICreator", "生成报表"))
        self.MailgroupBox.setTitle(_translate("QUICreator", "SendReport"))
        self.maillabel.setText(_translate("QUICreator", "发送状态: "))
        self.sendemail.setText(_translate("QUICreator", "Send"))
        self.clearemail.setText(_translate("QUICreator", "Clear"))
        self.clearflie.setText(_translate("QUICreator", "Clear"))
        self.head.setText(_translate("QUICreator", "请输入标题"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("QUICreator", "发送报表"))
        self.emailsetting.setTitle(_translate("QUICreator", "邮件设置"))
        self.label_5.setText(_translate("QUICreator", "          SMTP-Server: "))
        self.label_6.setText(_translate("QUICreator", "                Port:"))
        self.emailsource.setText(_translate("QUICreator", "Source"))
        self.label_7.setText(_translate("QUICreator", "              Sender:"))
        self.label_8.setText(_translate("QUICreator", "            Password:"))
        self.groupBox_3.setTitle(_translate("QUICreator", "账户设置"))
        self.accountsource.setText(_translate("QUICreator", "Source"))
        self.label_12.setText(_translate("QUICreator", "修改密码:"))
        self.label_11.setText(_translate("QUICreator", "输入原始密码:"))
        self.label_14.setText(_translate("QUICreator", "再次输入新密码:"))
        self.label_13.setText(_translate("QUICreator", "输入新密码:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab6), _translate("QUICreator", "设置"))
        self.menu_F.setTitle(_translate("QUICreator", "文件(&F)"))
        self.menu_E.setTitle(_translate("QUICreator", "编辑(&E)"))
        self.menu_B.setTitle(_translate("QUICreator", "构建(&B)"))
        self.menu_H.setTitle(_translate("QUICreator", "帮助(&H)"))
        self.menu.setTitle(_translate("QUICreator", "报表"))
        self.action.setText(_translate("QUICreator", "新建文件(&N)"))
        self.action_O.setText(_translate("QUICreator", "打开文件(&O)"))
        self.action_S.setText(_translate("QUICreator", "保存文件(&S) "))
        self.action_C.setText(_translate("QUICreator", "关闭退出(&C)"))
        self.action_X.setText(_translate("QUICreator", "剪切(&X) "))
        self.action_C_2.setText(_translate("QUICreator", "复制(&C)"))
        self.action_V.setText(_translate("QUICreator", "粘贴(&V)"))
        self.actionGouj.setText(_translate("QUICreator", "构建项目(&B)"))
        self.action_T.setText(_translate("QUICreator", "帮助文档(&T)"))
        self.action_A.setText(_translate("QUICreator", "关于(&A)"))
        self.actionshengcheng.setText(_translate("QUICreator", "生成报表"))
        self.actiond.setText(_translate("QUICreator", "导入数据"))


