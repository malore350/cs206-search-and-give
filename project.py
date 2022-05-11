import random

#Sorting (In-Place Quick Sort) (Can take two lists, and change order of the second one on the basis of main sorting of the first
def sortsys(S1, S2, a, b):
    if a >= b:
        return
    pivot = S1[b]
    left = a
    right = b - 1
    while left <= right:
        while left <= right and S1[left] < pivot:
            left += 1
        while left <= right and pivot < S1[right]:
            right -= 1
        if left <= right:
            S1[left], S1[right] = S1[right], S1[left]
            S2[left], S2[right] = S2[right], S2[left]
            left, right = left + 1, right - 1

    S1[left], S1[b] = S1[b], S1[left]
    S2[left], S2[b] = S2[b], S2[left]
    sortsys(S1, S2, a, left - 1)
    sortsys(S1, S2, left + 1, b)

#Main Operation
def restaurant():
    number = random.randint(1000, 9999)             #Randomly generated 4-digit number for order number

    food = ["Waffle Standard", "Waffle with Maple", "Waffle with Chocolate", "Sweet Strawberry", "Bubble Blow"]     #Menu of foods
    drinks = ["Cola", "Sprite", "Chocolate Smoothie", "Vanille Smoothie"]       #Menu of drinks
    info = {
        "food": ["This is just our best Waffle, and nothing else.", "This is our best Waffle together with Maple syrup. Legendary Combination", ""],
        "drinks": ["neise"]
        }                               #Full Descriptions of every food/drink, it is listed in order corresponding to food and drinks
    price_food = [3, 4, 7, 5, 5]        #Prices of every food in food (In corresponding order)
    price_drinks = [1, 1, 5, 4]         #Prices of every drink in drinks (In corresponding order)
    full = []                           #List, which is filled by the food/drinks that is being ordered
    qiymet = []                         #List, which is being filled by the prices of the food/drinks that are being ordered
    total_order = []                    #List, which is being filled with Tuples, which consist of Food/Drink name and its price

    while True:         #loop for going through the functions, works until interruped
        order = input("Welcome to Waffle Wagen! What would you love to order?")     #Main function input

        if order == 'exit':
            break           #Base line, when reached: Code gets interrupted

        elif order == "info":       #A function for dictionary call
            choice_type = input("About what would you love to learn more? Please type 'food' or 'drinks'")      #Depending on wether you choose food or drink 

            if choice_type == "food":                   #This part simply checks your object in food department
                choice_food = input("What waffle would you like to learn more about?")
                ind2 = food.index(choice_food)
                print(info["food"][ind2])

            elif choice_type == "drinks":           #This part simply checks your object in drinks department
                choice_drinks = input("What drink would you like to learn more about?")
                ind4 = drinks.index(choice_drinks)
                print(info["drinks"][ind4])

        elif order not in food:         #This part is for checking whether your input is inside the menu
            if order not in drinks:
                print("We do not have that in Menu!")               #Not in menu at all       
            elif order in drinks:
                ind3 = drinks.index(order)                          #Inside drinking department to be found
                full += [drinks[ind3]]
                qiymet += [price_drinks[ind3]]

        elif order in food:
            ind = food.index(order)                                 #Inside food Department to be found
            full += [food[ind]]
            qiymet += [price_food[ind]]
    
    #Result giving part
    fee = 0
    sortsys(qiymet, full, 0, len(full) - 1)             #We sort our items with respect to price, so that result will be very organized
    for i in range(len(full)):
        fee += qiymet[i]                                #Fee calculation part
        total_order += [(full[i], qiymet[i])]           #Tuple creation
    full_order = "Order Number: " + str(number) + " -> " + str(total_order)         #Creation of necessary outputs for return
    full_price = " Total: " + str(fee) + "$"
    return full_order, full_price


#While Restaurant Works, we will keep asking the orders (Implement Time Module)

all_orders = []
count = 0
while True:
    a = input("We still work?")
    if a == 'yes' or a == 'y' or a == "Yes" or a == "Yep":
        b = restaurant()
        print(b)
        all_orders += [b]
        count += 1
    else:
        print("Total Orders: " + str(count))
        break

print("Total Number of orders for Today:")
print(all_orders)