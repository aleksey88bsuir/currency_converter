def converter(convertible_currency: dict,
              wanted_currency: dict,
              convertible_amount: float) -> float:

    wanted_currency_result = \
        convertible_amount * wanted_currency['Cur_Scale'] * convertible_currency['Cur_OfficialRate'] / \
        (wanted_currency['Cur_OfficialRate'] * convertible_currency['Cur_Scale'])

    return round(wanted_currency_result, 4)


if __name__ == "__main__":
    from api import *
    api = API()
    convertible_cur = api.get_info("USD")
    wanted_cur = api.get_info("EUR")

    var = converter(convertible_cur, wanted_cur, 10.5)
    print(var)
