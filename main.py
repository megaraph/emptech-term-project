# This is to certify that this project is my own work, based on my personal
# efforts in studying and applying the concepts learned. I have constructed
# the functions and their respective algorithms and corresponding code by
# myself. The program was run, tested, and debugged by my own efforts. I
# further certify that I have not copied in part or whole or otherwise
# plagiarized the work of other students and/or persons.
# Raphael C. Murillo, DLSU ID# 122

# Description: A system for handling meal orders
# Programmed by: Raphael C. Murillo STEM 11-B
# Last modified: <date when last revision was made>
# Version: <version number>
# Acknowledgements: <list of sites or borrowed libraries and sources>

MAX_ORDERS = 3

MAINS = [
    {"id": 1, "type": "Chicken", "price": 90.0},
    {"id": 2, "type": "Pork", "price": 105.0},
    {"id": 3, "type": "Fish", "price": 120.0},
    {"id": 4, "type": "Beef", "price": 135.0},
]

SIDES = [
    {"id": 1, "type": "Steamed Rice", "price": 20.0},
    {"id": 2, "type": "Shredded Corn", "price": 35.0},
    {"id": 3, "type": "Mashed Potatoes", "price": 50.0},
    {"id": 4, "type": "Steam Vegetables", "price": 65.0},
]

DRINKS = [
    {"id": 1, "type": "Mineral Water", "price": 25.0},
    {"id": 2, "type": "Iced Tea", "price": 35.0},
    {"id": 3, "type": "Soda", "price": 45.0},
    {"id": 4, "type": "Fruit Juice", "price": 65.0},
]


def main() -> None:
    print("\nWelcome! Would you like to order?")
    print("Type 'order' to continue, otherwise type 'exit'")

    order_prompt = input("Answer [order/exit]: ").lower()

    if order_prompt == "exit":
        print("Exiting...")
        return None

    if not order_prompt == "order":
        print("Exiting... input not among the choices: 'order' or 'exit'")
        return None

    num_members = int(input("\nHow many people are in your group: "))

    orders = []
    order_num = 0
    prompt_choices = ["y", "n"]
    while order_num < MAX_ORDERS:
        order = get_meal_order(order_num + 1)
        order_is_correct = input("Is this meal set order correct (y/n):? ").lower()

        if order_is_correct not in prompt_choices:
            # TODO: implement edge condition
            pass

        if order_is_correct == "n":
            continue

        orders.append(order)
        order_num += 1

        next_order = input("Proceed with next order (y/n)? ").lower()

        if next_order not in prompt_choices:
            # TODO: implement edge condition
            pass

        if next_order == "n":
            break

    print(f"\nOrder for party of {num_members}")
    checkout(orders, num_members)

    return None


def get_meal_order(order_num: int):
    print(f"\nOrder {order_num}:")
    order = {
        "order_num": order_num,
        "main": get_order_item("main", MAINS),
        "side": get_order_item("side", SIDES),
        "drink": get_order_item("drink", DRINKS),
    }

    return order


def get_order_item(order_type: str, order_list: list) -> dict:
    order_item_id = int(
        input(
            f"\t{order_type.title()}:\t\t",
        )
    )
    order_item = find_item_from_list(order_list, order_item_id)
    print(f"\t\t{order_item.get('type')}")

    return order_item


def find_item_from_list(order_list: list, order_id: int) -> dict:
    if order_id == None:
        return {}

    for item in order_list:
        if item["id"] == order_id:
            return item

    return {}


def checkout(orders, num_members) -> None:
    total_price = 0
    for order in orders:
        main = order["main"]
        side = order["side"]
        drink = order["drink"]

        main_price = main.get("price", 0)
        side_price = side.get("price", 0)
        drink_price = drink.get("price", 0)

        print(f"\nOrder {order['order_num']}:")
        print(f"\t{'Main':<6}\t{str(main.get('type')):<12}\tP{main_price:.2f}")
        print(f"\t{'Side':<6}\t{str(side.get('type')):<12}\tP{side_price:.2f}")
        print(f"\t{'Drink':<6}\t{str(drink.get('type')):<12}\tP{drink_price:.2f}")

        subtotal = main_price + side_price + drink_price
        total_price += subtotal
        print(f"Subtotal:\t\t\t\tP{subtotal:.2f}")

    indiv_payment = total_price / num_members
    print(f"\n\nTotal Amount Due:\t\t\tP{total_price:.2f}")
    print(f"\nEach Person must pay:\t\t\tP{indiv_payment:.2f}")

    return None


if __name__ == "__main__":
    main()
