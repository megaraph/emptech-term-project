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
# Version: Python 3.9
# Acknowledgements: https://docs.python.org/3/

MENU = """
MAINS:
+---------------------------------------+
|  ID |   Type              |  Price    |
|     |                     |           |
|  1  |   Chicken           |  P90.00   |
|  2  |   Pork              |  P105.00  |
|  3  |   Fish              |  P120.00  |
|  4  |   Beef              |  P135.00  |
+---------------------------------------+

SIDES:
+---------------------------------------+
|  ID |   Type              |  Price    |
|     |                     |           |
|  1  |   Steamed Rice      |  P20.00   |
|  2  |   Shredded Corn     |  P35.00   |
|  3  |   Mashed Potatoes   |  P50.00   |
|  4  |   Steam Vegetables  |  P65.00   |
+---------------------------------------+

DRINKS:
+---------------------------------------+
|  ID |   Type              |  Price    |
|     |                     |           |
|  1  |   Mineral Water     |  P25.00   |
|  2  |   Iced Tea          |  P35.00   |
|  3  |   Soda              |  P45.00   |
|  4  |   Fruit Juice       |  P55.00   |
+---------------------------------------+
"""

MAX_ORDERS = 3

# MAINS TYPES
MAIN_1_TYPE = "Chicken"
MAIN_2_TYPE = "Pork"
MAIN_3_TYPE = "Fish"
MAIN_4_TYPE = "Beef"

# MAINS PRICES
MAIN_1_PRICE = 90.0
MAIN_2_PRICE = 105.0
MAIN_3_PRICE = 120.0
MAIN_4_PRICE = 135.0

# SIDES TYPES
SIDE_1_TYPE = "Steamed Rice"
SIDE_2_TYPE = "Shredded Corn"
SIDE_3_TYPE = "Mashed Potatoes"
SIDE_4_TYPE = "Steam Vegetables"

# SIDE PRICES
SIDE_1_PRICE = 20.0
SIDE_2_PRICE = 35.0
SIDE_3_PRICE = 50.0
SIDE_4_PRICE = 65.0

# DRINK TYPES
DRINK_1_TYPE = "Mineral Water"
DRINK_2_TYPE = "Iced Tea"
DRINK_3_TYPE = "Soda"
DRINK_4_TYPE = "Fruit Juice"

# DRINK PRICES
DRINK_1_PRICE = 25.0
DRINK_2_PRICE = 35.0
DRINK_3_PRICE = 45.0
DRINK_4_PRICE = 55.0

# FINAL ORDER 1
ORDER_1_MAIN = None
ORDER_1_SIDE = None
ORDER_1_DRINK = None
ORDER_1_MAIN_PRICE = 0.0
ORDER_1_SIDE_PRICE = 0.0
ORDER_1_DRINK_PRICE = 0.0

# FINAL ORDER 2
ORDER_2_MAIN = None
ORDER_2_SIDE = None
ORDER_2_DRINK = None
ORDER_2_MAIN_PRICE = 0.0
ORDER_2_SIDE_PRICE = 0.0
ORDER_2_DRINK_PRICE = 0.0

# FINAL ORDER 3
ORDER_3_MAIN = None
ORDER_3_SIDE = None
ORDER_3_DRINK = None
ORDER_3_MAIN_PRICE = 0.0
ORDER_3_SIDE_PRICE = 0.0
ORDER_3_DRINK_PRICE = 0.0

# SUBTOTALS
ORDER_1_SUBTOTAL = 0.0
ORDER_2_SUBTOTAL = 0.0
ORDER_3_SUBTOTAL = 0.0

print("\nWelcome! Would you like to order?")
print(MENU)
print("Type 'order' to continue, otherwise type 'exit'")

order_prompt = None
while order_prompt != "order" and order_prompt != "exit":
    if order_prompt is not None:
        print(
            "\nWARNING: The answer you provided is not found within the choices: (order/exit)"
        )
    order_prompt = input("Answer [order/exit]: ").lower()

if order_prompt == "exit":
    print("\nThank you for using our service! Come again next time.")
    print("Exiting...")
    exit()

num_members = -1
while not 1 <= num_members <= 3:
    num_members = int(input("\nHow many people are in your group: "))

    if num_members == 0:
        print("WARNING: Number of members can't be zero")

    if num_members < 0:
        print("WARNING: Number of members can't be a negative number")

    if num_members > 3:
        print("WARNING: Number of members can't be more than 3")

order_num = 1
while order_num <= num_members:
    print(f"\nOrder {order_num}:")

    main = int(input("\tMain:\t\t"))
    if main == 1:
        if order_num == 1:
            ORDER_1_MAIN = MAIN_1_TYPE
            ORDER_1_MAIN_PRICE = MAIN_1_PRICE
        elif order_num == 2:
            ORDER_2_MAIN = MAIN_1_TYPE
            ORDER_2_MAIN_PRICE = MAIN_1_PRICE
        elif order_num == 3:
            ORDER_3_MAIN = MAIN_1_TYPE
            ORDER_3_MAIN_PRICE = MAIN_1_PRICE
        print(f"\t\t{MAIN_1_TYPE}")
    elif main == 2:
        if order_num == 1:
            ORDER_1_MAIN = MAIN_2_TYPE
            ORDER_1_MAIN_PRICE = MAIN_2_PRICE
        elif order_num == 2:
            ORDER_2_MAIN = MAIN_2_TYPE
            ORDER_2_MAIN_PRICE = MAIN_2_PRICE
        elif order_num == 3:
            ORDER_3_MAIN = MAIN_2_TYPE
            ORDER_3_MAIN_PRICE = MAIN_2_PRICE
        print(f"\t\t{MAIN_2_TYPE}")
    elif main == 3:
        if order_num == 1:
            ORDER_1_MAIN = MAIN_3_TYPE
            ORDER_1_MAIN_PRICE = MAIN_3_PRICE
        elif order_num == 2:
            ORDER_2_MAIN = MAIN_3_TYPE
            ORDER_2_MAIN_PRICE = MAIN_3_PRICE
        elif order_num == 3:
            ORDER_3_MAIN = MAIN_3_TYPE
            ORDER_3_MAIN_PRICE = MAIN_3_PRICE
        print(f"\t\t{MAIN_3_TYPE}")
    elif main == 4:
        if order_num == 1:
            ORDER_1_MAIN = MAIN_4_TYPE
            ORDER_1_MAIN_PRICE = MAIN_4_PRICE
        elif order_num == 2:
            ORDER_2_MAIN = MAIN_4_TYPE
            ORDER_3_MAIN_PRICE = MAIN_4_PRICE
        elif order_num == 3:
            ORDER_3_MAIN = MAIN_4_TYPE
            ORDER_3_MAIN_PRICE = MAIN_4_PRICE
        print(f"\t\t{MAIN_4_TYPE}")
    else:
        print("\t\tNone")

    side = int(input("\tSide:\t\t"))
    if side == 1:
        if order_num == 1:
            ORDER_1_SIDE = SIDE_1_TYPE
            ORDER_1_SIDE_PRICE = SIDE_1_PRICE
        elif order_num == 2:
            ORDER_2_SIDE = SIDE_1_TYPE
            ORDER_2_SIDE_PRICE = SIDE_1_PRICE
        elif order_num == 3:
            ORDER_3_SIDE = SIDE_1_TYPE
            ORDER_3_SIDE_PRICE = SIDE_1_PRICE
        print(f"\t\t{SIDE_1_TYPE}")
    elif side == 2:
        if order_num == 1:
            ORDER_1_SIDE = SIDE_2_TYPE
            ORDER_1_SIDE_PRICE = SIDE_2_PRICE
        elif order_num == 2:
            ORDER_2_SIDE = SIDE_2_TYPE
            ORDER_2_SIDE_PRICE = SIDE_2_PRICE
        elif order_num == 3:
            ORDER_3_SIDE = SIDE_2_TYPE
            ORDER_3_SIDE_PRICE = SIDE_2_PRICE
        print(f"\t\t{SIDE_2_TYPE}")
    elif side == 3:
        if order_num == 1:
            ORDER_1_SIDE = SIDE_3_TYPE
            ORDER_1_SIDE_PRICE = SIDE_3_PRICE
        elif order_num == 2:
            ORDER_2_SIDE = SIDE_3_TYPE
            ORDER_2_SIDE_PRICE = SIDE_3_PRICE
        elif order_num == 3:
            ORDER_3_SIDE = SIDE_3_TYPE
            ORDER_3_SIDE_PRICE = SIDE_3_PRICE
        print(f"\t\t{SIDE_3_TYPE}")
    elif side == 4:
        if order_num == 1:
            ORDER_1_SIDE = SIDE_4_TYPE
            ORDER_1_SIDE_PRICE = SIDE_4_PRICE
        elif order_num == 2:
            ORDER_2_SIDE = SIDE_4_TYPE
            ORDER_2_SIDE_PRICE = SIDE_4_PRICE
        elif order_num == 3:
            ORDER_3_SIDE = SIDE_4_TYPE
            ORDER_3_SIDE_PRICE = SIDE_4_PRICE
        print(f"\t\t{SIDE_4_TYPE}")
    else:
        print("\t\tNone")

    drink = int(input("\tDrink:\t\t"))
    if drink == 1:
        if order_num == 1:
            ORDER_1_DRINK = DRINK_1_TYPE
            ORDER_1_DRINK_PRICE = DRINK_1_PRICE
        elif order_num == 2:
            ORDER_2_DRINK = DRINK_1_TYPE
            ORDER_2_DRINK_PRICE = DRINK_1_PRICE
        elif order_num == 3:
            ORDER_3_DRINK = DRINK_1_TYPE
            ORDER_3_DRINK_PRICE = DRINK_1_PRICE
        print(f"\t\t{DRINK_1_TYPE}")
    elif drink == 2:
        if order_num == 1:
            ORDER_1_DRINK = DRINK_2_TYPE
            ORDER_1_DRINK_PRICE = DRINK_2_PRICE
        elif order_num == 2:
            ORDER_2_DRINK = DRINK_2_TYPE
            ORDER_2_DRINK_PRICE = DRINK_2_PRICE
        elif order_num == 3:
            ORDER_3_DRINK = DRINK_2_TYPE
            ORDER_3_DRINK_PRICE = DRINK_2_PRICE
        print(f"\t\t{DRINK_2_TYPE}")
    elif drink == 3:
        if order_num == 1:
            ORDER_1_DRINK = DRINK_3_TYPE
            ORDER_1_DRINK_PRICE = DRINK_3_PRICE
        elif order_num == 2:
            ORDER_2_DRINK = DRINK_3_TYPE
            ORDER_2_DRINK_PRICE = DRINK_3_PRICE
        elif order_num == 3:
            ORDER_3_DRINK = DRINK_3_TYPE
            ORDER_3_DRINK_PRICE = DRINK_3_PRICE
        print(f"\t\t{DRINK_3_TYPE}")
    elif drink == 4:
        if order_num == 1:
            ORDER_1_DRINK = DRINK_4_TYPE
            ORDER_1_DRINK_PRICE = DRINK_4_PRICE
        elif order_num == 2:
            ORDER_2_DRINK = DRINK_4_TYPE
            ORDER_2_DRINK_PRICE = DRINK_4_PRICE
        elif order_num == 3:
            ORDER_3_DRINK = DRINK_4_TYPE
            ORDER_3_DRINK_PRICE = DRINK_4_PRICE
        print(f"\t\t{DRINK_4_TYPE}")
    else:
        print("\t\tNone")

    is_correct = None
    while is_correct != "y" and is_correct != "n":
        if is_correct is not None:
            print(
                "\nWARNING: The answer you provided is not found within the choices: (y/n)"
            )
        is_correct = input(f"Is this order correct? (y/n)? ").lower()

    if is_correct == "n":
        continue

    if order_num < num_members:
        next_order = None
        while next_order != "y" and next_order != "n":
            if next_order is not None:
                print(
                    "\nWARNING: The answer you provided is not found within the choices: (y/n)"
                )
            next_order = input(f"Proceed with next order (y/n)? ").lower()

        if next_order == "y":
            order_num += 1
            continue

    num_of_orders = order_num
    order_num = 4

    cancel_all = None
    while cancel_all != "y" and cancel_all != "n":
        if cancel_all is not None:
            print(
                "\nWARNING: The answer you provided is not found within the choices: (y/n)"
            )
        cancel_all = input(f"Cancel all orders (y/n)? ").lower()

    # if user wants to cancel all orders
    if cancel_all == "y":
        # FINAL ORDER 1
        ORDER_1_MAIN = None
        ORDER_1_SIDE = None
        ORDER_1_DRINK = None
        ORDER_1_MAIN_PRICE = 0.0
        ORDER_1_SIDE_PRICE = 0.0
        ORDER_1_DRINK_PRICE = 0.0

        # FINAL ORDER 2
        ORDER_2_MAIN = None
        ORDER_2_SIDE = None
        ORDER_2_DRINK = None
        ORDER_2_MAIN_PRICE = 0.0
        ORDER_2_SIDE_PRICE = 0.0
        ORDER_2_DRINK_PRICE = 0.0

        # FINAL ORDER 3
        ORDER_3_MAIN = None
        ORDER_3_SIDE = None
        ORDER_3_DRINK = None
        ORDER_3_MAIN_PRICE = 0.0
        ORDER_3_SIDE_PRICE = 0.0
        ORDER_3_DRINK_PRICE = 0.0

        # SUBTOTALS
        ORDER_1_SUBTOTAL = 0.0
        ORDER_2_SUBTOTAL = 0.0
        ORDER_3_SUBTOTAL = 0.0

        order_num = 1

        print("\nAll orders canceled...")

        continue

    exclude_count = 0
    new_line = "\n"
    while True:
        exclude_prompt = input(
            f"{new_line if exclude_count > 0 else ''}Exclude an{'other' if exclude_count > 0 else ''} item from the total (y/n)? "
        ).lower()
        exclude_count += 1

        if exclude_prompt != "y" and exclude_prompt != "n":
            print("WARNING: Provide a valid input (y/n)")
            continue
        elif exclude_prompt == "n":
            break

        order_to_exclude = int(input("From which order? "))
        item_to_exclude = int(input("Which item will be excluded? "))

        if order_to_exclude == 1:
            if item_to_exclude == 1:
                ORDER_1_MAIN_PRICE = 0.0
                print(f"{ORDER_1_MAIN} will be excluded from the total.")
            elif item_to_exclude == 2:
                ORDER_1_SIDE_PRICE = 0.0
                print(f"{ORDER_1_SIDE} will be excluded from the total.")
            elif item_to_exclude == 3:
                ORDER_1_DRINK_PRICE = 0.0
                print(f"{ORDER_1_DRINK} will be excluded from the total.")
            else:
                print("None will be excluded from the total.")
        elif order_to_exclude == 2:
            if item_to_exclude == 1:
                ORDER_2_MAIN_PRICE = 0.0
                print(f"{ORDER_2_MAIN} will be excluded from the total.")
            elif item_to_exclude == 2:
                ORDER_2_SIDE_PRICE = 0.0
                print(f"{ORDER_2_SIDE} will be excluded from the total.")
            elif item_to_exclude == 3:
                ORDER_2_DRINK_PRICE = 0.0
                print(f"{ORDER_2_DRINK} will be excluded from the total.")
            else:
                print("None will be excluded from the total.")
        elif order_to_exclude == 3:
            if item_to_exclude == 1:
                ORDER_3_MAIN_PRICE = 0.0
                print(f"{ORDER_3_MAIN} will be excluded from the total.")
            elif item_to_exclude == 2:
                ORDER_3_SIDE_PRICE = 0.0
                print(f"{ORDER_3_SIDE} will be excluded from the total.")
            elif item_to_exclude == 3:
                ORDER_3_DRINK_PRICE = 0.0
                print(f"{ORDER_3_DRINK} will be excluded from the total.")
            else:
                print("None will be excluded from the total.")
        else:
            print("None will be excluded from the total.")

    order_num += 1


print(f"\nOrder for party of {num_members}\n")

if num_of_orders >= 1:
    print("Order 1:")
    print(f"\t{'Main':<6}\t{ORDER_1_MAIN:<22}\tP{ORDER_1_MAIN_PRICE:.2f}")
    print(f"\t{'Side':<6}\t{ORDER_1_SIDE:<22}\tP{ORDER_1_SIDE_PRICE:.2f}")
    print(f"\t{'Drink':<6}\t{ORDER_1_DRINK:<22}\tP{ORDER_1_DRINK_PRICE:.2f}")

    ORDER_1_SUBTOTAL = ORDER_1_MAIN_PRICE + ORDER_1_SIDE_PRICE + ORDER_1_DRINK_PRICE
    print(f"Subtotal:\t\t\t\t\tP{ORDER_1_SUBTOTAL:.2f}")

if num_of_orders >= 2:
    print("Order 2:")
    print(f"\t{'Main':<6}\t{ORDER_2_MAIN:<22}\tP{ORDER_2_MAIN_PRICE:.2f}")
    print(f"\t{'Side':<6}\t{ORDER_2_SIDE:<22}\tP{ORDER_2_SIDE_PRICE:.2f}")
    print(f"\t{'Drink':<6}\t{ORDER_2_DRINK:<22}\tP{ORDER_2_DRINK_PRICE:.2f}")

    ORDER_2_SUBTOTAL = ORDER_2_MAIN_PRICE + ORDER_2_SIDE_PRICE + ORDER_2_DRINK_PRICE
    print(f"Subtotal:\t\t\t\t\tP{ORDER_2_SUBTOTAL:.2f}")

if num_of_orders == 3:
    print("Order 3:")
    print(f"\t{'Main':<6}\t{ORDER_3_MAIN:<22}\tP{ORDER_3_MAIN_PRICE:.2f}")
    print(f"\t{'Side':<6}\t{ORDER_3_SIDE:<22}\tP{ORDER_3_SIDE_PRICE:.2f}")
    print(f"\t{'Drink':<6}\t{ORDER_3_DRINK:<22}\tP{ORDER_3_DRINK_PRICE:.2f}")

    ORDER_3_SUBTOTAL = ORDER_3_MAIN_PRICE + ORDER_3_SIDE_PRICE + ORDER_3_DRINK_PRICE
    print(f"Subtotal:\t\t\t\t\tP{ORDER_3_SUBTOTAL:.2f}")

TOTAL_AMOUNT = ORDER_1_SUBTOTAL + ORDER_2_SUBTOTAL + ORDER_3_SUBTOTAL
print(f"\nTotal Amount Due: \t\t\t\tP{TOTAL_AMOUNT:.2f}")
print(f"Each person must pay: \t\t\t\tP{(TOTAL_AMOUNT / num_members):.2f}")
