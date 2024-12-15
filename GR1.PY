#FILE :2252_AhmedAbdirahman_Lesson01_GR1_Lab.py
#NAME:  Store Purchase Calculator  & Dining Out
#AUTHOR(s): abdirahman ahmed 
#DAte: 9/7/2024


# Store Purchase
#Goal: Calculate the subtotal, total tax, and the final amount a customer needs to pay after buying 3 items.


sales_tax_rate = float(input("Enter the sales tax rate (as a percentage, e.g., 7.5 for 7.5%): ")) / 100
item1_price = float(input("Enter the price of item 1: "))
item2_price = float(input("Enter the price of item 2: "))
item3_price = float(input("Enter the price of item 3: "))

subtotal = item1_price + item2_price + item3_price 

total_tax = subtotal * sales_tax_rate

total_amount = subtotal + total_tax

print("\nSubtotal of the sale: ${:.2f}".format(subtotal))
print("Total amount of tax to be collected: ${:.2f}".format(total_tax))
print("Total amount the customer must pay: ${:.2f}".format(total_amount))

print(input('\n\nHit Enter to Close\n'))


 #Dining Out
#objective: Calculate the total bill at a restaurant including tip and sales tax.

total_cost = float(input("Enter the total cost of food and drink: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

sales_tax_rate = 0.065  # 6.5%
sales_tax = total_cost * sales_tax_rate

tip = total_cost * (tip_percentage / 100)

total_bill = total_cost + sales_tax + tip

print("\nSubtotal: ${:.2f}".format(total_cost))
print("Tip: ${:.2f}".format(tip))
print("Sales Tax: ${:.2f}".format(sales_tax))
print("Total Amount of the Bill: ${:.2f}".format(total_bill))

print(input('\n\nHit Enter to Close\n'))


