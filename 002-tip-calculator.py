
# Pamdas way , float , sub-string f
#my answer
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip =  int (input("How much tip would you like to five? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tips_amount = float(tip / 100) * bill
every_one_payed_tips = float(tips_amount / people)
total_amount_payed = float(tips_amount + bill) / people
print(float(round(total_amount_payed, 2)))

#secound Answer 
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip =  int (input("How much tip would you like to five? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_persent = tip / 100
total_tip_amount = bill * tip_as_persent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each Person shouud pay: ${final_amount}")
