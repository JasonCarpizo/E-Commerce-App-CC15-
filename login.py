# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 550)
        Dialog.setMinimumSize(QtCore.QSize(480, 550))
        Dialog.setMaximumSize(QtCore.QSize(480, 550))
        Dialog.setSizeIncrement(QtCore.QSize(480, 620))
        Dialog.setBaseSize(QtCore.QSize(480, 620))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 170, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"color: rgb(220, 29, 36);")
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 240, 311, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.username = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        self.username.setStyleSheet("color: rgb(0, 0, 0);")
        self.username.setObjectName("username")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.username)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(220, 29, 36);\n"
"font: 10pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(80, 290, 311, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.password = QtWidgets.QTextEdit(parent=self.formLayoutWidget_2)
        self.password.setStyleSheet("color: rgb(0, 0, 0);")
        self.password.setObjectName("password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(220, 29, 36);\n"
"font: 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.registerButton = QtWidgets.QPushButton(parent=Dialog)
        self.registerButton.setGeometry(QtCore.QRect(290, 370, 101, 31))
        self.registerButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(85, 0, 0);\n"
"background-color: rgb(220, 29, 36);")
        self.registerButton.setObjectName("registerButton")
        self.loginButton = QtWidgets.QPushButton(parent=Dialog)
        self.loginButton.setGeometry(QtCore.QRect(180, 370, 101, 31))
        self.loginButton.setStyleSheet("\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(220, 29, 36);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.usertype = QtWidgets.QComboBox(parent=Dialog)
        self.usertype.setGeometry(QtCore.QRect(80, 370, 91, 31))
        self.usertype.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(220, 29, 36);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.usertype.setEditable(True)
        self.usertype.setObjectName("usertype")
        self.usertype.addItem("")
        self.usertype.addItem("")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 430, 351, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"color: rgb(220, 29, 36);\n"
"font: 12pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 321, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/bonethugz/Downloads/ngyopify_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " Login"))
        self.label_2.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.registerButton.setText(_translate("Dialog", "REGISTER"))
        self.loginButton.setText(_translate("Dialog", "LOGIN"))
        self.usertype.setItemText(0, _translate("Dialog", "Customer"))
        self.usertype.setItemText(1, _translate("Dialog", "Seller"))
        self.label_5.setText(_translate("Dialog", "Tip: Make sure to have a registered account first!"))
