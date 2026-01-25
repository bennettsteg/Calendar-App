BOUQUET_COST = 17
EXTRAFLOWERS_COST = .35
TIP_EXPENSE = .15
SALES_TAX = 0.18

total_bouquet_cost = 0
total_extra_flowers_cost = 0

number_of_bouquets = int(input("Enter number of bouquets that have been purchased: "))
extra_flowers = int(input("Enter number of extra flowers that have been purchased: "))

total_bouquet_cost = BOUQUET_COST * number_of_bouquets
total_extra_flowers_cost = EXTRAFLOWERS_COST * extra_flowers

total_order_cost = (1 + TIP_EXPENSE) * (total_bouquet_cost + total_extra_flowers_cost) + (number_of_bouquets * SALES_TAX)

print(f"The total cost of the order is: ${total_order_cost}")