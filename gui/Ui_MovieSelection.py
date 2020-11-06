# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\_Prj\FileSort\gui/MovieSelection.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1403, 828)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblOriginalFile = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblOriginalFile.setFont(font)
        self.lblOriginalFile.setObjectName("lblOriginalFile")
        self.verticalLayout.addWidget(self.lblOriginalFile)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tablePossibilities = QtWidgets.QTableWidget(self.groupBox)
        self.tablePossibilities.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablePossibilities.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablePossibilities.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablePossibilities.setObjectName("tablePossibilities")
        self.tablePossibilities.setColumnCount(2)
        self.tablePossibilities.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablePossibilities.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePossibilities.setHorizontalHeaderItem(1, item)
        self.tablePossibilities.horizontalHeader().setDefaultSectionSize(300)
        self.gridLayout_2.addWidget(self.tablePossibilities, 0, 0, 1, 2)
        self.btnEnterId = QtWidgets.QPushButton(self.groupBox)
        self.btnEnterId.setObjectName("btnEnterId")
        self.gridLayout_2.addWidget(self.btnEnterId, 1, 0, 1, 1)
        self.btnEnterTitle = QtWidgets.QPushButton(self.groupBox)
        self.btnEnterTitle.setObjectName("btnEnterTitle")
        self.gridLayout_2.addWidget(self.btnEnterTitle, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.btnAccept = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAccept.setObjectName("btnAccept")
        self.gridLayout.addWidget(self.btnAccept, 2, 0, 1, 1)
        self.txtOverview = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.txtOverview.setObjectName("txtOverview")
        self.gridLayout.addWidget(self.txtOverview, 1, 1, 1, 1)
        self.lblTitle = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select"))
        self.lblOriginalFile.setText(_translate("Dialog", "Original File"))
        item = self.tablePossibilities.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tablePossibilities.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Year"))
        self.btnEnterId.setText(_translate("Dialog", "Enter ID"))
        self.btnEnterTitle.setText(_translate("Dialog", "Enter Title"))
        self.btnAccept.setText(_translate("Dialog", "Accept"))
        self.lblTitle.setText(_translate("Dialog", "Title"))
        self.label.setText(_translate("Dialog", "Information by The Movie Database (tmdb.org)"))
