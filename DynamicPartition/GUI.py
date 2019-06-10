# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import dynamic_partition

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 90, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 90, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_alg_choose = QtWidgets.QLabel(self.centralwidget)
        self.label_alg_choose.setGeometry(QtCore.QRect(10, 35, 181, 31))
        self.label_alg_choose.setStyleSheet("")
        self.label_alg_choose.setObjectName("label_alg_choose")
        self.label_allocate = QtWidgets.QLabel(self.centralwidget)
        self.label_allocate.setGeometry(QtCore.QRect(10, 180, 72, 15))
        self.label_allocate.setObjectName("label_allocate")
        self.pushButton_allocate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_allocate.setGeometry(QtCore.QRect(250, 230, 93, 31))
        self.pushButton_allocate.setObjectName("pushButton_allocate")
        self.label_release = QtWidgets.QLabel(self.centralwidget)
        self.label_release.setGeometry(QtCore.QRect(10, 330, 72, 15))
        self.label_release.setObjectName("label_release")
        self.pushButton_release = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_release.setGeometry(QtCore.QRect(250, 380, 93, 31))
        self.pushButton_release.setObjectName("pushButton_release")
        self.spinBox_release = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_release.setGeometry(QtCore.QRect(90, 380, 121, 31))
        self.spinBox_release.setObjectName("spinBox_release")
        self.spinBox_release.setMaximum(640)
        self.spinBox_release.setMinimum(1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 230, 31, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 380, 51, 31))
        self.label_3.setObjectName("label_3")
        self.spinBox_allocate = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_allocate.setGeometry(QtCore.QRect(90, 230, 121, 31))
        self.spinBox_allocate.setObjectName("spinBox_allocate")
        self.spinBox_allocate.setMaximum(640)
        self.spinBox_allocate.setSingleStep(10)
        self.spinBox_allocate.setValue(10)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(540, 10, 161, 640))
        self.tableWidget.setLineWidth(10)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        # self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 10, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 630, 72, 15))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.radioButton.toggled.connect(self.chooseFF)
        self.radioButton_2.toggled.connect(self.chooseBF)
        self.pushButton_allocate.clicked.connect(lambda:self.all(self.allocate,self.updateTable))
        self.pushButton_release.clicked.connect(lambda:self.rel(self.releasee,self.updateTable))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def all(self,a,b):
        a()
        b()

    def rel(self,a,b):
        a()
        b()

    def chooseFF(self):
        if self.radioButton.isChecked():
            DP.algorithmn=0
    def chooseBF(self):
        if self.radioButton_2.isChecked():
            DP.algorithmn=1

    def allocate(self):
        print(self.spinBox_allocate.value())
        if DP.algorithmn==0:
            print('chooseFF')
            print(DP.algorithmn)
            if DP.firstFit(len(DP.freeChain),self.spinBox_allocate.value()):
                print('FF allocate success')

        else:
            if DP.algorithmn==1:
                print('chooseBF')
                if DP.bestFit(len(DP.freeChain),self.spinBox_allocate.value()):
                   print('BF allocate success')


    def releasee(self):
        # print("release ready:")
        # print(self.pushButton_release.isChecked)
          DP.release(self.spinBox_release.value())
          print(self.spinBox_release.value())
          print('release success')


    def updateTable(self):
        print('ready to update')
        self.tableWidget.clearContents()
        rowNum=len(DP.freeChain)
        self.tableWidget.setRowCount(rowNum)
        self.tableWidget.resize(161,640)
        for i in range(rowNum):

            print(DP.freeChain[i].index,DP.freeChain[i].isUsed,DP.freeChain[i].position,DP.freeChain[i].size)
            self.tableWidget.setRowHeight(i,DP.freeChain[i].size)
            newItem = QtWidgets.QTableWidgetItem('index:'+str(DP.freeChain[i].index)+'  '+str(DP.freeChain[i].size))
            self.tableWidget.setItem(i,0, newItem)
            if DP.freeChain[i].isUsed==True:
                self.tableWidget.item(i, 0).setBackground(QtGui.QBrush(QtGui.QColor(255, 68, 68)))
            if DP.freeChain[i].index==0:
                self.tableWidget.item(i,0).setBackground(QtGui.QBrush(QtGui.QColor(0,255,255)))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                             Dynamic Partition"))
        self.radioButton.setText(_translate("MainWindow", "首次适应算法"))
        self.radioButton_2.setText(_translate("MainWindow", "最佳适应算法"))
        self.label_alg_choose.setText(_translate("MainWindow", "选择动态分区算法："))
        self.label_allocate.setText(_translate("MainWindow", "申请内存："))
        self.pushButton_allocate.setText(_translate("MainWindow", "申请"))
        self.label_release.setText(_translate("MainWindow", "释放内存："))
        self.pushButton_release.setText(_translate("MainWindow", "释放"))
        self.label.setText(_translate("MainWindow", "K"))
        self.label_2.setText(_translate("MainWindow", "大小："))
        self.label_3.setText(_translate("MainWindow", "块号："))
        self.label_4.setText(_translate("MainWindow", "0 "))
        self.label_5.setText(_translate("MainWindow", "640 K"))






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    DP = dynamic_partition.DynamicPartition()
    mainWindow.show()
    sys.exit(app.exec_())
