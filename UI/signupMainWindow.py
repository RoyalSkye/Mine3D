from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI.signup import Ui_MainWindow
from UI.mainwindow import MainWindow
import helper
import database

class signupMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.animation1 = QPropertyAnimation(self, b"windowOpacity")
        self.animation1.setDuration(500)
        self.animation1.setStartValue(0)
        self.animation1.setEndValue(1)
        self.animation1.start()

    @pyqtSlot()
    def on_signup_clicked(self):
        username = self.username.text()
        pwd1 = self.pwd1.text()
        pwd2 = self.pwd2.text()
        if username and pwd1 and pwd2 :
            if pwd1 != pwd2:
                reply = QMessageBox.critical(self, 'Message', '<font color="black">两次输入密码不一致！', QMessageBox.Ok,
                                             QMessageBox.Ok)
                return
            try:
                userinfo = []
                userinfo.append(str(username))
                userinfo.append(str(pwd1))
                database.insertuser(userinfo)
            except:
                reply = QMessageBox.critical(self, 'Message', '<font color="black">注册失败！', QMessageBox.Ok,
                                             QMessageBox.Ok)
                print("insert user catch exception")
                e = Exception(",...")
                raise e
                return
            else:
                reply = QMessageBox.information(self, 'Message', '<font color="black">注册成功！', QMessageBox.Ok,
                                                QMessageBox.Ok)
                # 跳转至登录界面
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
        else:
            reply = QMessageBox.critical(self, 'Message', '<font color="black">用户名或密码不能为空！', QMessageBox.Ok,
                                         QMessageBox.Ok)

    @pyqtSlot()
    def on_exit_clicked(self):
        # 跳转至登录界面
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
