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


def main():
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

    print(num_members, type(num_members))

    return None


if __name__ == "__main__":
    main()
