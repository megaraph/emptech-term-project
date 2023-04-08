ORDER_1_MAIN = "Beef"
ORDER_1_MAIN_PRICE = 120.0

ORDER_1_SIDE = "Steam Vegetables"
ORDER_1_SIDE_PRICE = 35.0

ORDER_1_DRINK = "Fruit Juice"
ORDER_1_DRINK_PRICE = 0.0

TOTAL_AMOUNT = 300.0
num_members = 3

menu = """
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


print("Order 1:")
print(f"\t{'Main':<6}\t{ORDER_1_MAIN:22}\tP{ORDER_1_MAIN_PRICE:.2f}")
print(f"\t{'Side':<6}\t{ORDER_1_SIDE:<22}\tP{ORDER_1_SIDE_PRICE:.2f}")
print(f"\t{'Drink':<6}\t{ORDER_1_DRINK:<22}\tP{ORDER_1_DRINK_PRICE:.2f}")

ORDER_1_SUBTOTAL = ORDER_1_MAIN_PRICE + ORDER_1_SIDE_PRICE + ORDER_1_DRINK_PRICE
print(f"Subtotal:\t\t\t\t\tP{ORDER_1_SUBTOTAL}")

print(f"\nTotal Amount Due: \t\t\t\tP{TOTAL_AMOUNT}")
print(f"Each person must pay: \t\t\t\tP{(TOTAL_AMOUNT / num_members):.2f}")
