
def discount(price, category):
    if category == "student":
        return price * (0.9 if price > 1000 else 0.95)
    return price * 0.85 if price > 2000 else price
print(discount(1200, "student"))  # Should apply 10% discount
print(discount(800, "student"))   # Should apply 5% discount
print(discount(2500, "regular"))  # Should apply 15% discount
print(discount(1500, "regular"))  # Should return original price
