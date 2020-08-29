names = []
#define an empty list called names

# loop through the list for 5 times and for each input save to the list above
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)


#for each name in names, covert all the characters to lower case
lowercased = [name.lower() for name in names]

#for each name in names, covert the first character to upper case
titlecased = [name.title() for name in lowercased]

print(titlecased)


invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)







