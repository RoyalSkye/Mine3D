from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
# from UI.mainwindow import MainWindow
from UI.loginMainWindow import loginMainWindow
import sys
import helper

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # mainWindow = MainWindow()
    # # psblack.css has set the color of QPalette, but not work
    # palette = QtGui.QPalette()
    # palette.setColor(mainWindow.backgroundRole(), QtGui.QColor(68, 68, 68))
    #
    # mainWindow.setPalette(palette)
    # mainWindow.setFont(QtGui.QFont("Microsoft Yahei", 11))
    # mainWindow.setWindowTitle("Mine Information Management Platform")
    # styleFile = './UI/resource/qss/psblack.css'
    # Style = helper.Helper.readQss(styleFile)
    # mainWindow.setStyleSheet(Style)
    # mainWindow.show()
    # sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = loginMainWindow()
    palette = QtGui.QPalette()
    palette.setColor(mainWindow.backgroundRole(), QtGui.QColor(255, 255, 255))

    mainWindow.setPalette(palette)
    mainWindow.setFont(QtGui.QFont("Times New Roman", 12))  # Microsoft Yahei
    mainWindow.setWindowTitle("Mine Information Management Platform")
    # styleFile = './UI/resource/qss/psblack.css'
    # Style = helper.Helper.readQss(styleFile)
    # mainWindow.setStyleSheet(Style)
    mainWindow.show()
    sys.exit(app.exec_())
