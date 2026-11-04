def calculate_discount(price, discount_percentage):
    if price <= 0:
        return "Invalid price"

    if discount_percentage < 0 or discount_percentage > 100:
        return "Invalid discount percentage"

    discount = price * discount_percentage / 100
    return price - discount