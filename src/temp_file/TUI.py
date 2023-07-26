import os
import sys
from api import API
from converter import converter
from db.work_with_db import WorkWithHistory
from data_for_tests import tuple_for_tests


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def func(args):
    wwh = WorkWithHistory()
    wwh.delete()
    api = API()
    for i, arg in enumerate(args):
        convertible_currency = arg[0]
        convertible_amount = arg[1]
        wanted_currency = arg[2]
        convertible_currency = api.get_info(convertible_currency)
        wanted_currency = api.get_info(wanted_currency)
        rezult = converter(convertible_currency, wanted_currency, convertible_amount)
        wwh.create(convertible_currency, wanted_currency, convertible_amount, rezult)
        print(f'Тест №{i+1} из {len(args)} завершен')


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
    print('Отчет сгенерирован')


if __name__ == "__main__":
    func(tuple_for_tests)
    print("All tests completed")
    generate_report()
