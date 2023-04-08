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
ORDER_1_MAIN_PRICE = None
ORDER_1_SIDE_PRICE = None
ORDER_1_DRINK_PRICE = None

# FINAL ORDER 2
ORDER_2_MAIN = None
ORDER_2_SIDE = None
ORDER_2_DRINK = None
ORDER_2_MAIN_PRICE = None
ORDER_2_SIDE_PRICE = None
ORDER_2_DRINK_PRICE = None

# FINAL ORDER 3
ORDER_3_MAIN = None
ORDER_3_SIDE = None
ORDER_3_DRINK = None
ORDER_3_MAIN_PRICE = None
ORDER_3_SIDE_PRICE = None
ORDER_3_DRINK_PRICE = None

# SUBTOTALS
ORDER_1_SUBTOTAL = 0.0
ORDER_2_SUBTOTAL = 0.0
ORDER_3_SUBTOTAL = 0.0

print("\nWelcome! Would you like to order?")
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
    if main == 0:
        print("\t\tNone")
    elif main == 1:
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

    side = int(input("\tSide:\t\t"))
    if side == 0:
        print("\t\tNone")
    elif side == 1:
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

    drink = int(input("\tDrink:\t\t"))
    if drink == 0:
        print("\t\tNone")
    elif drink == 1:
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

    is_correct = None
    while is_correct != "y" and is_correct != "n":
        if is_correct is not None:
            print(
                "\nWARNING: The answer you provided is not found within the choices: (y/n)"
            )
        is_correct = input(f"Is this order correct? (y/n)? ")

    if is_correct == "n":
        continue

    if not order_num == num_members:
        order_prompt_str = "Proceed with next order"
    else:
        order_prompt_str = "Cancel all orders"

    order_prompt = None
    while order_prompt != "y" and order_prompt != "n":
        if order_prompt is not None:
            print(
                "\nWARNING: The answer you provided is not found within the choices: (y/n)"
            )
        order_prompt = input(f"{order_prompt_str} (y/n)? ")

    # if user wants to cancel all orders
    if order_num == num_members and order_prompt == "y":
        ORDER_1_MAIN_PRICE = None
        ORDER_1_SIDE_PRICE = None
        ORDER_1_DRINK_PRICE = None

        ORDER_2_MAIN_PRICE = None
        ORDER_2_SIDE_PRICE = None
        ORDER_2_DRINK_PRICE = None

        ORDER_3_MAIN_PRICE = None
        ORDER_3_SIDE_PRICE = None
        ORDER_3_DRINK_PRICE = None

    # if user does not want to proceed with the next order
    elif order_num < num_members and order_prompt == "n":
        num_of_orders = order_num
        order_num = 4

    if order_num < num_members:
        order_num += 1
        continue

    exclude_count = 0
    new_line = "\n"
    while True:
        exclude_prompt = input(
            f"{new_line if exclude_count > 0 else ''}Exclude an item from the total (y/n)? "
        )
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
            elif item_to_exclude == 2:
                ORDER_1_SIDE_PRICE = 0.0
            elif item_to_exclude == 3:
                ORDER_1_DRINK_PRICE = 0.0
        elif order_to_exclude == 2:
            if item_to_exclude == 1:
                ORDER_2_MAIN_PRICE = 0.0
            elif item_to_exclude == 2:
                ORDER_2_SIDE_PRICE = 0.0
            elif item_to_exclude == 3:
                ORDER_2_DRINK_PRICE = 0.0
        elif order_to_exclude == 3:
            if item_to_exclude == 1:
                ORDER_3_MAIN_PRICE = 0.0
            elif item_to_exclude == 2:
                ORDER_3_SIDE_PRICE = 0.0
            elif item_to_exclude == 3:
                ORDER_3_DRINK_PRICE = 0.0

    order_num += 1


print(f"\nOrder for party of {num_members}\n")

if num_of_orders >= 1:
    print("Order 1:")
    print(f"\tMain:\t{ORDER_1_MAIN}\tP{ORDER_1_MAIN_PRICE}")
    print(f"\tSide:\t{ORDER_1_SIDE}\tP{ORDER_1_SIDE_PRICE}")
    print(f"\tDrink:\t{ORDER_1_DRINK}\tP{ORDER_1_DRINK_PRICE}")

    ORDER_1_SUBTOTAL = ORDER_1_MAIN_PRICE + ORDER_1_SIDE_PRICE + ORDER_1_DRINK_PRICE
    print(f"Subtotal:\t\t\t\tP{ORDER_1_SUBTOTAL}")

if num_of_orders >= 2:
    print("Order 2:")
    print(f"\tMain:\t{ORDER_2_MAIN}\tP{ORDER_2_MAIN_PRICE}")
    print(f"\tSide:\t{ORDER_2_SIDE}\tP{ORDER_2_SIDE_PRICE}")
    print(f"\tDrink:\t{ORDER_2_DRINK}\tP{ORDER_2_DRINK_PRICE}")

    ORDER_2_SUBTOTAL = ORDER_2_MAIN_PRICE + ORDER_2_SIDE_PRICE + ORDER_2_DRINK_PRICE
    print(f"Subtotal:\t\t\t\tP{ORDER_2_SUBTOTAL}")

if num_of_orders == 3:
    print("Order 3:")
    print(f"\tMain:\t{ORDER_3_MAIN}\tP{ORDER_3_MAIN_PRICE}")
    print(f"\tSide:\t{ORDER_3_SIDE}\tP{ORDER_3_SIDE_PRICE}")
    print(f"\tDrink:\t{ORDER_3_DRINK}\tP{ORDER_3_DRINK_PRICE}")

    ORDER_3_SUBTOTAL = ORDER_3_MAIN_PRICE + ORDER_3_SIDE_PRICE + ORDER_3_DRINK_PRICE
    print(f"Subtotal:\t\t\t\tP{ORDER_3_SUBTOTAL}")

print("Total Amount Due: ")
