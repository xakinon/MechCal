# -*- coding: utf-8 -*-
import configparser
import csv
import math
import sys
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
#import qdarkstyle

from mainwindow import Ui_MainWindow
from tableViewModel import Model, Delegate
from calicurate import Calicurate

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        
        self.db_path = 'db.sqlite3'
        self.model = {}
        self.proxyModel = {}
        self.calculationConditions = {}

        # iniファイル読み込み
        self.iniflename = 'ini/settings.ini'
        self.inifile = configparser.ConfigParser()
        self.inifile.read(self.iniflename, encoding='utf8')

        # UI設定
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.dockWidget.hide()

        self.tableView_caliculate_xyz1_init()

        # 検索結果テーブル
        self.tableViewInit(self.ui.tableView_ballscrew, 'ballscrew')
        self.tableViewInit(self.ui.tableView_motor, 'servoMotor')
        self.tableViewInit(self.ui.tableView_coupling, 'coupling')
        self.tableViewInit(self.ui.tableView_supportunit, 'supportunit')
        self.tableViewInit(self.ui.tableView_linearguide, 'linearguide')
        self.tableViewInit(self.ui.tableView_caliculate_result_x, 'caliculate_result_x', True)
        self.tableViewInit(self.ui.tableView_caliculate_result_y, 'caliculate_result_y', True)
        self.tableViewInit(self.ui.tableView_caliculate_result_z, 'caliculate_result_z', True)
        self.tableViewInit(self.ui.tableView_move_coodinates, 'move_coodinates', False, self.refleshPlot)
        self.tableViewInit(self.ui.tableView_move_parameter, 'move_parameters', False)

        # 
        self.model['move_coodinates'].addColumns( self.inifile.get('move_coodinates','columns').splitlines() )
        self.model['move_coodinates'].editableColumns = range(len(self.model['move_coodinates'].columns))

        # データ読み込み
        self.ballscrews = self.loadDatasCsv(self.ui.tableView_ballscrew, 'ballscrew')
        self.servomotors = self.loadDatasCsv(self.ui.tableView_motor, 'servoMotor')
        self.couplings = self.loadDatasCsv(self.ui.tableView_coupling, 'coupling')

        # ツールチップ
        #self.ui.doubleSpinBox_load_coefficient.setToolTip(self.inifile.get('tooltips', 'doubleSpinBox_load_coefficient'))

        # イベントスロット
        self.ui.pushButton_caliculate_xyz.clicked.connect(self.calculateXYZ)
        self.ui.pushButton_add_coordinate.clicked.connect(self.add_move_coodinates)
        self.ui.pushButton_delete_coordinate.clicked.connect(self.delete_move_coodinates)
        #self.ui.plainTextEdit_narrow.textChanged.connect(self.filterChanged)
        #self.ui.comboBox_narrow.currentIndexChanged.connect(self.comboBoxCurrentIndexChanged)

        # グラフ設定
        self.plot_init()

        '''
    def filterChanged(self):
        regExp = QtCore.QRegExp( # 正規表現作成
            self.ui.plainTextEdit_narrow.toPlainText(), # 文字列
            QtCore.Qt.CaseSensitive, # 大文字、小文字を区別
            QtCore.QRegExp.RegExp2) # 文字列の扱い
        self.proxyModel['search'].setFilterRegExp(regExp) # 正規表現セット

    def comboBoxCurrentIndexChanged(self):
        if self.ui.comboBox_narrow.count() < 1:
            return # comboBoxにアイテムが無ければ何もしない
        keyIndex = self.model['search'].columns.index( self.ui.comboBox_narrow.currentText() )
        self.proxyModel['search'].setFilterKeyColumn( keyIndex )
        self.filterChanged()
        '''

    def refleshPlot(self):
        from plotXY import PlotXY
        PlotXY().refleshPlot(self.model['move_coodinates'], self.plotWidget)

    def plot_init(self):

        ui = self.ui
        self.plotWidget = { 'position_X':None, 'position_Y':None, 'position_Z':None, 'position_xyz':None }
        layouts = [ ui.verticalLayout_position_x, ui.verticalLayout_position_y, ui.verticalLayout_position_z, ui.verticalLayout_position_xyz ]
        groupBoxes = [ ui.groupBox_position_x, ui.groupBox_position_y, ui.groupBox_position_z, ui.groupBox_position_xyz ]

        for layout, groupBox, key in zip( layouts, groupBoxes, self.plotWidget ):
            self.plotWidget[key] = pg.PlotWidget(groupBox)
            self.plotWidget[key].setBackground("#FFFFFF00")
            self.plotWidget[key].getViewBox().setAspectLocked(lock=True, ratio=1)
            layout.addWidget(self.plotWidget[key])

    def add_move_coodinates(self):
        items = [{ 'X':'0.0', 'Y':'0.0', 'Z':'0.0' }]
        self.model['move_coodinates'].addItems(items)

    def delete_move_coodinates(self):
        # 選択中のセルが無ければ何もしない
        selectedIndexes = self.ui.tableView_move_coodinates.selectedIndexes()
        if len(selectedIndexes) < 1:
            return
        
        proxyModel = selectedIndexes[0].model()
        model = proxyModel.sourceModel()
        rows = [ proxyModel.mapToSource(selectedIndex).row() for selectedIndex in selectedIndexes ]
        for row in list(set(rows))[::-1]:
            model.removeItem(row)

    def calculateXYZ(self):

        def dict_(axis):
            # 指定したキーに一致するものはそれぞれ型変換して辞書にセット
            float_keys = ['ワーク質量', 'ストローク', '最高速度', '最高加速度', '摩擦抵抗', '荷重係数', '希望寿命時間']
            int_keys = ['支持条件入力側', '支持条件ナット部', '支持条件反対側']
            conditions = {}
            for dict_ in self.model['caliculate_xyz1'].items:
                if dict_['項目'] in float_keys:
                    conditions[dict_['項目']] = float(dict_[axis])
                    continue
                if dict_['項目'] in int_keys:
                    conditions[dict_['項目']] = int(dict_[axis])
                    continue
                conditions[dict_['項目']] = dict_[axis]
            return conditions
        
        def calicurate(axis, result_model_name, checkBox, groupBox):
            groupBox.hide()
            if checkBox.isChecked():
                calicurate = Calicurate(dict_(axis), self.ballscrews, self.servomotors, self.couplings)
                calicurate.commit()
                self.model[result_model_name].removeAllItems()
                self.model[result_model_name].addColumns(calicurate.columns)
                self.model[result_model_name].addItems(calicurate.dicts)
                groupBox.show()

        calicurate('X', 'caliculate_result_x', self.ui.checkBox_calculate_x, self.ui.groupBox_4)
        calicurate('Y', 'caliculate_result_y', self.ui.checkBox_calculate_y, self.ui.groupBox_5)
        calicurate('Z', 'caliculate_result_z', self.ui.checkBox_calculate_z, self.ui.groupBox_6)

        self.ui.tabWidget.setCurrentIndex(2)
        
    def loadDatasCsv(self, tableView, dataName):

        def toFloat(str_):
            try:
                return float(str_)
            except:
                return str_
        
        with open(dataName + '.csv', encoding='shift_jis') as f:
            dr = list( csv.DictReader(f) )
            dicts = []
            for row in dr:
                dicts.append( { key:toFloat(row[key]) for key in row } )

        # モデルに追加
        self.model[dataName].addColumns( [key for key in dicts[0]] )
        self.model[dataName].addItems( dicts )

        return dicts

    def tableViewInit(self, tableView, name, sortEnable=False, setModelDataEvent=None):
        # テーブルビュー設定
        self.model[name] = Model(self)
        self.proxyModel[name] = QtCore.QSortFilterProxyModel()
        self.proxyModel[name].setSourceModel(self.model[name])
        tableView.setModel(self.proxyModel[name])
        tableView.setItemDelegate(Delegate(None, setModelDataEvent))
        tableView.setAlternatingRowColors(True)
        if sortEnable:
            self.proxyModel[name].sort(-1, QtCore.Qt.AscendingOrder)
            self.proxyModel[name].setFilterKeyColumn(1)
            tableView.setSortingEnabled(True)

    def tableView_caliculate_xyz1_init(self):
        
        columns = self.inifile.get('calculationConditions','columns').splitlines()
        items = []
        for i in range(1000):
            try:
                vals = self.inifile.get( 'calculationConditions', 'items_{:0=3}'.format(i) ).splitlines()
                item = { key:val for key, val in zip(columns, vals) }
                items.append(item)
            except:
                break

        self.model['caliculate_xyz1'] = Model(self)
        self.model['caliculate_xyz1'].editableColumns = [1, 2, 3]
        self.model['caliculate_xyz1'].addColumns( columns )
        self.model['caliculate_xyz1'].addItems( items )
        self.proxyModel['caliculate_xyz1'] = QtCore.QSortFilterProxyModel()
        self.proxyModel['caliculate_xyz1'].setSourceModel(self.model['caliculate_xyz1'])
        self.ui.tableView_caliculate_xyz1.setModel(self.proxyModel['caliculate_xyz1'])
        self.ui.tableView_caliculate_xyz1.setItemDelegate(Delegate())
        self.ui.tableView_caliculate_xyz1.setAlternatingRowColors(True)
        self.ui.tableView_caliculate_xyz1.setColumnWidth(0, 150)
        self.ui.tableView_caliculate_xyz1.setColumnWidth(1, 70)
        self.ui.tableView_caliculate_xyz1.setColumnWidth(2, 70)
        self.ui.tableView_caliculate_xyz1.setColumnWidth(3, 70)
        
    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            # Ctrlキーが押されたら
            
            # アクティブなtableViewを取得
            for tv in self.findChildren(QtWidgets.QTableView):
                if tv.hasFocus():
                    tableView = tv
                    break
            else:
                return
            
            # 選択中のセルが無ければ何もしない
            selectedIndexes = tableView.selectedIndexes()
            if len(selectedIndexes) < 1:
                return
            
            if e.key() == QtCore.Qt.Key_C:
                self.CtrlC(selectedIndexes)

            if e.key() == QtCore.Qt.Key_V:
                self.CtrlV(selectedIndexes)
                
            if e.key() == QtCore.Qt.Key_U:
                sourceModel = selectedIndexes[0].model().sourceModel()
                txt = ''
                for column in sourceModel.columns:
                    txt = txt + column + '\t'
                txt = txt + '\n'
                for item in sourceModel.items:
                    for column in sourceModel.columns:
                        txt = txt + str(item[column]) + '\t'
                    txt = txt[:-1] + '\n'
                QtWidgets.QApplication.clipboard().setText(txt)
                
    def CtrlC(self, selectedIndexes):
        proxyModelData = selectedIndexes[0].model().data
        row = selectedIndexes[0].row()
        txt = ''

        for index in selectedIndexes:
            if not row == index.row():
                row = index.row()
                txt = txt[:-1] + '\n'
            txt = txt + str(proxyModelData(index)) + '\t'
        txt = txt[:-1]
        QtWidgets.QApplication.clipboard().setText(txt)

    def CtrlV(self, selectedIndexes):
        index = selectedIndexes[0]
        model = index.model().sourceModel()
        clipboardText = QtWidgets.QApplication.clipboard().text()
        for r, line in enumerate(clipboardText.splitlines()):
            if r + index.row() >= len(model.items):
                model.addItems([{}])
            for c, cellData in enumerate(line.split('\t')):
                if c + index.column() >= len(model.columns):
                    break
                inputIndex = model.createIndex(r + index.row(), c + index.column())
                model.setData(inputIndex, cellData.strip())
                model.dataChanged.emit(inputIndex, inputIndex)

def main():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MainWindow(app)
    window.show()
    #sys.exit(app.exec_())
    app.exec_()
    
if __name__ == '__main__':
    main()