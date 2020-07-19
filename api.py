import requests

def latest(base=None, symbols=None):
    if base == None and symbols == None:
        return requests.get('https://api.exchangeratesapi.io/latest').json()
    elif base != None and symbols == None:
        return requests.get(f'https://api.exchangeratesapi.io/latest?base={base}').json()
    elif base == None and symbols != None:
        if type(symbols) == type(str()):
            return requests.get(f'https://api.exchangeratesapi.io/latest?symbols={symbols}').json()
        else:
            pass
    else:
        if type(symbols) == type(str()):
            return requests.get(f'https://api.exchangeratesapi.io/latest?base={base}&symbols={symbols}').json()
        else:
            pass

def history_date(date):
    return requests.get(f'https://api.exchangeratesapi.io/{date}').json()

def history_term(start_date, end_date, base=None, symbols=None):
    if base == None and symbols == None:
        return requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_date}&end_at{end_date}').json()
    elif base != None and symbols == None:
        return requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_date}&end_at{end_date}&base={base}').json()
    elif base == None and symbols != None:
        return requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_date}&end_at{end_date}&symbols={symbols}').json()
    else:
        return requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_date}&end_at{end_date}&base={base}&symbols={symbols}').json()