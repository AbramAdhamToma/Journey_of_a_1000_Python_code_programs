# game roller coaster or death train 
# Nested if , esle , elif

print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age= int(input("What is your age? "))
    if age < 12:
        print("Please Pay $5.")
        bill = 5
        take_photo = input("Do you need take photo write by 3$ y or n ?")
        if take_photo == "y":
            bill += 3
            print(f"Yor total bill is {bill}")
        else:
            print(f"Yor total bill is {bill}")
    elif age <= 18:
        print("Please Pay $7.")
        bill = 7
        take_photo = input("Do you need take photo write by 3$ y or n ?")
        if take_photo == "y":
            bill += 3
            print(f"Yor total bill is {bill}")
        else:
            print(f"Yor total bill is {bill}")
    elif age <=22:
        print("Please Pay 10")
        bill = 10
        take_photo = input("Do you need take photo write by 3$ y or n ?")
        if take_photo == "y":
            bill += 3
            print(f"Yor total bill is {bill}")
        else:
            print(f"Yor total bill is {bill}")
    else:
        print("Please Pay $12.")
        bill = 12
        take_photo = input("Do you need take photo write by 3$ y or n ?")
        if take_photo == "y":
            bill += 3
            print(f"Yor total bill is {bill}")
        else:
            print(f"Yor total bill is {bill}")
else:
    print(" Sorry, You have to grow taller before you can rider  ")
