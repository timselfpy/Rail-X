# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from bs4 import BeautifulSoup
import pyqtgraph as pg
from PIL import Image
import subprocess
import threading
import requests
import datetime
import numpy
import sys


pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
pg.setConfigOption('imageAxisOrder', 'row-major')


class Ui_Form(object):
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        if sys.platform.startswith('linux'):
            self.system = 'Linux'
        elif sys.platform.startswith('darwin'):
            self.system = 'macOS'
        elif sys.platform.startswith('win32'):
            self.system = 'Windows'

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1074, 676)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.FOR = QtWidgets.QVBoxLayout()
        self.FOR.setContentsMargins(-1, -1, -1, 0)
        self.FOR.setObjectName("FOR")
        self.FOR_INPUT = QtWidgets.QLineEdit(self.widget)
        self.FOR_INPUT.setObjectName("FOR_INPUT")
        self.FOR.addWidget(self.FOR_INPUT)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.FOR.addWidget(self.comboBox)
        self.FOR_BUTTON = QtWidgets.QPushButton(self.widget)
        self.FOR_BUTTON.setObjectName("FOR_BUTTON")
        self.FOR.addWidget(self.FOR_BUTTON)
        self.FOR_TABLE = QtWidgets.QTableWidget(self.widget)
        self.FOR_TABLE.setObjectName("FOR_TABLE")
        self.FOR_TABLE.setColumnCount(6)
        self.FOR_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE.setHorizontalHeaderItem(5, item)
        self.FOR.addWidget(self.FOR_TABLE)
        self.verticalLayout_5.addLayout(self.FOR)
        self.tabWidget.addTab(self.widget, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FOR_2 = QtWidgets.QVBoxLayout()
        self.FOR_2.setContentsMargins(-1, -1, -1, 0)
        self.FOR_2.setObjectName("FOR_2")
        self.FOR_INPUT_2 = QtWidgets.QLineEdit(self.tab)
        self.FOR_INPUT_2.setObjectName("FOR_INPUT_2")
        self.FOR_2.addWidget(self.FOR_INPUT_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.FOR_2.addWidget(self.comboBox_2)
        self.FOR_BUTTON_2 = QtWidgets.QPushButton(self.tab)
        self.FOR_BUTTON_2.setObjectName("FOR_BUTTON_2")
        self.FOR_2.addWidget(self.FOR_BUTTON_2)
        self.FOR_TABLE_2 = QtWidgets.QTableWidget(self.tab)
        self.FOR_TABLE_2.setObjectName("FOR_TABLE_2")
        self.FOR_TABLE_2.setColumnCount(4)
        self.FOR_TABLE_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_2.setHorizontalHeaderItem(3, item)
        self.FOR_2.addWidget(self.FOR_TABLE_2)
        self.horizontalLayout.addLayout(self.FOR_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FOR_3 = QtWidgets.QVBoxLayout()
        self.FOR_3.setContentsMargins(-1, -1, -1, 0)
        self.FOR_3.setObjectName("FOR_3")
        self.FOR_INPUT_3 = QtWidgets.QLineEdit(self.tab_2)
        self.FOR_INPUT_3.setObjectName("FOR_INPUT_3")
        self.FOR_3.addWidget(self.FOR_INPUT_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.FOR_3.addWidget(self.comboBox_3)
        self.FOR_BUTTON_3 = QtWidgets.QPushButton(self.tab_2)
        self.FOR_BUTTON_3.setObjectName("FOR_BUTTON_3")
        self.FOR_3.addWidget(self.FOR_BUTTON_3)
        self.FOR_TABLE_3 = QtWidgets.QTableWidget(self.tab_2)
        self.FOR_TABLE_3.setObjectName("FOR_TABLE_3")
        self.FOR_TABLE_3.setColumnCount(6)
        self.FOR_TABLE_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.FOR_TABLE_3.setHorizontalHeaderItem(5, item)
        self.FOR_3.addWidget(self.FOR_TABLE_3)
        self.horizontalLayout_2.addLayout(self.FOR_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.RAILRE = QtWidgets.QWidget()
        self.RAILRE.setObjectName("RAILRE")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.RAILRE)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RAILRE_ = QtWidgets.QVBoxLayout()
        self.RAILRE_.setObjectName("RAILRE_")
        self.RAILRE_INPUT = QtWidgets.QLineEdit(self.RAILRE)
        self.RAILRE_INPUT.setObjectName("RAILRE_INPUT")
        self.RAILRE_.addWidget(self.RAILRE_INPUT)
        self.RAILRE_BUTTON = QtWidgets.QPushButton(self.RAILRE)
        self.RAILRE_BUTTON.setObjectName("RAILRE_BUTTON")
        self.RAILRE_.addWidget(self.RAILRE_BUTTON)
        self.RAILRE_TABLE = QtWidgets.QTableWidget(self.RAILRE)
        self.RAILRE_TABLE.setObjectName("RAILRE_TABLE")
        self.RAILRE_TABLE.setColumnCount(3)
        self.RAILRE_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.RAILRE_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RAILRE_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RAILRE_TABLE.setHorizontalHeaderItem(2, item)
        self.RAILRE_.addWidget(self.RAILRE_TABLE)
        self.horizontalLayout_3.addLayout(self.RAILRE_)
        self.tabWidget.addTab(self.RAILRE, "")
        self.TIME = QtWidgets.QWidget()
        self.TIME.setObjectName("TIME")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.TIME)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.TIME_ = QtWidgets.QVBoxLayout()
        self.TIME_.setObjectName("TIME_")
        self.TIME_INPUT = QtWidgets.QLineEdit(self.TIME)
        self.TIME_INPUT.setObjectName("TIME_INPUT")
        self.TIME_.addWidget(self.TIME_INPUT)
        self.TIME_BUTTON = QtWidgets.QPushButton(self.TIME)
        self.TIME_BUTTON.setObjectName("TIME_BUTTON")
        self.TIME_.addWidget(self.TIME_BUTTON)
        self.TIME_TABLE = QtWidgets.QTableWidget(self.TIME)
        self.TIME_TABLE.setObjectName("TIME_TABLE")
        self.TIME_TABLE.setColumnCount(3)
        self.TIME_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TIME_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TIME_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TIME_TABLE.setHorizontalHeaderItem(2, item)
        self.TIME_.addWidget(self.TIME_TABLE)
        self.verticalLayout_7.addLayout(self.TIME_)
        self.tabWidget.addTab(self.TIME, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.xiaguan_line = QtWidgets.QLineEdit(self.tab_4)
        self.xiaguan_line.setObjectName("xiaguan_line")
        self.verticalLayout_4.addWidget(self.xiaguan_line)
        self.xiaguan_search = QtWidgets.QPushButton(self.tab_4)
        self.xiaguan_search.setObjectName("xiaguan_search")
        self.verticalLayout_4.addWidget(self.xiaguan_search)
        self.graphicsView = pg.ImageView(self.tab_4)
        self.graphicsView.ui.histogram.hide()
        self.graphicsView.ui.menuBtn.hide()
        self.graphicsView.ui.roiBtn.hide()


        self.verticalLayout_4.addWidget(self.graphicsView)
        self.progressBar = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(100)
        self.verticalLayout_4.addWidget(self.progressBar)
        self.xiaguan_last = QtWidgets.QPushButton(self.tab_4)
        self.xiaguan_last.setObjectName("xiaguan_last")
        self.verticalLayout_4.addWidget(self.xiaguan_last)
        self.xiaguan_next = QtWidgets.QPushButton(self.tab_4)
        self.xiaguan_next.setObjectName("xiaguan_next")
        self.verticalLayout_4.addWidget(self.xiaguan_next)
        self.xiaguan_openfolder = QtWidgets.QPushButton(self.tab_4)
        self.xiaguan_openfolder.setObjectName("xiaguan_openfolder")
        self.verticalLayout_4.addWidget(self.xiaguan_openfolder)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.ABOUT = QtWidgets.QWidget()
        self.ABOUT.setObjectName("ABOUT")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ABOUT)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ABOUT_LABLE = QtWidgets.QLabel(self.ABOUT)
        self.ABOUT_LABLE.setObjectName("ABOUT_LABLE")
        self.horizontalLayout_4.addWidget(self.ABOUT_LABLE)
        self.tabWidget.addTab(self.ABOUT, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Rail-X"))
        self.comboBox.setItemText(0, _translate("Form", "车组号"))
        self.comboBox.setItemText(1, _translate("Form", "车型"))
        self.comboBox.setItemText(2, _translate("Form", "配属路局"))
        self.comboBox.setItemText(3, _translate("Form", "配属动车所"))
        self.comboBox.setItemText(4, _translate("Form", "生产厂家"))
        self.FOR_BUTTON.setText(_translate("Form", "查询"))
        item = self.FOR_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("Form", "车型"))
        item = self.FOR_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("Form", "车组号"))
        item = self.FOR_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("Form", "配属路局"))
        item = self.FOR_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("Form", "配属动车所"))
        item = self.FOR_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("Form", "生产厂家"))
        item = self.FOR_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("Form", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "动车组配属"))
        self.comboBox_2.setItemText(0, _translate("Form", "车型"))
        self.comboBox_2.setItemText(1, _translate("Form", "车型-车号"))
        self.comboBox_2.setItemText(2, _translate("Form", "配属机务段"))
        self.FOR_BUTTON_2.setText(_translate("Form", "查询"))
        item = self.FOR_TABLE_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "车型"))
        item = self.FOR_TABLE_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "车号"))
        item = self.FOR_TABLE_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "配属机务段"))
        item = self.FOR_TABLE_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "机车配属"))
        self.comboBox_3.setItemText(0, _translate("Form", "车号"))
        self.comboBox_3.setItemText(1, _translate("Form", "型号"))
        self.comboBox_3.setItemText(2, _translate("Form", "现配属"))
        self.comboBox_3.setItemText(3, _translate("Form", "运用车次(不保证时效性)"))
        self.comboBox_3.setItemText(4, _translate("Form", "制造厂"))
        self.comboBox_3.setItemText(5, _translate("Form", "转向架"))
        self.FOR_BUTTON_3.setText(_translate("Form", "查询"))
        item = self.FOR_TABLE_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "型号    "))
        item = self.FOR_TABLE_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "车号"))
        item = self.FOR_TABLE_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "现配属"))
        item = self.FOR_TABLE_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "运用车次(仅供回忆)"))
        item = self.FOR_TABLE_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "制造厂"))
        item = self.FOR_TABLE_3.horizontalHeaderItem(5)
        item.setText(_translate("Form", "转向架"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "车厢配属"))
        self.RAILRE_BUTTON.setText(_translate("Form", "查询"))
        item = self.RAILRE_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("Form", "时间"))
        item = self.RAILRE_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("Form", "车号"))
        item = self.RAILRE_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("Form", "车次"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RAILRE), _translate("Form", "列车车型"))
        self.TIME_BUTTON.setText(_translate("Form", "查询"))
        item = self.TIME_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("Form", "车站"))
        item = self.TIME_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("Form", "到达时间"))
        item = self.TIME_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("Form", "出发时间"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TIME), _translate("Form", "车次时刻表"))
        self.pushButton.setText(_translate("Form", "查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "车次"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "始发站"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "出发时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "终到站"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "终到时间"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "交路表"))
        self.xiaguan_search.setText(_translate("Form", "查询"))
        self.xiaguan_last.setText(_translate("Form", "上一张"))
        self.xiaguan_next.setText(_translate("Form", "下一张"))
        self.xiaguan_openfolder.setText(_translate("Form", "打开下载目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "下关站图片"))
        self.ABOUT_LABLE.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:96pt; font-weight:600; font-style:italic;\">Rail-X</span></p><p>Rail-X  作者：Bilibili东方疯地铁</p><p>e-mail:3136391710@qq.com</p><p><br/></p><p>API来源</p><p>车次交路:<a href=\"rail.re\"><span style=\" text-decoration: underline; color:#0000ff;\">rail.re</span></a></p><p>车辆配属:<a href=\"cr400bf.passearch.info\"><span style=\" text-decoration: underline; color:#0000ff;\">cr400bf.passearch.info</span></a></p><p><a href=\"cr400bf.passearch.info\"><span style=\" color:#000000;\">车次时刻表、车站途径列车、车站大屏:</span></a><a href=\"rail.moefactory.com\"><span style=\" text-decoration: underline; color:#0000ff;\">rail.moefactory.com</span></a></p><p><a href=\"rail.moefactory.com\"><span style=\" color:#000000;\">动车组配属:</span></a><a href=\"emu.passearch.info\"><span style=\" text-decoration: underline; color:#0000ff;\">emu.passearch.info</span></a></p><p><a href=\"rail.moefactory.com\"><span style=\" color:#000000;\">机车配属:</span></a><a href=\"loco.passearch.info\"><span style=\" text-decoration: underline; color:#0000ff;\">loco.passearch.info</span></a></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ABOUT), _translate("Form", "关于Rail-X"))


        self.RAILRE_BUTTON.clicked.connect(self.find)
        self.TIME_BUTTON.clicked.connect(self.time)
        self.FOR_BUTTON_2.clicked.connect(self.pass_search_ui)
        self.FOR_BUTTON.clicked.connect(self.emu_search_ui)
        self.FOR_BUTTON_3.clicked.connect(self.bf_ui)
        self.pushButton.clicked.connect(self.route_ui)
        self.xiaguan_search.clicked.connect(self.train_photo_ui)
        self.xiaguan_last.clicked.connect(self.last_page)
        self.xiaguan_next.clicked.connect(self.next_page)
        self.xiaguan_openfolder.clicked.connect(self.start_img_dir)



    def find(self):
        if self.RAILRE_INPUT.text()[0: 2].upper() == "CR":
            flag = "emu"
        else:
            flag = "train"
        response = requests.get(f"https://api.rail.re/{flag}/{self.RAILRE_INPUT.text()}", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"})

        ls = eval(response.text)

        self.RAILRE_TABLE.setRowCount(0)
        self.RAILRE_TABLE.clearContents()


        for i in ls:
            model = self.RAILRE_TABLE.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount() - 1, 0), i["date"])
            model.setData(model.index(model.rowCount() - 1, 1), i["emu_no"])
            model.setData(model.index(model.rowCount() - 1, 2), i["train_no"])



    def time(self):
        date_ls = datetime.date.today().__str__().split("-")
        response = requests.post("https://rail.moefactory.com/api/trainDetails/queryTrainDelayDetails", data={"trainNumber": self.TIME_INPUT.text(), "date": f"{date_ls[0]}{date_ls[1]}{date_ls[2]}"})
        ls = eval(response.text.replace("null", "None"))["data"]

        self.TIME_TABLE.setRowCount(0)
        self.TIME_TABLE.clearContents()
        for i in ls:
            model = self.TIME_TABLE.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount() - 1, 0), i["stationName"])
            model.setData(model.index(model.rowCount() - 1, 1), i["arrivalTime"])
            model.setData(model.index(model.rowCount() - 1, 2), i["departureTime"])


    def pass_search(self, keyword, type):
        result = []
        response = requests.get(f"https://loco.passearch.info/index.php?type={type}&keyword={keyword}&pagenum=1")
        response.encoding = "utf-8"
        bs = BeautifulSoup(response.text, "html.parser")

        try:
            a = bs.find_all("p")[1].find_all_next("p")[0].find_all_next("a")[2]["href"].split("pagenum=")[1]
        except:
            a = 1
        for i in range(1, int(a) + 1):
            response = requests.get(f"https://loco.passearch.info/index.php?type={type}&keyword={keyword}&pagenum={i}")
            response.encoding = "utf-8"
            bs = BeautifulSoup(response.text, "html.parser")
            table = bs.find("table", border="0", align="center")
            tr_ls = table.find_all("tr")
            tr_ls.pop(0)

            for i in tr_ls:
                ls = i.find_all_next("td")[0: 4]
                result.append([ls[0].find("a").getText(), ls[1].getText(), ls[2].find("a").getText(), ls[3].getText()])

        return result

    def pass_search_ui(self):
        if self.comboBox_2.currentText() == "车型":
            flag = "model"
        elif self.comboBox_2.currentText() == "车型-车号":
            flag = "fullname"
        else:
            flag = "depot"
        ls = self.pass_search(self.FOR_INPUT_2.text(), flag)


        self.FOR_TABLE_2.setRowCount(0)
        self.FOR_TABLE_2.clearContents()
        for i in ls:
            model = self.FOR_TABLE_2.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount() - 1, 0), i[0])
            model.setData(model.index(model.rowCount() - 1, 1), i[1])
            model.setData(model.index(model.rowCount() - 1, 2), i[2])
            model.setData(model.index(model.rowCount() - 1, 3), i[3])


    def emu_search(self, keyword, type):


        result = []
        response = requests.get(f"https://emu.passearch.info/index.php?type={type}&keyword={keyword}&pagenum=1")
        response.encoding = "utf-8"
        bs = BeautifulSoup(response.text, "html.parser")

        try:
            a = bs.find_all("p")[1].find_all_next("p")[0].find_all_next("a")[2]["href"].split("pagenum=")[1]
        except:
            a = 1

        for i in range(1, int(a) + 1):
            response = requests.get(f"https://emu.passearch.info/index.php?type={type}&keyword={keyword}&pagenum={i}")
            response.encoding = "utf-8"
            bs = BeautifulSoup(response.text, "html.parser")
            table = bs.find("table", border="0", align="center")
            tr_ls = table.find_all("tr")
            tr_ls.pop(0)

            for i in tr_ls:
                ls = i.find_all_next("td")[0: -1]
                result.append([ls[0].find("a").getText(), ls[1].getText(), ls[2].find("a").getText(), ls[3].find("a").getText(), ls[4].getText(), ls[5].getText()])

        return result

    def emu_search_ui(self):
        if self.comboBox.currentText() == "车组号":
            flag = "number"
        elif self.comboBox.currentText() == "车型":
            flag = "model"
        elif self.comboBox.currentText() == "配属路局":
            flag = "bureau"
        elif self.comboBox.currentText() == "配属动车所":
            flag = "department"
        else:
            flag = "plant"
        ls = self.emu_search(self.FOR_INPUT.text(), flag)


        self.FOR_TABLE.setRowCount(0)
        self.FOR_TABLE.clearContents()
        for i in ls:
            model = self.FOR_TABLE.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount() - 1, 0), i[0])
            model.setData(model.index(model.rowCount() - 1, 1), i[1])
            model.setData(model.index(model.rowCount() - 1, 2), i[2])
            model.setData(model.index(model.rowCount() - 1, 3), i[3])
            model.setData(model.index(model.rowCount() - 1, 4), i[4])
            model.setData(model.index(model.rowCount() - 1, 5), i[5])


    def bf_search(self, keyword, type):


        result = []
        response = requests.get(f"https://cr400bf.passearch.info/index.php?type={type}&keyword={keyword}&pagenum=1")
        response.encoding = "utf-8"
        bs = BeautifulSoup(response.text, "html.parser")

        try:
            a = bs.find_all("p")[1].find_all_next("p")[0].find_all_next("a")[2]["href"].split("pagenum=")[1]
        except:
            a = 1


        for i in range(1, int(a) + 1):
            response = requests.get(f"https://cr400bf.passearch.info/index.php?type={type}&keyword={keyword}&pagenum={i}")
            response.encoding = "utf-8"
            bs = BeautifulSoup(response.text, "html.parser")
            table = bs.find("table", border="0")
            tr_ls = table.find_all("tr")
            tr_ls.pop(0)

            for i in tr_ls:
                ls = i.find_all_next("td")[0: -1]
                result.append([ls[0].getText(), ls[1].getText(), ls[2].getText(), ls[3].getText(), ls[4].getText(), ls[5].getText(), ls[6].getText()])

        return result

    def bf_ui(self):
        if self.comboBox_3.currentText() == "车号":
            flag = "number"
        elif self.comboBox_3.currentText() == "型号":
            flag = "model"
        elif self.comboBox_3.currentText() == "现配属":
            flag = "depot"
        elif self.comboBox_3.currentText() == "运用车次(不保证时效性)":
            flag = "train"
        elif self.comboBox_3.currentText() == "转向架":
            flag = "bogie"
        else:
            flag = "plant"
        ls = self.bf_search(self.FOR_INPUT_3.text(), flag)


        self.FOR_TABLE_3.setRowCount(0)
        self.FOR_TABLE_3.clearContents()
        for i in ls:
            model = self.FOR_TABLE_3.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount() - 1, 0), i[0])
            model.setData(model.index(model.rowCount() - 1, 1), i[1])
            model.setData(model.index(model.rowCount() - 1, 2), i[2])
            model.setData(model.index(model.rowCount() - 1, 3), i[3])
            model.setData(model.index(model.rowCount() - 1, 4), i[4])
            model.setData(model.index(model.rowCount() - 1, 5), i[5])
            model.setData(model.index(model.rowCount() - 1, 6), i[6])


    def route(self, train):
        date = "".join(datetime.date.today().__str__().split("-"))
        data = {"date": date, "trainNumber": train, "pageIndex": "1", "pageSize": "15"}
        response = requests.post("https://rail.moefactory.com/api/trainNumber/query", data=data)
        response.encoding = "utf-8"
        train_index = response.json()["data"]["data"][0]['trainIndex']

        data = {"date": date, "trainIndex": train_index}
        response = requests.post("https://rail.moefactory.com/api/trainDetails/query", data=data)
        response.encoding = "utf-8"
        return response.json()["data"]["routing"]["routingItems"]


    def route_ui(self):
        ls = self.route(self.lineEdit.text())


        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        for i in ls:
            model = self.tableWidget.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount() - 1, 0), i["trainNumber"])
            model.setData(model.index(model.rowCount() - 1, 1), i["beginStationName"])
            model.setData(model.index(model.rowCount() - 1, 2), i["departureTime"])
            model.setData(model.index(model.rowCount() - 1, 3), i["endStationName"])
            model.setData(model.index(model.rowCount() - 1, 4), i["arrivalTime"])

    def train_photo(self, keyword):

        headers = {
            'Connection': 'close',
            "User-Agent": self.user_agent
        }
        response = requests.post(f"http://www.xiaguanzhan.com/soso.asp", data={"keyword": keyword.encode("gb2312"), "Submit": "%CB%D1%CB%F7"}, headers=headers)
        response.encoding = "gbk"

        bs = BeautifulSoup(response.text, "html.parser")
        table = bs.find("td", height="58")
        div = table.find("div", attrs={"class": "container"})
        items = div.find_all("div", attrs={"class": "Item"})
        photo_url_list = []
        for i in items:
            photo_url_list.append("http://www.xiaguanzhan.com" + i.find("img")["src"].replace("xt", "xz"))
        return photo_url_list

    def train_photo_ui(self):

        self.img_page = 0
        self.photo_list = self.train_photo(self.xiaguan_line.text())
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹")  # 起始路径


        with open(self.directory + "/Rail-X Image.jpg", "wb") as file:
            file.write(requests.get(self.photo_list[self.img_page]).content)

        self.graphicsView.setImage(numpy.array(Image.open(self.directory + "/Rail-X Image.jpg")))

        threading.Thread(target=self.download_image).start()



    def download_image(self):

        state_a = 100 / len(self.photo_list)
        index = 0

        for i in self.photo_list:
            with open(f"{self.directory}/{str(index)}.jpg", "wb") as file:
                file.write(requests.get(i).content)
            self.progressBar.setValue(int((index + 1) * state_a))
            index += 1



    def next_page(self):
        self.img_page += 1
        self.img_page = self.img_page % len(self.photo_list)
        with open(self.directory + "/Rail-X Image.jpg", "wb") as file:
            file.write(requests.get(self.photo_list[self.img_page]).content)

        self.graphicsView.setImage(numpy.array(Image.open(self.directory + "/Rail-X Image.jpg")))

    def last_page(self):
        self.img_page -= 1
        self.img_page = self.img_page % len(self.photo_list)
        with open(self.directory + "/Rail-X Image.jpg", "wb") as file:
            file.write(requests.get(self.photo_list[self.img_page]).content)

        self.graphicsView.setImage(numpy.array(Image.open(self.directory + "/Rail-X Image.jpg")))

    def start_img_dir(self):
        if self.system == "Windows":
            subprocess.Popen(f'explorer {self.directory}')
        elif self.system == "macOS":
            subprocess.Popen(['open', self.directory])
        else:
            subprocess.Popen(['xdg-open', self.directory])




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
