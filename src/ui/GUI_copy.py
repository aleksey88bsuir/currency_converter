from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QDoubleValidator

from dialog import AddCurrencyWindow
from internet_connection_for_PyQt import InternetAccess
from ui.interface import Ui_MainWindow
from funcs_for_GUI import current_curs, convert_value_if_online, \
    convert_value_if_offline, generate_report, delete_history, open_file


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.validator = QDoubleValidator()
        self.ui.retranslateUi(self)
        self.start_interface()
        self.set_data()
        self.connection = InternetAccess(self)
        self.connection.start()
        self.ui_w_add_currency = AddCurrencyWindow(self)

    def closeEvent(self, event):
        self.connection.flag = False

    def start_interface(self):
        self.ui.qconvert_line.setValidator(self.validator)
        self.ui.qconvert_line.setMaxLength(10)
        self.ui.b_convert.clicked.connect(self.start_converting)
        self.ui.m_add_currency.triggered.connect(self.add_currency)
        self.ui.m_default_settings.triggered.connect(self.default_currency)
        self.ui.m_open_history.triggered.connect(self.open_history)
        self.ui.m_del_history.triggered.connect(self.del_history)
        self.ui.m_manual.triggered.connect(self.open_manual)
        self.ui.m_donate.triggered.connect(self.open_donate)

    def set_data(self):
        self.ui.qconvert_line.setText('0')
        for abr in current_curs.get_current_abr():
            self.ui.qcurrency_in.addItem(f'{abr[0]} - {abr[1]}')
            self.ui.qcurrency_out.addItem(f'{abr[0]} - {abr[1]}')
        self.ui.qcurrency_in.setCurrentIndex(0)
        self.ui.qcurrency_out.setCurrentIndex(1)

    def update_data(self):
        index1 = self.ui.qcurrency_in.currentIndex()
        index2 = self.ui.qcurrency_out.currentIndex()
        self.ui.qcurrency_in.clear()
        self.ui.qcurrency_out.clear()
        self.ui.qcurrency_in.setMaxVisibleItems(10)
        self.ui.qcurrency_out.setMaxVisibleItems(10)
        for abr in current_curs.get_current_abr():
            if not isinstance(abr, str):
                self.ui.qcurrency_in.addItem(f'{abr[0]} - {abr[1]}')
                self.ui.qcurrency_out.addItem(f'{abr[0]} - {abr[1]}')
            else:
                self.ui.qcurrency_in.addItem(abr)
                self.ui.qcurrency_out.addItem(abr)
        self.ui.qcurrency_in.setCurrentIndex(index1)
        self.ui.qcurrency_out.setCurrentIndex(index2)

    def start_converting(self):
        if self.check_the_possibility_of_conversion():
            amount = self.ui.qconvert_line.text().replace(',', '.')
            cur_in = self.ui.qcurrency_in.currentText()[:3]
            cur_out = self.ui.qcurrency_out.currentText()[:3]
            if self.online:
                result = convert_value_if_online(cur_in,
                                                 cur_out,
                                                 float(amount)
                                                 )
            else:
                result = convert_value_if_offline(cur_in,
                                                  cur_out,
                                                  float(amount)
                                                  )
            self.ui.qresult.setText(str(result[0]))
            self.ui.qresult_date.setText(result[1])

    def check_the_possibility_of_conversion(self):
        if self.ui.qconvert_line.text() and\
                self.ui.qcurrency_in.count() > 0 and\
                self.ui.qcurrency_out.count() > 0:
            return True

    def add_currency(self):
        self.ui_w_add_currency.init()
        self.ui_w_add_currency.show()

    def default_currency(self):
        self.ui.qconvert_line.setText('0')
        current_curs.set_default_abr()
        self.update_data()

    @staticmethod
    def open_history():
        generate_report()
        open_file('report.txt')

    @staticmethod
    def del_history():
        delete_history()

    def open_manual(self):
        QMessageBox.information(self, "Описание работы программы",
                                'Разработано компанией Р-443У_comp')

    def open_donate(self):
        QMessageBox.information(self, "Вы можете поддержать проект",
                                'Для донатов 6711 2900 4619 0066')

    def show_internet_connection_status(self):
        if self.online:
            self.ui.l_online_offline.setText('online')
            self.ui.l_online_offline.setStyleSheet("color: green;")
        else:
            self.ui.l_online_offline.setText('offline')
            self.ui.l_online_offline.setStyleSheet("color: red;")


def show_message_about_error(error, description_error):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(error)
    msg.setText(description_error)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    app.exec()
