from api import API
from converter import converter
from db.work_with_db import WorkWithCurrency, WorkWithHistory
import subprocess


class CursAbr:
    default_abr = [('BYN', 'Белорусский рубль'),
                   ('EUR', 'Евро'),
                   ('USD', 'Доллар США'),
                   ]

    def __init__(self):
        self.current_abr = self.default_abr

    def update(self, data: list):
        self.current_abr = data

    def get_current_abr(self):
        return self.current_abr

    def set_default_abr(self):
        self.current_abr = self.default_abr


def load_all_abr_for_gui():
    api = API()
    all_access_currency = api.get_all_abr_currency()
    return all_access_currency


def convert_value_if_online(cur_in, cur_out, volume):
    convertible_currency = API().get_info(cur_in)
    wanted_currency = API().get_info(cur_out)
    wwc = WorkWithCurrency()
    wwc.create_or_update(convertible_currency)
    wwc.create_or_update(wanted_currency)
    if convertible_currency.get('error_404') or \
            wanted_currency.get('error_404'):
        return "Connection error...", "date not defined"
    elif convertible_currency.get('error_type') or\
            wanted_currency.get('error_type'):
        return "Check input data...", "date not defined"
    else:
        wwh = WorkWithHistory()
        result = converter(convertible_currency,
                           wanted_currency,
                           float(volume))
        wwh.create(convertible_currency, wanted_currency, float(volume),
                   result)
        return str(round(result, 2)), \
            (str(convertible_currency.get('Date')[:10]) + ' ' +
             str(convertible_currency.get('Date')[11:]))


def convert_value_if_offline(cur_in, cur_out, volume):
    wwc = WorkWithCurrency()
    convertible_currency = wwc.read(cur_in)
    wanted_currency = wwc.read(cur_out)
    if convertible_currency['Cur_Abbreviation'] is not None and \
            wanted_currency['Cur_Abbreviation'] is not None:
        result = converter(convertible_currency, wanted_currency, volume)
        date_conv = min(convertible_currency['Date'],
                        wanted_currency['Date'])
        return result, str(date_conv)
    else:
        return "Currency not found in db...", "None"


def delete_history():
    wwh = WorkWithHistory()
    wwh.delete()


def generate_report():
    wwh = WorkWithHistory()
    result = wwh.read()
    with open('report.txt', 'w') as file:
        if result:
            first_line = f'{"№ п/п":^5}|' \
               f'{"дата и время":^26}|' \
               f'{"id конвертируемой валюты":^24}|' \
               f'{"абревиатура конвертируемой валюты":^33}|' \
               f'{"множ. конв. валюты":^18}|' \
               f'{"имя конв. валюты":^20}|' \
               f'{"множ. конв.":^11}|' \
               f'{"id конвертируемой валюты":^24}|' \
               f'{"абревиатура конвертируемой валюты":^33}|' \
               f'{"множ. конв. валюты":^18}|' \
               f'{"имя конв. валюты":^20}|' \
               f'{"множ. конв.":^11}|' \
               f'{"актуальная дата курса":^21}|' \
               f'{"кол-во конв валюты":^18}|' \
               f'{"результат":^9};\n'
            file.write(first_line)
            for row in result:
                file.write(str(row))
        else:
            file.write('База данных пуста')


def open_file(file_path):
    try:
        subprocess.run(['open', file_path])
    except FileNotFoundError:
        print('Error: No default text editor found')

current_curs = CursAbr()
