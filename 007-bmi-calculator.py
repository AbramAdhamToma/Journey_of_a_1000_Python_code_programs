#BMI Calc

Weight = int(input("Write your Weight "))
hight = int(input("Write your hight in cm "))
bmi = int(Weight / (hight /100 ) **2)
if bmi < 18.5:
    print ("You are underweight")
if bmi < 25:
    print(f"Your bmi is {bmi}, You have a normal weight")
elif bmi < 30 :
    print (f"Your bmi is {bmi}, You have a over weight")
elif bmi < 35 :
    print (f"Your bmi is {bmi}, You are Obese")
else:
    print (f"Your bmi is {bmi}, Clinically Obese")


