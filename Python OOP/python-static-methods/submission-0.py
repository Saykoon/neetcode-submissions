class CurrencyConverter:
    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class attribute

    # TODO: Implement the static method `to_usd`
    @staticmethod
    def to_usd(num: float, currency: str) -> float:
        valid_currency = ['EUR', 'JPY']
        if currency in valid_currency:
            if currency == 'EUR':
                result = num * 1.2
                return result
            elif currency == 'JPY':
                result = num * 0.01
                return result
            else:
                return None
        else:
            return None

    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
