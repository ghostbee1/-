# Form implementation generated from reading ui file 'rename_.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog6(object):
    def setupUi(self, Dialog6):
        Dialog6.setObjectName("Dialog6")
        Dialog6.setEnabled(True)
        Dialog6.resize(340, 278)
        Dialog6.setMaximumSize(QtCore.QSize(340, 278))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sourse/rename1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog6.setWindowIcon(icon)
        Dialog6.setStyleSheet("")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog6)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(250, 210, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText('取消并清空')
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setText('确认重命名')

        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog6)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(70, 200, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog6)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 240, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=Dialog6)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-20, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(88, 88, 88);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog6)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(-10, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(33, 144, 25);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog6)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 321, 111))
        self.textEdit.setToolTip("")
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.radioButton = QtWidgets.QRadioButton(parent=Dialog6)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(30, 170, 121, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=Dialog6)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 170, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=Dialog6)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 170, 121, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.toolButton = QtWidgets.QToolButton(parent=Dialog6)
        self.toolButton.setEnabled(True)
        self.toolButton.setGeometry(QtCore.QRect(289, 121, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.toolButton.setFont(font)
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("sourse/icon1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(25, 25))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog6)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 61, 41))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog6)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 120, 221, 41))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(32767)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)

        self.retranslateUi(Dialog6)
        self.buttonBox.rejected.connect(self.lineEdit.clear) # type: ignore
        self.pushButton.clicked.connect(self.radioButton_3.click) # type: ignore
        self.pushButton.clicked.connect(self.lineEdit.clear) # type: ignore
        self.pushButton.clicked.connect(self.lineEdit_2.clear) # type: ignore
        self.pushButton.clicked.connect(self.textEdit.clear) # type: ignore
        self.buttonBox.rejected.connect(self.lineEdit_2.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog6)

    def retranslateUi(self, Dialog6):
        _translate = QtCore.QCoreApplication.translate
        Dialog6.setWindowTitle(_translate("Dialog6", "批量重命名@ghost_bee"))
        self.lineEdit.setPlaceholderText(_translate("Dialog6", "-输入原名称/前缀-"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog6", "-输入新名称/后缀-"))
        self.label.setToolTip(_translate("Dialog6", "<html><head/><body><p>快捷键ALT+O,焦点切换至旧名称输入<br/></p></body></html>"))
        self.label.setText(_translate("Dialog6", "旧名(&O):"))
        self.label_2.setToolTip(_translate("Dialog6", "<html><head/><body><p>快捷键ALT+N,焦点切换至新名称输入</p></body></html>"))
        self.label_2.setText(_translate("Dialog6", "新名(&N):"))
        self.radioButton.setToolTip(_translate("Dialog6", "从左开始匹配字符"))
        self.radioButton.setText(_translate("Dialog6", "前缀替换"))
        self.radioButton_2.setToolTip(_translate("Dialog6", "只改名称，不转格式"))
        self.radioButton_2.setText(_translate("Dialog6", "后缀替换"))
        self.radioButton_3.setToolTip(_translate("Dialog6", "匹配字符全替换，支持文件夹改名"))
        self.radioButton_3.setText(_translate("Dialog6", "任意替换"))
        self.pushButton.setText(_translate("Dialog6", "重置清屏"))
        self.lineEdit_3.setToolTip(_translate("Dialog6", "路径显示"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog6", "                        当前文件夹选择路径："))
