age = input("Insert your age first\n")

week_year = 52
max_weeks = int(week_year) * 90
age_lived = int(age) * week_year

print (f"one year: {week_year}, 90 years week {max_weeks}, your age weeks {age_lived}, your time left in weeks {max_weeks - age_lived}")
