# game roller coaster or death train 
# Nested if , esle , elif

print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster!")
    age= int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please Pay $5.")
    elif age <= 18:
        bill = 7
        print("Please Pay $7.")
    elif age <=22:
        bill = 10
        print("Please Pay 10")
    else:
        bill = 12
        print("Please Pay $12.")
    take_photo = input("Do you need take photo write by 3$ y or n ?")
    if take_photo == "y":
        bill += 3
        print(f"Yor total bill is {bill}")
    else:
            print(f"Yor total bill is {bill}")
else:
    print(" Sorry, You have to grow taller before you can rider  ")
