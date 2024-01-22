import requests

def get_currency_rates():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return data['Valute']
        else:
            print(f"Ошибка при получении данных: {response.status_code}")
            return None

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def display_currency_rates(rates):
    if rates:
        print("Курсы валют Центрального Банка России:")
        for currency_code, rate_info in rates.items():
            currency_name = rate_info['Name']
            exchange_rate = rate_info['Value']
            print(f"{currency_name} ({currency_code}) -> {exchange_rate}")

if __name__ == "__main__":
    currency_rates = get_currency_rates()

    if currency_rates:
        display_currency_rates(currency_rates)
