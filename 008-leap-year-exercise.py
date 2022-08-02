year = int(input("write year you want to chack leap or not : "))
if year % 4 == 0:    
    if year % 100 == 0:
        if year % 400 == 0: 
            print(f"The {year} is LEAP")
        else:
            print(f"The {year} is NOT leap")
    else:
        print(f"The {year} is LEAP")
else:
    print(f"The {year} is NOT leap")

