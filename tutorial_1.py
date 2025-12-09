def sum_valid_prices(price_list):
    sum_price=0
    for price in price_list:
        if price.lower()=="free":
            price=0.0
        elif "$" in price:
            price=price.replace("$", "")
        try:
            sum_price+=float(price)
        except ValueError:
            print(f"Skipping invalid price: {price}")
    return sum_price

raw_prices = ["$12.50", "Free", "error_404", "$5.00", "2.50", "N/A"]
total = sum_valid_prices(raw_prices)
print(f"Total: ${total}")