from PyQt5.QtWidgets import QListWidgetItem

from ui_w_add_currency import Ui_Dialog
from PyQt5 import QtWidgets
from funcs_for_GUI import load_all_abr_for_gui, current_curs
from search_abr import CursAbrIter
from db.work_with_db import WorkWithCurrency


class AddCurrencyWindow(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = None

    def init(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.setWindowTitle("Список валют для конвертации")
        self.ui.l_search_line.textChanged.connect(self.parse)
        self.ui.b_left_currency.clicked.connect(self.move_right)
        self.ui.b_right_currency.clicked.connect(self.move_left)
        self.ui.b_save_and_exit.clicked.connect(self.save_and_exit)
        self.ui.b_exit_without_save.clicked.connect(self.exit_without_save)
        self.show_left_list_on_dialog_window()
        self.show_right_list_on_dialog_window()

    def closeEvent(self, event):
        self.main_window.update_data()
        event.accept()

    def move_left(self):
        selected_items = self.ui.l_right_currency.selectedItems()
        if len(selected_items) > 0:
            for item in selected_items:
                if item.text() not in self.get_qlist_widget_data():
                    item_ = QListWidgetItem(item)
                    self.ui.l_left_currency.addItem(item_)

    def move_right(self):
        selected_items = self.ui.l_left_currency.selectedItems()
        if selected_items:
            for item in selected_items:
                row = self.ui.l_left_currency.row(item)
                self.ui.l_left_currency.takeItem(row)

    def show_left_list_on_dialog_window(self):
        for abr in current_curs.get_current_abr():
            if isinstance(abr, tuple):
                item = QListWidgetItem(f'{abr[0]} - {abr[1]}')
            else:
                item = QListWidgetItem(abr)
            self.ui.l_left_currency.addItem(item)

    def show_right_list_on_dialog_window(self):
        if self.main_window.online:
            list_abr = load_all_abr_for_gui()
        else:
            wwc = WorkWithCurrency()
            list_abr = wwc.read_all_available_currency()
        self.cur_iter = CursAbrIter(['BYN - Белорусский рубль'])
        for abr in list_abr:
            if abr[0] is not None:
                print(abr)
                str_abr = f'{abr[0]} - {abr[1]}'
                self.cur_iter.add_new_abr(str_abr)
                item = QListWidgetItem(str_abr)
                self.ui.l_right_currency.addItem(item)

    def parse(self, char):
        self.ui.l_right_currency.clear()
        data = []
        for item in self.cur_iter:
            if char.lower() in item.lower():
                data.append(item)
        for string_item in data:
            item_ = QListWidgetItem(string_item)
            self.ui.l_right_currency.addItem(item_)

    def get_qlist_widget_data(self):
        data = []
        for i in range(self.ui.l_left_currency.count()):
            item = self.ui.l_left_currency.item(i)
            key = item.text()
            data.append(key)
        return data

    def save_and_exit(self):
        new_data = self.get_qlist_widget_data()
        current_curs.update(new_data)
        self.close()

    def exit_without_save(self):
        self.close()

