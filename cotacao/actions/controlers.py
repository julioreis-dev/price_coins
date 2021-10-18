import requests


def read_api(date: str) -> list:
    """
    :param date: A date to be used in address API
    :return: list
    """
    list_result = []
    address = f'https://api.vatcomply.com/rates?base=USD&date={date}'
    response = requests.get(url=f'{address}')
    data = response.json()
    coins = ['BRL', 'EUR', 'JPY']
    for coin in coins:
        try:
            result_info = (data['date'], coin, round(data['rates'][coin], 2))
            list_result.append(list(result_info))
        except KeyError:
            result_info = (data['date'], coin, 0.0)
            list_result.append(list(result_info))
    return list_result

# print(read_api('2001-04-16'))
