states = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]
states.append("Viniland")
states.extend(["Steteland", "Lilaland"])
for i in states:
    print(i)

# New lesson, working with nested lists

fruits = ["Banana", "Apples", "Grapes"]
vegetables = ["Kale", "Spinach", "Tomatoes"]

dirty_dozen = [fruits, vegetables]

len_list = len(dirty_dozen)
print(len_list)
print(dirty_dozen)

