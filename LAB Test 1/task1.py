def currency_converter():
    exchange_rates = {
        'USD': 87.64,    # 1 USD = 87.64 INR
        'GBP': 118.63,   # 1 GBP = 118.63 INR
        'EUR': 94.50     # Example: 1 EUR = 94.50 INR
    }

    print("Available currencies: USD, GBP, EUR")
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., INR): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))

    if from_currency not in exchange_rates or to_currency != 'INR':
        print("Conversion only supported from USD, GBP, EUR to INR.")
        return

    converted_amount = amount * exchange_rates[from_currency]
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# Example usage
currency_converter()