# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\С����\Monkey\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os
import re
import time
import threading

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(720, 599)
		font = QtGui.QFont()
		font.setPointSize(11)
		Dialog.setFont(font)
		Dialog.setSizeGripEnabled(True)
		self.groupBox = QtGui.QGroupBox(Dialog)
		self.groupBox.setGeometry(QtCore.QRect(20, 30, 361, 101))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.groupBox.setFont(font)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.layoutWidget = QtGui.QWidget(self.groupBox)
		self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 61))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.comboBox = QtGui.QComboBox(self.layoutWidget)
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.verticalLayout.addWidget(self.comboBox)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.label_2 = QtGui.QLabel(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_2.setFont(font)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.verticalLayout_2.addWidget(self.label_2)
		self.comboBox_2 = QtGui.QComboBox(self.layoutWidget)
		self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
		self.comboBox_2.addItem(_fromUtf8(""))
		self.comboBox_2.addItem(_fromUtf8(""))
		self.comboBox_2.addItem(_fromUtf8(""))
		self.verticalLayout_2.addWidget(self.comboBox_2)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.groupBox_4 = QtGui.QGroupBox(Dialog)
		self.groupBox_4.setGeometry(QtCore.QRect(430, 390, 271, 181))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.groupBox_4.setFont(font)
		self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
		self.layoutWidget1 = QtGui.QWidget(self.groupBox_4)
		self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 161, 151))
		self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
		self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget1)
		self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
		self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget1)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.checkBox_2.setFont(font)
		self.checkBox_2.setChecked(True)
		self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
		self.verticalLayout_5.addWidget(self.checkBox_2)
		self.checkBox_1 = QtGui.QCheckBox(self.layoutWidget1)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.checkBox_1.setFont(font)
		self.checkBox_1.setChecked(True)
		self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
		self.verticalLayout_5.addWidget(self.checkBox_1)
		self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget1)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.checkBox_3.setFont(font)
		self.checkBox_3.setChecked(True)
		self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
		self.verticalLayout_5.addWidget(self.checkBox_3)
		self.checkBox_5 = QtGui.QCheckBox(self.layoutWidget1)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.checkBox_5.setFont(font)
		self.checkBox_5.setChecked(True)
		self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
		self.verticalLayout_5.addWidget(self.checkBox_5)
		self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget1)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.checkBox_4.setFont(font)
		self.checkBox_4.setChecked(True)
		self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
		self.verticalLayout_5.addWidget(self.checkBox_4)
		self.checkBox_6 = QtGui.QCheckBox(self.layoutWidget1)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.checkBox_6.setFont(font)
		self.checkBox_6.setChecked(True)
		self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
		self.verticalLayout_5.addWidget(self.checkBox_6)
		self.groupBox_3 = QtGui.QGroupBox(Dialog)
		self.groupBox_3.setGeometry(QtCore.QRect(430, 150, 271, 231))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.groupBox_3.setFont(font)
		self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
		self.layoutWidget2 = QtGui.QWidget(self.groupBox_3)
		self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 254, 201))
		self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.verticalLayout_6 = QtGui.QVBoxLayout()
		self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
		self.verticalLayout_8 = QtGui.QVBoxLayout()
		self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
		self.label_6 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_6.setFont(font)
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.verticalLayout_8.addWidget(self.label_6)
		self.label_7 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_7.setFont(font)
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.verticalLayout_8.addWidget(self.label_7)
		self.label_8 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_8.setFont(font)
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.verticalLayout_8.addWidget(self.label_8)
		self.label_9 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_9.setFont(font)
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.verticalLayout_8.addWidget(self.label_9)
		self.label_10 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_10.setFont(font)
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.verticalLayout_8.addWidget(self.label_10)
		self.label_11 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_11.setFont(font)
		self.label_11.setObjectName(_fromUtf8("label_11"))
		self.verticalLayout_8.addWidget(self.label_11)
		self.label_13 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_13.setFont(font)
		self.label_13.setObjectName(_fromUtf8("label_13"))
		self.verticalLayout_8.addWidget(self.label_13)
		self.label_12 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_12.setFont(font)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.verticalLayout_8.addWidget(self.label_12)
		self.verticalLayout_6.addLayout(self.verticalLayout_8)
		self.horizontalLayout_3.addLayout(self.verticalLayout_6)
		self.verticalLayout_7 = QtGui.QVBoxLayout()
		self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
		self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setText(_fromUtf8(""))
		self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
		self.verticalLayout_7.addWidget(self.lineEdit_4)
		self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_5.setFont(font)
		self.lineEdit_5.setText(_fromUtf8(""))
		self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
		self.verticalLayout_7.addWidget(self.lineEdit_5)
		self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_6.setFont(font)
		self.lineEdit_6.setText(_fromUtf8(""))
		self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
		self.verticalLayout_7.addWidget(self.lineEdit_6)
		self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_7.setFont(font)
		self.lineEdit_7.setText(_fromUtf8(""))
		self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
		self.verticalLayout_7.addWidget(self.lineEdit_7)
		self.lineEdit_8 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_8.setFont(font)
		self.lineEdit_8.setText(_fromUtf8(""))
		self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
		self.verticalLayout_7.addWidget(self.lineEdit_8)
		self.lineEdit_9 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_9.setFont(font)
		self.lineEdit_9.setText(_fromUtf8(""))
		self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
		self.verticalLayout_7.addWidget(self.lineEdit_9)
		self.lineEdit_10 = QtGui.QLineEdit(self.layoutWidget2)
		self.lineEdit_11 = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lineEdit_10.setFont(font)
		self.lineEdit_10.setText(_fromUtf8(""))
		self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
		self.verticalLayout_7.addWidget(self.lineEdit_10)
		self.lineEdit_11.setFont(font)
		self.lineEdit_11.setText(_fromUtf8(""))
		self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
		self.verticalLayout_7.addWidget(self.lineEdit_11)
		self.horizontalLayout_3.addLayout(self.verticalLayout_7)
		self.groupBox_2 = QtGui.QGroupBox(Dialog)
		self.groupBox_2.setGeometry(QtCore.QRect(430, 30, 271, 111))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.groupBox_2.setFont(font)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.layoutWidget3 = QtGui.QWidget(self.groupBox_2)
		self.layoutWidget3.setGeometry(QtCore.QRect(13, 20, 247, 81))
		self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget3)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.verticalLayout_4 = QtGui.QVBoxLayout()
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.label_3 = QtGui.QLabel(self.layoutWidget3)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.verticalLayout_4.addWidget(self.label_3)
		self.label_4 = QtGui.QLabel(self.layoutWidget3)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.verticalLayout_4.addWidget(self.label_4)
		self.label_5 = QtGui.QLabel(self.layoutWidget3)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.verticalLayout_4.addWidget(self.label_5)
		self.horizontalLayout_2.addLayout(self.verticalLayout_4)
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.lineEdit = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.verticalLayout_3.addWidget(self.lineEdit)
		self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.verticalLayout_3.addWidget(self.lineEdit_2)
		self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
		self.verticalLayout_3.addWidget(self.lineEdit_3)
		self.horizontalLayout_2.addLayout(self.verticalLayout_3)
		self.groupBox_5 = QtGui.QGroupBox(Dialog)
		self.groupBox_5.setGeometry(QtCore.QRect(20, 140, 371, 381))
		self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
		self.widget = QtGui.QWidget(self.groupBox_5)
		self.widget.setGeometry(QtCore.QRect(10, 20, 351, 351))
		self.widget.setObjectName(_fromUtf8("widget"))
		self.verticalLayout_9 = QtGui.QVBoxLayout(self.widget)
		self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.radioButton = QtGui.QRadioButton(self.widget)
		self.radioButton.setChecked(True)
		self.radioButton.setObjectName(_fromUtf8("radioButton"))
		self.buttonGroup = QtGui.QButtonGroup(Dialog)
		self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
		self.buttonGroup.addButton(self.radioButton)
		self.horizontalLayout_4.addWidget(self.radioButton)
		self.radioButton_4 = QtGui.QRadioButton(self.widget)
		self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
		self.buttonGroup.addButton(self.radioButton_4)
		self.horizontalLayout_4.addWidget(self.radioButton_4)
		self.radioButton_2 = QtGui.QRadioButton(self.widget)
		self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
		self.buttonGroup.addButton(self.radioButton_2)
		self.horizontalLayout_4.addWidget(self.radioButton_2)
		self.radioButton_3 = QtGui.QRadioButton(self.widget)
		self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
		self.buttonGroup.addButton(self.radioButton_3)
		self.horizontalLayout_4.addWidget(self.radioButton_3)
		self.verticalLayout_9.addLayout(self.horizontalLayout_4)
		self.listWidget = QtGui.QListWidget(self.widget)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.verticalLayout_9.addWidget(self.listWidget)
		self.horizontalLayout_5 = QtGui.QHBoxLayout()
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.pushButton_3 = QtGui.QPushButton(self.widget)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.horizontalLayout_5.addWidget(self.pushButton_3)
		self.pushButton_5 = QtGui.QPushButton(self.widget)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.horizontalLayout_5.addWidget(self.pushButton_5)
		self.pushButton_4 = QtGui.QPushButton(self.widget)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.horizontalLayout_5.addWidget(self.pushButton_4)
		self.verticalLayout_9.addLayout(self.horizontalLayout_5)
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(10, 530, 241, 61))
		font = QtGui.QFont()
		font.setPointSize(26)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(260, 530, 151, 61))
		font = QtGui.QFont()
		font.setPointSize(17)
		font.setBold(False)
		font.setWeight(50)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.runMonkey)
		QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.chooseSinglePackage)
		QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
		QtCore.QObject.connect(self.checkBox_1, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
		QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
		QtCore.QObject.connect(self.checkBox_5, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
		QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
		QtCore.QObject.connect(self.checkBox_6, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_6, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_8, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_9, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_10, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_11, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.open)
		QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.singalMode)
		QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.whiteListMode)
		QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.blackListMode)
		QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.allMode)
		QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.theTest)
		QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.updataPackage)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.updataDevices)
		QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectAll)
		QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectNone)
		QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectSwap)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.groupBox.setTitle(_translate("Dialog", "测试设备", None))
		self.label.setText(_translate("Dialog", "设备名称：", None))
		self.label_2.setText(_translate("Dialog", "日志类型：", None))
		self.comboBox_2.setItemText(0, _translate("Dialog", "Level 3", None))
		self.comboBox_2.setItemText(1, _translate("Dialog", "Level 2", None))
		self.comboBox_2.setItemText(2, _translate("Dialog", "Level 1", None))
		self.groupBox_4.setTitle(_translate("Dialog", "调试", None))
		self.checkBox_2.setText(_translate("Dialog", "忽略Crash", None))
		self.checkBox_1.setText(_translate("Dialog", "忽略ANR", None))
		self.checkBox_3.setText(_translate("Dialog", "忽略许可证异常", None))
		self.checkBox_5.setText(_translate("Dialog", "忽略本地代码崩溃", None))
		self.checkBox_4.setText(_translate("Dialog", "监视代码崩溃事件", None))
		self.checkBox_6.setText(_translate("Dialog", "错误后停止该进程", None))
		self.groupBox_3.setTitle(_translate("Dialog", "设置事件百分比", None))
		self.label_6.setText(_translate("Dialog", "触摸事件:", None))
		self.label_7.setText(_translate("Dialog", "动作事件:", None))
		self.label_8.setText(_translate("Dialog", "轨迹事件:", None))
		self.label_9.setText(_translate("Dialog", "基本导航:", None))
		self.label_10.setText(_translate("Dialog", "主要导航:", None))
		self.label_11.setText(_translate("Dialog", "系统按键:", None))
		self.label_13.setText(_translate("Dialog", "其他事件:", None))
		self.label_12.setText(_translate("Dialog", "启动活动:", None))
		self.groupBox_2.setTitle(_translate("Dialog", "基本设置", None))
		self.label_3.setText(_translate("Dialog", "事件数:", None))
		self.label_4.setText(_translate("Dialog", "延迟:", None))
		self.label_5.setText(_translate("Dialog", "伪随机数:", None))
		self.lineEdit.setText(_translate("Dialog", "3000000", None))
		self.lineEdit_2.setText(_translate("Dialog", "1000", None))
		self.groupBox_5.setTitle(_translate("Dialog", "测试模式", None))
		self.radioButton.setText(_translate("Dialog", "全模块", None))
		self.radioButton_4.setText(_translate("Dialog", "黑名单", None))
		self.radioButton_2.setText(_translate("Dialog", "白名单", None))
		self.radioButton_3.setText(_translate("Dialog", "单模块", None))
		self.pushButton_3.setText(_translate("Dialog", "全选", None))
		self.pushButton_5.setText(_translate("Dialog", "反选", None))
		self.pushButton_4.setText(_translate("Dialog", "取消", None))
		self.pushButton.setText(_translate("Dialog", "开始执行", None))
		self.pushButton_2.setText(_translate("Dialog", "刷新设备列表", None))

	changeListWidget = []

	def theTest(self):
		pass

	def allMode(self):
		self.__clearJokeStr()
		self.disUseListWidget()

	def blackListMode(self):
		self.__clearJokeStr()
		self.useListWidget()

	def runBlackListMode(self):
		with open("blacklist.txt",'w') as file:
			for x in xrange(self.listWidget.count()):
				if self.listWidget.item(x).checkState() == 2:
					file.write('%s\n'%self.listWidget.item(x).text())

	def runWhiteListMode(self):
		with open("whitelist.txt",'w') as file:
			for x in xrange(self.listWidget.count()):
				if self.listWidget.item(x).checkState() == 2:
					file.write('%s\n'%self.listWidget.item(x).text())

	def runAllMode(self):
		pass

	def runSingalMode(self):
		pass

	def whiteListMode(self):
		self.__clearJokeStr()
		self.useListWidget()

	def singalMode(self):
		self.setButtonNoDisplay()
		self.setListWidgetDisplay()

	def __clearJokeStr(self):
		if self.changeListWidget:
			self.listWidget.item(self.changeListWidget[0]).setCheckState(0)
			self.listWidget.item(self.changeListWidget[0]).setText(self.changeListWidget[1])
			self.changeListWidget = []

	def chooseSinglePackage(self):
		if self.buttonGroup.checkedId() != -5:
			return
		self.selectNone()
		self.__clearJokeStr()
		row = self.listWidget.currentRow()
		text = self.listWidget.item(row).text()
		self.listWidget.item(row).setText(u'执行这个➤➤➤➤:%s'%text)
		self.changeListWidget = [row,text]

	def selectAll(self):
		for x in xrange(self.listWidget.count()):
			self.listWidget.item(x).setCheckState(2)

	def selectNone(self):
		for x in xrange(self.listWidget.count()):
			self.listWidget.item(x).setCheckState(0)

	def selectSwap(self):
		for x in xrange(self.listWidget.count()):
			if self.listWidget.item(x).checkState() == 2:
				self.listWidget.item(x).setCheckState(0)
			else:
				self.listWidget.item(x).setCheckState(2)

	def setButtonDisplay(self):
		self.pushButton_3.setEnabled(True)
		self.pushButton_4.setEnabled(True)
		self.pushButton_5.setEnabled(True)

	def setButtonNoDisplay(self):
		self.pushButton_3.setEnabled(False)
		self.pushButton_4.setEnabled(False)
		self.pushButton_5.setEnabled(False)

	def setListWidgetDisplay(self):
		self.listWidget.setEnabled(True)

	def setListWidgetNoDisplay(self):
		self.listWidget.setEnabled(False)

	def useListWidget(self):
		self.setListWidgetDisplay()
		self.setButtonDisplay()

	def disUseListWidget(self):
		self.setButtonNoDisplay()
		self.setListWidgetNoDisplay()

	def updataPackage(self):
		def __updataListWidgetItem():
			for text in os.popen('adb -s %s shell pm list package'%self.comboBox.currentText()).readlines():
				tmpItem = QtGui.QListWidgetItem(text[text.find(':') + 1:].strip('\n'))
				tmpItem.setCheckState(0)
				self.listWidget.addItem(tmpItem)
		t = threading.Thread(target = __updataListWidgetItem)
		t.setDaemon(True)
		self.listWidget.clear()
		t.start()

	def updataDevices(self):
		def __updataDevices():
			self.comboBox.clear()
			os.system('adb start-server')
			for id in [re.findall('^([A-Za-z0-9]*)\tdevice',text)[0] for text in os.popen('adb devices').readlines() if re.findall('^([A-Za-z0-9]*)\tdevice',text)]:self.comboBox.addItem(id)
		t = threading.Thread(target = __updataDevices)
		t.setDaemon(True)
		t.start()

	def getModeRunStr(self):
		def __copyFile(fileName):
			self.pushButton.setText(u'正在生成执行名单')
			os.system('adb -s %s.txt push fileName /storage/sdcard0/'%fileName)
			os.remove('%s.txt'%fileName)
			return 'monkey --pkg-%s-file /storage/sdcard0/%s.txt'%fileName
		tmp = self.buttonGroup.checkedId()
		if tmp == -3:
			self.runBlackListMode()
			return __copyFile('blacklist')
		elif tmp == -4:
			self.runWhiteListMode()
			return __copyFile('whitelist')
		elif tmp == -5:
			self.runSingalMode()
			return 'monkey -p %s'%self.changeListWidget[1].trimmed()
		else:
			self.runAllMode()
			return 'monkey'

	def isRightNumber(self,s):
		try:
			s = float(s)
			if s > 100 or s < 0:
				return False
			return True
		except ValueError:
			return False

	def checkEvent(self):
		listEdit = [u'触摸事件',u'动作事件',u'轨迹事件',u'基本导航',u'主要导航',u'系统按键',u'其他事件',u'启动活动']
		for x in xrange(4,12):
			if eval('self.lineEdit_%s.displayText()'%x):
				if not eval('self.isRightNumber(self.lineEdit_%s.displayText())'%x):
					QtGui.QMessageBox.critical(Dialog,u'要爆炸了',u'%s参数不正确'%listEdit[x - 4],u'知道错了')
					return False
		tmp = 0
		for x in xrange(4,12):
			if eval('self.lineEdit_%s.displayText()'%x):
				tmp += eval('float(self.lineEdit_%s.displayText())'%x)
		if tmp > 100:
			QtGui.QMessageBox.critical(Dialog,u'要爆炸了',u'事件参数太大',u'知道错了')
			return False
		return True

	def errorCheck(self):
		if not self.comboBox.currentText():
			QtGui.QMessageBox.critical(Dialog,u'要爆炸了',u'必须选择一个设备',u'知道错了')
			return False
		if not self.lineEdit.displayText():
			QtGui.QMessageBox.critical(Dialog,u'要爆炸了',u'必须设置事件数量',u'知道错了')
			return False
		if (self.buttonGroup.checkedId() == -5) and (not self.changeListWidget):
			QtGui.QMessageBox.critical(Dialog,u'要爆炸了',u'单模块啊！！起码选择一个模块啊',u'知道错了')
			return False
		if self.buttonGroup.checkedId() not in [-2,-3,-4,-5]:
			QtGui.QMessageBox.critical(Dialog,u'真·要爆炸了',u'点确定后程序会退出(错误代码0x00456)',u'确定')
			exit()
		if not self.checkEvent():
			print '22222222'
			return False
		return True

	def getThrottleTime(self):
		throttle = self.lineEdit_2.displayText()
		if throttle:
			return ' --throttle %s'%throttle
		return ''

	def getDebugMode(self):
		debugOptions = ['ignore-timeouts','ignore-crashes','ignore-security-exceptions','ignore-native-crashes','monitor-native-crashes','kill-process-after-error']
		tmpStr = ''
		for x in xrange(1,7):
			if eval('self.checkBox_%s.isChecked()'%x):
				tmpStr += ' --%s'%debugOptions[x - 1]
		return tmpStr

	def getLogLevel(self):
		tmpStr = ''
		for x in xrange(3 - self.comboBox_2.currentIndex()):
			tmpStr += ' -v'
		return tmpStr

	def getSeed(self):
		if self.lineEdit_3.displayText():
			return ' -s %s'%self.lineEdit_3.displayText()
		return ''

	def getEventStr(self):
		listEdit = ['--pct-touch','--pct-motion','--pct-trackball','--pct-nav','--pct-majornav','--pct-syskeys','--pct-anyevent','--pct-appswitch']
		tmpStr = ''
		for x in xrange(4,12):
			tmp = eval('self.lineEdit_%s.displayText()'%x)
			if tmp:
				tmpStr += ' %s %s'%(listEdit[x - 4],tmp)
		return tmpStr

	def runMonkey(self):
		self.pushButton.setEnabled(False)
		self.pushButton.setText(u'代码检查')
		if not self.errorCheck():
			self.pushButton.setEnabled(True)
			self.pushButton.setText(u'开始执行')
			return
		self.pushButton.setText(u'连接执行设备')
		runText = 'adb -s %s shell "'%self.comboBox.currentText()
		self.pushButton.setText(u'生成执行模式')
		runText += '%s'%self.getModeRunStr()
		self.pushButton.setText(u'生成执行间隔')
		runText += '%s'%self.getThrottleTime()
		self.pushButton.setText(u'设置Debug模式')
		runText += '%s'%self.getDebugMode()
		self.pushButton.setText(u'设置随机种子')
		runText += '%s'%self.getSeed()
		self.pushButton.setText(u'设置Log级别')
		runText += '%s'%self.getLogLevel()
		self.pushButton.setText(u'设置事件百分比')
		runText += self.getEventStr()
		self.pushButton.setText(u'设置事件数量')
		runText += ' %s'%self.lineEdit.displayText()
		self.pushButton.setText(u'设置Log存放')
		runText += ' >/storage/self/primary/%s.txt"'%self.comboBox.currentText()
		print runText
		t = threading.Thread(target = lambda:os.system(runText))
		t.setDaemon(True)
		t.start()

		self.pushButton.setEnabled(True)
		self.pushButton.setText(u'开始执行')



if __name__ == "__main__":
	import sys
	ui = Ui_Dialog()
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui.setupUi(Dialog)
	Dialog.show()
	ui.updataDevices()
	ui.disUseListWidget()
	sys.exit(app.exec_())

