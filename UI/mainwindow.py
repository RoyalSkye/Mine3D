import os
import xlrd
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from UI.quicreator import Ui_QUICreator

class MainWindow(QMainWindow, Ui_QUICreator):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initTableWidget()

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