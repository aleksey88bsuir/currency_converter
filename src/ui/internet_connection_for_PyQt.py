from time import sleep
from threading import Thread
from check_connection import check_internet_access


class InternetAccess(Thread):
    """Предпологалось задействовать для автообновления курса"""
    def __init__(self, check_obj):
        super().__init__()
        self.flag = True
        self.check_obj = check_obj
        self.check_connection()

    def run(self):
        while self.flag:
            self.check_connection()
            sleep(5)

    def check_connection(self):
        self.check_obj.online = check_internet_access()
        self.check_obj.show_internet_connection_status()
