# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 392)
        Dialog.setMinimumSize(QtCore.QSize(431, 392))
        Dialog.setMaximumSize(QtCore.QSize(431, 392))
        self.l_left_currency = QtWidgets.QListWidget(Dialog)
        self.l_left_currency.setGeometry(QtCore.QRect(5, 61, 205, 251))
        self.l_left_currency.setObjectName("l_left_currency")
        self.l_right_currency = QtWidgets.QListWidget(Dialog)
        self.l_right_currency.setGeometry(QtCore.QRect(220, 60, 205, 251))
        self.l_right_currency.setObjectName("l_right_currency")
        self.b_left_currency = QtWidgets.QPushButton(Dialog)
        self.b_left_currency.setGeometry(QtCore.QRect(5, 320, 91, 25))
        self.b_left_currency.setObjectName("b_left_currency")
        self.b_right_currency = QtWidgets.QPushButton(Dialog)
        self.b_right_currency.setGeometry(QtCore.QRect(334, 320, 91, 25))
        self.b_right_currency.setObjectName("b_right_currency")
        self.l_search_line = QtWidgets.QLineEdit(Dialog)
        self.l_search_line.setGeometry(QtCore.QRect(10, 20, 411, 25))
        self.l_search_line.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.l_search_line.setClearButtonEnabled(False)
        self.l_search_line.setObjectName("l_search_line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 121, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 44, 151, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 44, 161, 17))
        self.label_3.setObjectName("label_3")
        self.b_save_and_exit = QtWidgets.QPushButton(Dialog)
        self.b_save_and_exit.setGeometry(QtCore.QRect(120, 320, 191, 25))
        self.b_save_and_exit.setObjectName("b_save_and_exit")
        self.b_exit_without_save = QtWidgets.QPushButton(Dialog)
        self.b_exit_without_save.setGeometry(QtCore.QRect(120, 360, 191, 25))
        self.b_exit_without_save.setObjectName("b_exit_without_save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.b_left_currency.setText(_translate("Dialog", "-->"))
        self.b_left_currency.setShortcut(_translate("Dialog", "Right"))
        self.b_right_currency.setText(_translate("Dialog", "<--"))
        self.b_right_currency.setShortcut(_translate("Dialog", "Left"))
        self.label.setText(_translate("Dialog", "Строка поиска"))
        self.label_2.setText(_translate("Dialog", "Имеющаяся валюта"))
        self.label_3.setText(_translate("Dialog", "Добавляемая валюта"))
        self.b_save_and_exit.setText(_translate("Dialog", "Сохранить и выйти"))
        self.b_save_and_exit.setShortcut(_translate("Dialog", "Return"))
        self.b_exit_without_save.setText(_translate("Dialog", "Выйти без сохранения"))
        self.b_exit_without_save.setShortcut(_translate("Dialog", "Backspace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())