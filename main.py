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

# MAINS
MAIN_1_TYPE = "Chicken"
MAIN_1_PRICE = 90.0
MAIN_2_TYPE = "Pork"
MAIN_2_PRICE = 105.0
MAIN_3_TYPE = "Fish"
MAIN_3_PRICE = 120.0
MAIN_4_TYPE = "Beef"
MAIN_4_PRICE = 135.0

# SIDES
SIDE_1_TYPE = "Steamed Rice"
SIDE_1_PRICE = 20.0
SIDE_2_TYPE = "Shredded Corn"
SIDE_2_PRICE = 35.0
SIDE_3_TYPE = "Mashed Potatoes"
SIDE_3_PRICE = 50.0
SIDE_4_TYPE = "Steam Vegetables"
SIDE_4_PRICE = 65.0

# DRINKS
DRINK_1_TYPE = ""
DRINK_1_PRICE = 20.0
DRINK_2_TYPE = "Shredded Corn"
DRINK_2_PRICE = 35.0
DRINK_3_TYPE = "Mashed Potatoes"
DRINK_3_PRICE = 50.0
DRINK_4_TYPE = "Steam Vegetables"
DRINK_4_PRICE = 65.0

# FINAL ORDERS
ORDER_1_MAIN = None
ORDER_1_SIDE = None
ORDER_1_DRINK = None

ORDER_2_MAIN = None
ORDER_2_SIDE = None
ORDER_2_DRINK = None

ORDER_3_MAIN = None
ORDER_3_SIDE = None
ORDER_3_DRINK = None

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
	print("\Thank you for using our service! Come again next time.")
	print("Exiting...")
	exit()

num_members = -1
while not 1 <= num_members <= 3:
	num_members = int(input("\nHow many people are in your group: "))

	if num_members < 0:
		print("WARNING: Number of members can't be a negative number")
		
	if num_members > 3:
		print("WARNING: Number of members can't be more than 3")

order_num = 0
while order_num < num_members:
	main = int(input("\tMain:\t\t"))
	if main == 0:
		if order_num == 1:
			ORDER_1_MAIN = None
		elif order_num == 2:
			ORDER_2_MAIN = None
		elif order_num == 3:
			ORDER_3_MAIN = None
	elif main == 1:
		if order_num == 1:
			ORDER_1_MAIN = MAIN_1_TYPE
		elif order_num == 2:
			ORDER_2_MAIN = MAIN_1_TYPE
		elif order_num == 3:
			ORDER_3_MAIN = MAIN_1_TYPE
	elif main == 2:
		if order_num == 1:
			ORDER_1_MAIN = MAIN_2_TYPE
		elif order_num == 2:
			ORDER_2_MAIN = MAIN_2_TYPE
		elif order_num == 3:
			ORDER_3_MAIN = MAIN_2_TYPE
	elif main == 3:
		if order_num == 1:
			ORDER_1_MAIN = MAIN_3_TYPE
		elif order_num == 2:
			ORDER_2_MAIN = MAIN_3_TYPE
		elif order_num == 3:
			ORDER_3_MAIN = MAIN_3_TYPE
		
	side = input("\tSide:\t\t")
	
	
	drink = input("\tDrink:\t\t")
	
	order_is_correct = initiate_prompt("Is this order correct (y/n)? ")

	if order_is_correct == "n":
		continue

	orders.append(order)
	order_num += 1

	next_order = initiate_prompt("Proceed with next order (y/n)? ")

	if next_order == "n":
		break
