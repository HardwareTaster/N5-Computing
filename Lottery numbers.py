#lottery numbers
#18/06/24

lotterynumbers = []


for b in range(6):
    number = int(input("enter a number between 1 and 49"))
    while number < 1 or number >49:
        print ("invalid number")
        number = int(input("enter a number between 1 and 49"))
    lotterynumbers.append(number)

print ("your lottery numbers are", str(lotterynumbers).strip("[]"))

