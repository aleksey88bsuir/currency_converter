# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.b_convert = QtWidgets.QPushButton(self.centralwidget)
        self.b_convert.setGeometry(QtCore.QRect(70, 230, 141, 25))
        self.b_convert.setObjectName("b_convert")
        self.qconvert_line = QtWidgets.QLineEdit(self.centralwidget)
        self.qconvert_line.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.qconvert_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qconvert_line.setObjectName("qconvert_line")
        self.qcurrency_in = QtWidgets.QComboBox(self.centralwidget)
        self.qcurrency_in.setGeometry(QtCore.QRect(5, 90, 290, 25))
        self.qcurrency_in.setEditable(False)
        self.qcurrency_in.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.qcurrency_in.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.qcurrency_in.setPlaceholderText("")
        self.qcurrency_in.setObjectName("qcurrency_in")
        self.qcurrency_out = QtWidgets.QComboBox(self.centralwidget)
        self.qcurrency_out.setGeometry(QtCore.QRect(5, 150, 290, 25))
        self.qcurrency_out.setObjectName("qcurrency_out")
        self.qlabel_currency_out = QtWidgets.QLabel(self.centralwidget)
        self.qlabel_currency_out.setGeometry(QtCore.QRect(20, 124, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qlabel_currency_out.setFont(font)
        self.qlabel_currency_out.setObjectName("qlabel_currency_out")
        self.qlabel_currency_in = QtWidgets.QLabel(self.centralwidget)
        self.qlabel_currency_in.setGeometry(QtCore.QRect(30, 60, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qlabel_currency_in.setFont(font)
        self.qlabel_currency_in.setObjectName("qlabel_currency_in")
        self.qtext_result = QtWidgets.QLabel(self.centralwidget)
        self.qtext_result.setGeometry(QtCore.QRect(20, 200, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qtext_result.setFont(font)
        self.qtext_result.setObjectName("qtext_result")
        self.qresult = QtWidgets.QLabel(self.centralwidget)
        self.qresult.setGeometry(QtCore.QRect(170, 200, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qresult.setFont(font)
        self.qresult.setText("")
        self.qresult.setObjectName("qresult")
        self.qtext_data_result = QtWidgets.QLabel(self.centralwidget)
        self.qtext_data_result.setGeometry(QtCore.QRect(20, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qtext_data_result.setFont(font)
        self.qtext_data_result.setObjectName("qtext_data_result")
        self.qresult_date = QtWidgets.QLabel(self.centralwidget)
        self.qresult_date.setGeometry(QtCore.QRect(110, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qresult_date.setFont(font)
        self.qresult_date.setText("")
        self.qresult_date.setObjectName("qresult_date")
        self.l_online_offline = QtWidgets.QLabel(self.centralwidget)
        self.l_online_offline.setGeometry(QtCore.QRect(230, 0, 67, 17))
        self.l_online_offline.setText("")
        self.l_online_offline.setObjectName("l_online_offline")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.m_history = QtWidgets.QMenu(self.menu)
        self.m_history.setObjectName("m_history")
        self.menu_currency_exchange = QtWidgets.QMenu(self.menu)
        self.menu_currency_exchange.setObjectName("menu_currency_exchange")
        self.m_about_us = QtWidgets.QMenu(self.menubar)
        self.m_about_us.setObjectName("m_about_us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.m_open_history = QtWidgets.QAction(MainWindow)
        self.m_open_history.setObjectName("m_open_history")
        self.m_del_history = QtWidgets.QAction(MainWindow)
        self.m_del_history.setObjectName("m_del_history")
        self.m_add_currency = QtWidgets.QAction(MainWindow)
        self.m_add_currency.setCheckable(False)
        self.m_add_currency.setObjectName("m_add_currency")
        self.m_del_currency = QtWidgets.QAction(MainWindow)
        self.m_del_currency.setObjectName("m_del_currency")
        self.m_default_settings = QtWidgets.QAction(MainWindow)
        self.m_default_settings.setObjectName("m_default_settings")
        self.m_online = QtWidgets.QAction(MainWindow)
        self.m_online.setObjectName("m_online")
        self.m_offline = QtWidgets.QAction(MainWindow)
        self.m_offline.setObjectName("m_offline")
        self.m_manual = QtWidgets.QAction(MainWindow)
        self.m_manual.setObjectName("m_manual")
        self.m_donate = QtWidgets.QAction(MainWindow)
        self.m_donate.setObjectName("m_donate")
        self.m_history.addAction(self.m_open_history)
        self.m_history.addAction(self.m_del_history)
        self.menu_currency_exchange.addAction(self.m_add_currency)
        self.menu_currency_exchange.addSeparator()
        self.menu_currency_exchange.addAction(self.m_default_settings)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_currency_exchange.menuAction())
        self.menu.addAction(self.m_history.menuAction())
        self.m_about_us.addAction(self.m_manual)
        self.m_about_us.addAction(self.m_donate)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.m_about_us.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конвертор валют"))
        self.b_convert.setText(_translate("MainWindow", "Конвертировать"))
        self.qconvert_line.setPlaceholderText(_translate("MainWindow", "Введите сумму для конвертации"))
        self.qlabel_currency_out.setText(_translate("MainWindow", "Выберите в какую валюту конвертируем"))
        self.qlabel_currency_in.setText(_translate("MainWindow", "Выберите конвертируемую валюту"))
        self.qtext_result.setText(_translate("MainWindow", "Результат конвертации:"))
        self.qtext_data_result.setText(_translate("MainWindow", "Курс на дату:"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.m_history.setTitle(_translate("MainWindow", "История конвертаций"))
        self.menu_currency_exchange.setTitle(_translate("MainWindow", "Конвертация валюты"))
        self.m_about_us.setTitle(_translate("MainWindow", "О приложении"))
        self.m_open_history.setText(_translate("MainWindow", "Открыть историю"))
        self.m_del_history.setText(_translate("MainWindow", "Очистить историю"))
        self.m_add_currency.setText(_translate("MainWindow", "Добавить/удалить валюту для конвертации"))
        self.m_del_currency.setText(_translate("MainWindow", "Удалить валюту для конвертации"))
        self.m_default_settings.setText(_translate("MainWindow", "Настройки по умолчанию"))
        self.m_online.setText(_translate("MainWindow", "Через глобальную паутину"))
        self.m_offline.setText(_translate("MainWindow", "Автономно"))
        self.m_manual.setText(_translate("MainWindow", "Рук-во по эксплуатации"))
        self.m_donate.setText(_translate("MainWindow", "Поддержать проект"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
