#Jesse Codamon, Cesar Guzman, Karol Zagorski, Orlando Perez


user_text = input("Type any text: ")
user_letter1 = input("Type a letter: ")
user_letter2 = input("Type a letter: ")
user_letter3 = input("Type a letter: ")

lowercase=str.lower(user_text)
new_tuple = (tuple(lowercase))
lowercaseletters1 = str.lower(user_letter1)
lowercaseletters2 = str.lower(user_letter2)
lowercaseletters3 = str.lower(user_letter3)


letter1 = lowercase.count(lowercaseletters1)
letter2 = lowercase.count(lowercaseletters2)
letter3 = lowercase.count(lowercaseletters3)


# # Find the total number of oranges in warehouse1
# orange_quantity = product_inventory["warehouse1"]["quantities"][1]
# print(f"Total oranges in warehouse1: {orange_quantity}")  # Output: 30



#how many letters in the text
print(letter1)
print(letter2)
print(letter3)
              
#how many words total
list1 = (list(user_text))
print(len(space))

#text inverted
print(user_text[::-1])

#first and last letter
print(user_text[0:])
print(user_text[-1:])


