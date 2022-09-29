# Lists are ordered, changeable and allow duplicate values
names = ["Harry", "Daniel", "Sarah", "Keyma"]
print(names)
print(names[2])

scores = []
scores.append(80)
scores.append(91)

print(scores)

print("Amount of names stored in names list: " + str(len(names)))

names.insert(0, "Bob")
print("Bob has joined the team: " +str(names))
names.sort()
print("Sorted alphabetically: " + str(names))
print(names[0:2])
names.insert(0, "Bob")
print("We have two Bob's now: " + str(names))

# Dictionaries are comprised of key value pairs
person = {"first": "Michael"}
print(person)
print(person["first"])
person["last"] = "Ross"
print(person["last"])