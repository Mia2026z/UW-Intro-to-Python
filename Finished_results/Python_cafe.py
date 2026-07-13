menu = ["Croissant", "Latte", "Black coffee", "Espresso", "Muffins", "Avocado toast", "Matcha", "Cappuccino"]

print("Welcome to Python cafe!")
print("First take a look at the menu please!")

day = 1

def specials(day):
    print("Todays daily special:")
    if day == 1:
        print("Cake pop : $2.50")
    elif day == 2:
        print("Iced tea : $4.00")
    elif day == 3:
        print("Lemonade : $4.00")
    elif day == 4:
        print("Lemon iced toast : $7.50")
    else:
        print("Hot chocolate : $4.50")
        
if day > 5:
    day = 1
specials(day)

print(menu)

prices = {
   "Croissant": 3.50,
   "Latte": 5.00,
   "Black Coffee": 3.00,
   "Espresso": 3.00,
   "Muffins": 3.50,
   "Avocado Toast": 8.50,
   "Matcha": 5.50,
   "Cappuccino": 5.00,
}

# Function to find the price of an item
def get_price(item):
   if item in prices:
       return prices[item]
   else:
       return None

# Customer ordering
total = 0
while True:
   order = input("What would you like to order? (type done to finish): ").title()
   if order == "Done":
       break
   price = get_price(order)
   if price is not None:
       print(order, "costs $", price)
       total += price
   else:
       print("Sorry, that item is not on the menu.")
print("-------------------")
print("Your total is: $", total)
print("Thank you for visiting Python Café!")

day += 1