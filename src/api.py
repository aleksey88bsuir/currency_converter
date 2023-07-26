import requests
import enum
import datetime


class RequestMode(enum.Enum):
    """
    Перечисление режимов работы функции get_info()
    """
    # настройка поиска валюты по ее коду
    digital_currency_mode = '?parammode=1'
    # настройка поиска валюты по аббревиатуре
    alphabetic_currency_mode = '?parammode=2'
    # настройка для поиска всех валют
    all_currency_mode = 'currencies'


class API:
    """
    Класс предназначен для получения актуального курса валют с нацбанка РБ через API
    """
    # Строка запроса API без указания валюты и режима работы
    __link = 'https://api.nbrb.by/exrates/'

    def get_info(self, input_currency: str,
                 mode=RequestMode.alphabetic_currency_mode) -> dict:
        """
        функция принимает введеную пользователем валюту,
         посылает запрос согласно указанному режиму работы,
          а полученный результат возвращает ввиде словаря json формата
        :param input_currency:
         аббревиатура или числовой код валюты пользователя в зависимости от выбранного режима
        :param mode: по умолчанию настроен на аббревиатурный запрос.
         Отвечает за настройку поиска по аббревиатуре или коду валюты
        :return: возвращает информацию о валюте в json формате
         или ошибку в ввиде словаря.
        """
        try:
            # Формируем строку ззапроса через API нац банка или генерируем бел руб.
            if input_currency == 'BYN' or input_currency == 'byn' or input_currency == 1:
                currency_json_format = {
                    'Cur_ID': 1,
                    'Date': datetime.datetime.now().strftime("%d-%m-%YT%H:%M:%S"),
                    'Cur_Abbreviation': 'BYN',
                    'Cur_Scale': 1,
                    'Cur_Name': 'Белорусский рубль',
                    'Cur_OfficialRate': 1}
            else:
                link = f'{self.__link}rates/{input_currency}{mode.value}'
                currency_json_format = requests.get(link).json()
            if currency_json_format.get('status') != 404:
                return currency_json_format
            else:
                return {"error_type": "Check input data. "
                                      "Incorrect currency entered "
                                      "or search error occurred"}
        except requests.exceptions.ConnectionError:
            return {"error_404": "Connection error..."}

    def get_all_abr_currency(self) -> list:
        """
        Делает запрос к api Национального банка Республики Беларусь
        с целью получения всех абривиатур валют доступных в Нац. банке.
        :return: list со всеми абривиатурами полученными из запроса.
        """
        link = f'{self.__link}' \
               f'{RequestMode.alphabetic_currency_mode.all_currency_mode.value}'
        currency_json_format = requests.get(link).json()
        byn_currency = {
                    'Cur_ID': 1,
                    'Date': datetime.datetime.now().strftime("%d-%m-%YT%H:%M:%S"),
                    'Cur_Abbreviation': 'BYN',
                    'Cur_Scale': 1,
                    'Cur_Name': 'Белорусский рубль',
                    'Cur_OfficialRate': 1}
        currency_json_format.insert(0, byn_currency)
        currency_list = []
        for currency_1 in currency_json_format:
            currency_list.append((currency_1['Cur_Abbreviation'],
                                  currency_1['Cur_Name']))
        return currency_list


if __name__ == '__main__':
    api = API()
    # for key, value in api.get_info("USD").items():
    #     print(f'{key}: {value}')
    # for key, value in api.get_info("841", RequestMode.digital_currency_mode).items():
    #     print(f'{key}: {value}')
    for currency in api.get_all_abr_currency():
        print(f"{currency[0]} - {currency[1]}")
