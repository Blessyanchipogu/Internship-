import random
def passwordGenerator():
    length =int(input("enter the length of a password:"))
    characters=["a","b","c","d","!","@","#","$","%","^","&","*",1,2,3,4,5]
    output=""
    for key in range(length):
        output +=str(random.choice(characters))
        
    return output
print(passwordGenerator())
