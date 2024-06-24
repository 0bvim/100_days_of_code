programming_dict = {
    "Bug": "I don't like of yellow submarine music.",
    "Error": "Misleading identation",
    "Loop": "Loop detected",
}

# the value to retrieve the value is the key like example below
print(programming_dict["Bug"])
print(programming_dict["Error"])
print(programming_dict["Loop"])

# adding new value
programming_dict["Hello"] = "Hello, how are you today?"
print(programming_dict["Hello"])

# creating new empty dict
empty_dict = {}

# to wipe an existing dictionary
programming_dict = {}
print(programming_dict)

# editing an existing entry
programming_dict["Bug"] = "Not more a bug"
print(programming_dict["Bug"])
