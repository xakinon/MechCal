# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WinPython\workspace\MechCal\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_conditions_xyz = QtWidgets.QWidget()
        self.tab_conditions_xyz.setObjectName("tab_conditions_xyz")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_conditions_xyz)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab_conditions_xyz)
        self.groupBox.setMaximumSize(QtCore.QSize(420, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_caliculate_xyz = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_caliculate_xyz.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_caliculate_xyz.setObjectName("pushButton_caliculate_xyz")
        self.horizontalLayout_3.addWidget(self.pushButton_caliculate_xyz)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.checkBox_calculate_x = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_calculate_x.setObjectName("checkBox_calculate_x")
        self.horizontalLayout_3.addWidget(self.checkBox_calculate_x)
        self.checkBox_calculate_y = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_calculate_y.setObjectName("checkBox_calculate_y")
        self.horizontalLayout_3.addWidget(self.checkBox_calculate_y)
        self.checkBox_calculate_z = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_calculate_z.setObjectName("checkBox_calculate_z")
        self.horizontalLayout_3.addWidget(self.checkBox_calculate_z)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableView_caliculate_xyz1 = QtWidgets.QTableView(self.groupBox)
        self.tableView_caliculate_xyz1.setObjectName("tableView_caliculate_xyz1")
        self.verticalLayout_2.addWidget(self.tableView_caliculate_xyz1)
        self.horizontalLayout_7.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_conditions_xyz, "")
        self.tab_move_simulation = QtWidgets.QWidget()
        self.tab_move_simulation.setObjectName("tab_move_simulation")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_move_simulation)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_move_simulation)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 300))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableView_move_parameter = QtWidgets.QTableView(self.groupBox_2)
        self.tableView_move_parameter.setObjectName("tableView_move_parameter")
        self.tableView_move_parameter.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_8.addWidget(self.tableView_move_parameter)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_move_simulation)
        self.groupBox_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add_coordinate = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_add_coordinate.setObjectName("pushButton_add_coordinate")
        self.horizontalLayout.addWidget(self.pushButton_add_coordinate)
        self.pushButton_delete_coordinate = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_delete_coordinate.setObjectName("pushButton_delete_coordinate")
        self.horizontalLayout.addWidget(self.pushButton_delete_coordinate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_20.addLayout(self.horizontalLayout)
        self.tableView_move_coodinates = QtWidgets.QTableView(self.groupBox_3)
        self.tableView_move_coodinates.setObjectName("tableView_move_coodinates")
        self.tableView_move_coodinates.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_20.addWidget(self.tableView_move_coodinates)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_position_z = QtWidgets.QGroupBox(self.tab_move_simulation)
        self.groupBox_position_z.setObjectName("groupBox_position_z")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.groupBox_position_z)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_position_z = QtWidgets.QVBoxLayout()
        self.verticalLayout_position_z.setObjectName("verticalLayout_position_z")
        self.verticalLayout_21.addLayout(self.verticalLayout_position_z)
        self.gridLayout_2.addWidget(self.groupBox_position_z, 0, 1, 1, 1)
        self.groupBox_position_xyz = QtWidgets.QGroupBox(self.tab_move_simulation)
        self.groupBox_position_xyz.setObjectName("groupBox_position_xyz")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_position_xyz)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_position_xyz = QtWidgets.QVBoxLayout()
        self.verticalLayout_position_xyz.setObjectName("verticalLayout_position_xyz")
        self.verticalLayout_14.addLayout(self.verticalLayout_position_xyz)
        self.gridLayout_2.addWidget(self.groupBox_position_xyz, 0, 0, 1, 1)
        self.groupBox_position_x = QtWidgets.QGroupBox(self.tab_move_simulation)
        self.groupBox_position_x.setObjectName("groupBox_position_x")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.groupBox_position_x)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_position_x = QtWidgets.QVBoxLayout()
        self.verticalLayout_position_x.setObjectName("verticalLayout_position_x")
        self.verticalLayout_22.addLayout(self.verticalLayout_position_x)
        self.gridLayout_2.addWidget(self.groupBox_position_x, 1, 0, 1, 1)
        self.groupBox_position_y = QtWidgets.QGroupBox(self.tab_move_simulation)
        self.groupBox_position_y.setObjectName("groupBox_position_y")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.groupBox_position_y)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_position_y = QtWidgets.QVBoxLayout()
        self.verticalLayout_position_y.setObjectName("verticalLayout_position_y")
        self.verticalLayout_23.addLayout(self.verticalLayout_position_y)
        self.gridLayout_2.addWidget(self.groupBox_position_y, 1, 1, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.tab_move_simulation, "")
        self.tab_search_xyz = QtWidgets.QWidget()
        self.tab_search_xyz.setObjectName("tab_search_xyz")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_search_xyz)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_search_xyz)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_13.addWidget(self.comboBox)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_13.addWidget(self.plainTextEdit)
        self.horizontalLayout_4.addWidget(self.groupBox_7)
        self.tableView_caliculate_result_x = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_caliculate_result_x.setObjectName("tableView_caliculate_result_x")
        self.tableView_caliculate_result_x.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalLayout_4.addWidget(self.tableView_caliculate_result_x)
        self.verticalLayout_12.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_search_xyz)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_16.addWidget(self.comboBox_2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_8)
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_16.addWidget(self.plainTextEdit_2)
        self.horizontalLayout_5.addWidget(self.groupBox_8)
        self.tableView_caliculate_result_y = QtWidgets.QTableView(self.groupBox_5)
        self.tableView_caliculate_result_y.setObjectName("tableView_caliculate_result_y")
        self.tableView_caliculate_result_y.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalLayout_5.addWidget(self.tableView_caliculate_result_y)
        self.verticalLayout_12.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_search_xyz)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_9.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_17.addWidget(self.comboBox_3)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox_9)
        self.plainTextEdit_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_17.addWidget(self.plainTextEdit_3)
        self.horizontalLayout_6.addWidget(self.groupBox_9)
        self.tableView_caliculate_result_z = QtWidgets.QTableView(self.groupBox_6)
        self.tableView_caliculate_result_z.setObjectName("tableView_caliculate_result_z")
        self.tableView_caliculate_result_z.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalLayout_6.addWidget(self.tableView_caliculate_result_z)
        self.verticalLayout_12.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.tab_search_xyz, "")
        self.tab_ballscrew = QtWidgets.QWidget()
        self.tab_ballscrew.setObjectName("tab_ballscrew")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_ballscrew)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tableView_ballscrew = QtWidgets.QTableView(self.tab_ballscrew)
        self.tableView_ballscrew.setObjectName("tableView_ballscrew")
        self.tableView_ballscrew.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_9.addWidget(self.tableView_ballscrew)
        self.tabWidget.addTab(self.tab_ballscrew, "")
        self.tab_motor = QtWidgets.QWidget()
        self.tab_motor.setObjectName("tab_motor")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_motor)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView_motor = QtWidgets.QTableView(self.tab_motor)
        self.tableView_motor.setObjectName("tableView_motor")
        self.tableView_motor.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_4.addWidget(self.tableView_motor)
        self.tabWidget.addTab(self.tab_motor, "")
        self.tab_coupling = QtWidgets.QWidget()
        self.tab_coupling.setObjectName("tab_coupling")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_coupling)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableView_coupling = QtWidgets.QTableView(self.tab_coupling)
        self.tableView_coupling.setObjectName("tableView_coupling")
        self.tableView_coupling.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_7.addWidget(self.tableView_coupling)
        self.tabWidget.addTab(self.tab_coupling, "")
        self.tab_linearguide = QtWidgets.QWidget()
        self.tab_linearguide.setObjectName("tab_linearguide")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_linearguide)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableView_linearguide = QtWidgets.QTableView(self.tab_linearguide)
        self.tableView_linearguide.setObjectName("tableView_linearguide")
        self.tableView_linearguide.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_5.addWidget(self.tableView_linearguide)
        self.tabWidget.addTab(self.tab_linearguide, "")
        self.tab_supportunit = QtWidgets.QWidget()
        self.tab_supportunit.setObjectName("tab_supportunit")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_supportunit)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableView_supportunit = QtWidgets.QTableView(self.tab_supportunit)
        self.tableView_supportunit.setObjectName("tableView_supportunit")
        self.tableView_supportunit.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_6.addWidget(self.tableView_supportunit)
        self.tabWidget.addTab(self.tab_supportunit, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XYZシミュレーション"))
        self.groupBox.setTitle(_translate("MainWindow", "計算条件"))
        self.pushButton_caliculate_xyz.setText(_translate("MainWindow", "計算"))
        self.label.setText(_translate("MainWindow", "計算対象の軸"))
        self.checkBox_calculate_x.setText(_translate("MainWindow", "X"))
        self.checkBox_calculate_y.setText(_translate("MainWindow", "Y"))
        self.checkBox_calculate_z.setText(_translate("MainWindow", "Z"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_conditions_xyz), _translate("MainWindow", "計算条件XYZ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "速度パラメーター"))
        self.groupBox_3.setTitle(_translate("MainWindow", "動作パターン"))
        self.pushButton_add_coordinate.setText(_translate("MainWindow", "追加"))
        self.pushButton_delete_coordinate.setText(_translate("MainWindow", "削除"))
        self.groupBox_position_z.setTitle(_translate("MainWindow", "Z軸 時間-速度グラフ"))
        self.groupBox_position_xyz.setTitle(_translate("MainWindow", "XY位置"))
        self.groupBox_position_x.setTitle(_translate("MainWindow", "X軸 時間-速度グラフ"))
        self.groupBox_position_y.setTitle(_translate("MainWindow", "Y軸 時間-速度グラフ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_move_simulation), _translate("MainWindow", "動作シミュレーション"))
        self.groupBox_4.setTitle(_translate("MainWindow", "X"))
        self.groupBox_7.setTitle(_translate("MainWindow", "絞り込み"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Y"))
        self.groupBox_8.setTitle(_translate("MainWindow", "絞り込み"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Z"))
        self.groupBox_9.setTitle(_translate("MainWindow", "絞り込み"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search_xyz), _translate("MainWindow", "検索結果XYZ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ballscrew), _translate("MainWindow", "ボールねじ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_motor), _translate("MainWindow", "モーター"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_coupling), _translate("MainWindow", "カップリング"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linearguide), _translate("MainWindow", "リニアガイド"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_supportunit), _translate("MainWindow", "サポートユニット"))

