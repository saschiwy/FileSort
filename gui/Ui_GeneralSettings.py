# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\_Prj\FileSort\gui/GeneralSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(655, 757)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtLang = QtWidgets.QLineEdit(self.groupBox)
        self.txtLang.setObjectName("txtLang")
        self.horizontalLayout.addWidget(self.txtLang)
        self.cbxLang = QtWidgets.QComboBox(self.groupBox)
        self.cbxLang.setObjectName("cbxLang")
        self.horizontalLayout.addWidget(self.cbxLang)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chkOverwrite = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkOverwrite.setToolTip("")
        self.chkOverwrite.setStatusTip("")
        self.chkOverwrite.setWhatsThis("")
        self.chkOverwrite.setTristate(False)
        self.chkOverwrite.setObjectName("chkOverwrite")
        self.verticalLayout_3.addWidget(self.chkOverwrite)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.lstIgnore = QtWidgets.QListWidget(self.groupBox_3)
        self.lstIgnore.setObjectName("lstIgnore")
        self.gridLayout.addWidget(self.lstIgnore, 0, 0, 1, 2)
        self.btnIgnoreAdd = QtWidgets.QPushButton(self.groupBox_3)
        self.btnIgnoreAdd.setObjectName("btnIgnoreAdd")
        self.gridLayout.addWidget(self.btnIgnoreAdd, 1, 0, 1, 1)
        self.btnIgnoreRemove = QtWidgets.QPushButton(self.groupBox_3)
        self.btnIgnoreRemove.setObjectName("btnIgnoreRemove")
        self.gridLayout.addWidget(self.btnIgnoreRemove, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General Settings"))
        self.groupBox.setTitle(_translate("Dialog", "Database Settings"))
        self.label.setText(_translate("Dialog", "Database Language:"))
        self.groupBox_2.setTitle(_translate("Dialog", "File Settings"))
        self.chkOverwrite.setText(_translate("Dialog", "Overwrite files"))
        self.groupBox_3.setTitle(_translate("Dialog", "Ignore Files"))
        self.btnIgnoreAdd.setText(_translate("Dialog", "Add"))
        self.btnIgnoreRemove.setText(_translate("Dialog", "Remove"))
