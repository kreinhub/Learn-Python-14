def discounted(price, discount, max_discount=90):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))

    if max_discount > 99:
        raise Exception
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


if __name__ == "__main__":
    try:
        print(discounted("pisos", 200, 100))
    except (TypeError, ValueError):
        print("Error")
    except Exception:
        print("Too big max discount")


