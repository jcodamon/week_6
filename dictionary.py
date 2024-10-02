# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Dehli",
            "China": "Bejing",
            "Russia":"Moscow"}
#print(dir(capitals))
#gives the attributes of the methods of the dictionary
#print(help(capitals))
#gives you the documentation of each of the methods
#print(capitals.get("USA"))
#print(capitals.get("India"))
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"})
#This is how you update things
#print(capitals)

capitals.update({"Mexico": "Mexico City"})

#print(capitals)

#print(capitals.get("Mexico"))

capitals.update({"USA": "Detroit"})

capitals.pop("China")
#Removes item from dictionary
capitals.popitem()

print(capitals)
capitals.clear()
#clears the dictionary

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

items = capitals.items()
for key in capitals.items():
    print(f"{key}: {value}")