person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print()

print(person['children'])
print()

print(person['children'][1])
print()

print(person['pets']['cat'])
print()

#names of all children
for child in person['children']:
    print(child)
print()


# #print names of dog and cat
for p in person['pets']:
    print(person['pets'][p])
