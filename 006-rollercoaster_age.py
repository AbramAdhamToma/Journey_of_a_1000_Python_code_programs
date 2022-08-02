# game roller coaster or death train 
# Nested if , esle , elif

print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster!")
    age= int(input("What is your age? "))
    if age < 12:
        print("Please Pay $5.")
    elif age <= 18:
        print("Please Pay $7.")
    elif age <=22:
        print("Please Pay 10")
    else:
        print("Please Pay $12.")
else:
    print(" Sorry, You have to grow taller before you can rider  ")
