# from datetime import date

# def calculate_age(dtob):
#     today = date.today()
#     return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
# print()
# print(calculate_age(date(2006,10,12)))
# print(calculate_age(date(1994,2,2)))
# print()

from datetime import date

dob = date(1990, 2, 2)

t   = date.today()

age = t.year - dob.year - ((t.month, t.day) < (dob.month, dob.day))

print(age)