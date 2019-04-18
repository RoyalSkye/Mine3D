import user, database
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI.login import Ui_MainWindow
from UI.mainwindow import MainWindow

class loginMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.animation1 = QPropertyAnimation(self, b"windowOpacity")
        self.animation1.setDuration(500)
        self.animation1.setStartValue(0)
        self.animation1.setEndValue(1)
        self.animation1.start()

    @pyqtSlot()
    def on_login_clicked(self):
        self.login_username.setText("skye")
        self.login_pwd.setText("123456")
        if self.login_username.text() and self.login_pwd.text():
            userinfo = database.getUserByusername(self.login_username.text(), self.login_pwd.text())
            print(userinfo)
            if userinfo:
                user.user.setUser(userinfo[0])

                # 跳转至主界面
                self.windowList = []
                SecondmainWindow = MainWindow()
                self.windowList.append(SecondmainWindow)
                self.close()

                import helper
                if helper.modelversion == "light":
                    palette = QtGui.QPalette()
                    palette.setColor(SecondmainWindow.backgroundRole(), QtGui.QColor(255, 255, 255))
                    SecondmainWindow.setPalette(palette)
                    SecondmainWindow.setFont(QtGui.QFont("Times New Roman", 12))
                    SecondmainWindow.setWindowTitle("Mine Information Management Platform")
                    SecondmainWindow.show()
                else:
                    palette = QtGui.QPalette()
                    palette.setColor(SecondmainWindow.backgroundRole(), QtGui.QColor(68, 68, 68))
                    SecondmainWindow.setPalette(palette)
                    SecondmainWindow.setWindowTitle("Mine Information Management Platform")
                    styleFile = './UI/resource/qss/psblack.css'
                    Style = helper.Helper.readQss(styleFile)
                    SecondmainWindow.setStyleSheet(Style)
                    SecondmainWindow.show()
            else:
                self.palette1 = QtGui.QPalette()
                self.palette1.setColor(QPalette.WindowText, Qt.black)
                self.QMessageBox = QtWidgets.QMessageBox()
                self.QMessageBox.setPalette(self.palette1)
                reply = QMessageBox.warning(self, 'Message', '<font color="black">用户名或密码错误！', QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    pass
                print("用户名或密码错误！")
        else:
            self.palette1 = QtGui.QPalette()
            self.palette1.setColor(QPalette.WindowText, Qt.black)
            self.QMessageBox = QtWidgets.QMessageBox()
            self.QMessageBox.setPalette(self.palette1)
            reply = QMessageBox.warning(self, 'Message', '<font color="black">用户名或密码不能为空！', QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                pass

    @pyqtSlot()
    def on_exit_clicked(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
        self.animation.finished.connect(self.close1)

    def close1(self):
        self.hide()
        self.close()

    # def closeEvent(self, event):
    #     self.animation = QPropertyAnimation(self, b"windowOpacity")
    #     self.animation.setDuration(500)
    #     self.animation.setStartValue(1)
    #     self.animation.setEndValue(0)
    #     self.animation.start()
    #     self.animation.finished.connect(self.close1)