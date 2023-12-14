# Program using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old. (Inspo: https://waitbutwhy.com/2014/05/life-weeks.html)
age = input("What is your current age? \n ")
age_int = int(age)
weeks_mult = age_int*52
weeks_total = 4680 - weeks_mult
print(f"You have {weeks_total} weeks left.")
