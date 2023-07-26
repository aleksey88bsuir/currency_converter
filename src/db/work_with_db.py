from db.models import Currency, History, Session
from datetime import datetime


class WorkWithCurrency:

    @staticmethod
    def create_or_update(currency_dict: dict) -> None:
        """
        Добавляет новые записи в таблицу или обновляет уже имеющиеся
        :param currency_dict: принимает данные о валюте в виде словаря
        :return: None
        """
        with Session() as session:
            new_data = Currency(
                cur_id=currency_dict.get('Cur_ID'),
                cur_abbreviation=currency_dict.get('Cur_Abbreviation'),
                cur_scale=currency_dict.get('Cur_Scale'),
                cur_name=currency_dict.get('Cur_Name'),
                cur_official_rate=currency_dict.get('Cur_OfficialRate'),
                date_time=currency_dict.get('Date'),
                last_query_time=datetime.now())

            if not session.query(Currency).\
                    filter(Currency.cur_id == currency_dict.get('Cur_ID')).all():
                session.add(new_data)
            else:
                session.query(Currency).\
                    filter(Currency.cur_id == currency_dict.get('Cur_ID')).update(
                    dict(cur_scale=currency_dict.get('Cur_Scale'),
                         cur_official_rate=currency_dict.get('Cur_OfficialRate'),
                         date_time=currency_dict.get('Date'),
                         last_query_time=datetime.now()),
                    synchronize_session=False
                )
            session.commit()

    @staticmethod
    def read(cur_abbreviation):
        with Session() as session:
            read_currency = session.query(Currency).filter(Currency.cur_abbreviation == cur_abbreviation).first()
            if read_currency:
                return_read_currency = {
                        'Cur_ID': read_currency.cur_id,
                        'Date': read_currency.date_time,
                        'Cur_Abbreviation': read_currency.cur_abbreviation,
                        'Cur_Scale': read_currency.cur_scale,
                        'Cur_Name': read_currency.cur_name,
                        'Cur_OfficialRate': read_currency.cur_official_rate,
                }
            else:
                return_read_currency = {
                        'Cur_ID': None,
                        'Date': None,
                        'Cur_Abbreviation': None,
                        'Cur_Scale': None,
                        'Cur_Name': None,
                        'Cur_OfficialRate': None,
                }
            return return_read_currency

    @staticmethod
    def delete(cur_id):
        with Session() as session:
            your_currency = session.query(Currency).filter(Currency.cur_id == cur_id).first()
            if your_currency:
                session.delete(your_currency)
                session.commit()
            else:
                print('Currency not found!')

    @staticmethod
    def read_all_available_currency():
        with Session() as session:
            available_currency = session.query(Currency.cur_abbreviation,
                                               Currency.cur_name).all()
            return available_currency


class WorkWithHistory:

    @staticmethod
    def create(convertible_currency: dict,
              wanted_currency: dict,
              convertible_amount_: float,
              wanted_currency_result_: float) -> None:
        """
        Добавляет новые записи в таблицу или обновляет уже имеющиеся
        :param currency_dict: принимает данные о валюте в виде словаря
        :return: None
        """
        new_data = History(
            cur_id_convertible=convertible_currency.get('Cur_ID'),
            cur_abbreviation_convertible=convertible_currency.get('Cur_Abbreviation'),
            cur_scale_convertible=convertible_currency.get('Cur_Scale'),
            cur_name_convertible=convertible_currency.get('Cur_Name'),
            cur_official_rate_convertible=convertible_currency.get('Cur_OfficialRate'),
            cur_id_wanted=wanted_currency.get('Cur_ID'),
            cur_abbreviation_wanted=wanted_currency.get('Cur_Abbreviation'),
            cur_scale_wanted=wanted_currency.get('Cur_Scale'),
            cur_name_wanted=wanted_currency.get('Cur_Name'),
            cur_official_rate_wanted=wanted_currency.get('Cur_OfficialRate'),
            actual_curs_date=wanted_currency.get('Date'),
            convertible_amount=convertible_amount_,
            wanted_currency_result=wanted_currency_result_
            )

        with Session() as session:
            session.add(new_data)
            session.commit()

    @staticmethod
    def read():
        with Session() as session:
            if data := session.query(History).all():
                return data
            else:
                return None

    @staticmethod
    def delete():
        with Session() as session:
            try:
                session.query(History).delete()
                session.commit()
            except:
                session.rollback()


if __name__ == '__main__':
    w = WorkWithCurrency()
    # currency_json_format = {
    #                 'Cur_ID': 1,
    #                 'Date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    #                 'Cur_Abbreviation': 'BYN',
    #                 'Cur_Scale': 1,
    #                 'Cur_Name': 'Бел рубль',
    #                 'Cur_OfficialRate': 1}
    # w.create_or_update(currency_json_format)
    print(w.read_all_available_currency())


