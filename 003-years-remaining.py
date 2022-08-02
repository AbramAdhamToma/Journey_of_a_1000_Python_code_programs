#  sub-string f

age = input("What is your current age?")
years_remaining = 90 - int(age)
age_days = years_remaining * 365
age_weeks = years_remaining * 52
age_mounth = years_remaining * 12

message=print(f"You have {age_days} days, {age_weeks} weeks, and {age_mounth} months left.")
print(message)  