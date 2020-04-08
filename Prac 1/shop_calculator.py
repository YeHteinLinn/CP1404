def main():
    number_of_items = int(input("Number of items: "))
    total_price = 0
    while number_of_items < 0:
        print("Invalid number of items")
        number_of_items = input("Number of items")
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total_price = total_price + price

    if total_price > 100:
        total_price = total_price * 0.9

    print("Total price for ", number_of_items, "items is $", total_price)


if __name__ == '__main__':
    main()
