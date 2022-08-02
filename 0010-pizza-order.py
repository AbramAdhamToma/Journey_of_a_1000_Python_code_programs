# My code

print("****Welcome in our Resturant****")
resturant_menu =print("We provide kinds of pizza:\n Small Pezza for $15 \n Medium Pezza for $20 \n Large Pezza for $25")
bill = 0
size_pizza = input("witch size of pezza you want ?  S , M or L ")
if size_pizza == "S":
    bill += 15
elif size_pizza == "M":
    bill +=20
elif size_pizza == "L":
    bill += 25    
else:
    print(" We hope see you agian ")
    
ask_about_addition = input("Are you prefre addition ? write Y for yes or N  for no ")
if size_pizza != "L":
    if ask_about_addition =="Y":
            addition_menu = input("pepperoni: $2 \n Cheese $1 \n write P for pepperoni C for cheese A for all ")
            if addition_menu == "P":
                bill += 2
                print(f"Total bill is: {bill}")
                
            elif addition_menu == "C":
                bill += 1
                print(f"Total bill is: {bill}")
            elif addition_menu == "A":
                    bill += 3
                    print(f"Total bill is: {bill}")
    else:
        print(f"Total bill is: {bill}")
else:
    addition_menu = input("pepperoni: $2 \n Cheese $1 \n write P for pepperoni C for cheese A for all ")    
    if addition_menu == "P":
        bill += 2
        print(f"Total bill is: {bill}") 
    elif addition_menu == "C":
        bill += 1
        print(f"Total bill is: {bill}")
    elif addition_menu == "A":
            bill += 3
            print(f"Total bill is: {bill}")
    else:
        print(f"Total bill is: {bill}")

    
    
# # Dr Angula 

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# # elif size == "L" another way code
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size =="S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
    
# print(f"Your total bill is ${bill}")




