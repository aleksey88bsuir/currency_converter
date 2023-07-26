import sys
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, \
    QAction
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import QThread, Qt, QCoreApplication
from funcs_for_GUI import current_curs, convert_value_if_online, \
    convert_value_if_offline, generate_report, delete_history
import subprocess
from check_connection import check_internet_access
from dialog import ChildWindow


class App(QWidget):
    """Создает и описывает главное окно программы."""
    def __init__(self, application):
        super().__init__()
        self.app = application
        self.cur_in = None
        self.cur_out = None
        self.volume = None
        self.cur_iter = None
        self.w_dialog = None
        self.online = None
        self.connection = None
        self.validator = QDoubleValidator()
        self.validator.setDecimals(2)
        self.start_interface()
        self.set_data()
        self.w_dialog = ChildWindow(self)

    def start_interface(self):
        self.w_main = uic.loadUi('ui/interface.ui')
        self.w_main.show()
        self.w_main.qconvert_line.setValidator(self.validator)
        self.w_main.qconvert_line.setMaxLength(10)
        self.w_main.b_convert.clicked.connect(self.start_converting)
        self.w_main.m_add_currency.triggered.connect(self.add_currency)
        self.w_main.m_default_settings.triggered.connect(self.default_currency)
        self.w_main.m_open_history.triggered.connect(self.open_history)
        self.w_main.m_del_history.triggered.connect(self.del_history)
        self.w_main.m_manual.triggered.connect(self.open_manual)
        self.w_main.m_donate.triggered.connect(self.open_donate)


    def set_data(self):
        self.w_main.qconvert_line.setText('0')
        for abr in current_curs.get_current_abr():
            self.w_main.qcurrency_in.addItem(f'{abr[0]} - {abr[1]}')
            self.w_main.qcurrency_out.addItem(f'{abr[0]} - {abr[1]}')
        self.w_main.qcurrency_in.setCurrentIndex(0)
        self.w_main.qcurrency_out.setCurrentIndex(1)

    def update_data(self):
        index1 = self.w_main.qcurrency_in.currentIndex()
        index2 = self.w_main.qcurrency_out.currentIndex()
        self.w_main.qcurrency_in.clear()
        self.w_main.qcurrency_out.clear()
        self.w_main.qcurrency_in.setMaxVisibleItems(10)
        self.w_main.qcurrency_out.setMaxVisibleItems(10)
        for abr in current_curs.get_current_abr():
            if not isinstance(abr, str):
                self.w_main.qcurrency_in.addItem(f'{abr[0]} - {abr[1]}')
                self.w_main.qcurrency_out.addItem(f'{abr[0]} - {abr[1]}')
            else:
                self.w_main.qcurrency_in.addItem(abr)
                self.w_main.qcurrency_out.addItem(abr)
        self.w_main.qcurrency_in.setCurrentIndex(index1)
        self.w_main.qcurrency_out.setCurrentIndex(index2)

    def start_converting(self):
        if self.check_the_possibility_of_conversion():
            self.volume = self.w_main.qconvert_line.text().replace(',', '.')
            self.cur_in = self.w_main.qcurrency_in.currentText()[:3]
            self.cur_out = self.w_main.qcurrency_out.currentText()[:3]
            if self.online:
                result = convert_value_if_online(self.cur_in,
                                                 self.cur_out,
                                                 float(self.volume)
                                                 )
            else:
                result = convert_value_if_offline(self.cur_in,
                                                  self.cur_out,
                                                  float(self.volume)
                                                  )
            self.w_main.qresult.setText(str(result[0]))
            self.w_main.qresult_date.setText(result[1])

    def check_the_possibility_of_conversion(self):
        if self.w_main.qconvert_line.text() and\
                self.w_main.qcurrency_in.count() > 0 and\
                self.w_main.qcurrency_out.count() > 0:
            return True

    def add_currency(self):
        if self.online:
            self.w_dialog.init()
            self.w_dialog.exec_()
        else:
            show_message_about_error('отсутствует интренет соединение',
                                     'данная функция пока недоступна в офлайн режиме')

    def default_currency(self):
        self.w_main.qconvert_line.setText('0')
        current_curs.set_default_abr()
        self.update_data()

    def open_history(self):
        generate_report()
        self.open_file_with_default_text_editor('report.txt')

    @staticmethod
    def del_history():
        delete_history()

    @staticmethod
    def open_file_with_default_text_editor(file_path):
        try:
            subprocess.run(['open', file_path])
        except FileNotFoundError:
            print('Error: No default text editor found')

    def open_manual(self):
        QMessageBox.information(self, "Описание работы программы", 'aaa')

    def open_donate(self):
        QMessageBox.information(self, "Вы можете поддержать проект", 'bbb')

    def show_internet_connection_status(self):
        if self.online:
            self.w_main.l_online_offline.setText('online')
            self.w_main.l_online_offline.setStyleSheet("color: green;")
        else:
            self.w_main.l_online_offline.setText('offline')
            self.w_main.l_online_offline.setStyleSheet("color: red;")

    def closeEvent(self, event):
        print('Ohh...')
        reply = QMessageBox.question(
            self, 'Вопрос', 'Точно хотите закрыть?',
            QMessageBox.Yes, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class InternetAccess(QThread):
    """Предпологалось задействовать для автообновления курса"""
    def __init__(self):
        QThread.__init__(self)
        self.check_connection()

    def run(self):
        while True:
            self.check_connection()
            sleep(5)

    @staticmethod
    def check_connection():
        ex.online = check_internet_access()
        ex.show_internet_connection_status()


def show_message_about_error(error, description_error):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(error)
    msg.setText(description_error)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


app = QtWidgets.QApplication(sys.argv)
ex = App(app)
ex.connection = InternetAccess()
ex.connection.start()
sys.exit(app.exec_())
