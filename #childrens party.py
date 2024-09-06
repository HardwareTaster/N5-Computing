#childrens party
child_buffet = 2.00
cake = input("is cake required")
if cake == "yes"yes:
    Cakecost = 15
else:
    Cakecost = 0
adults = int(input("enter the number of adults attending"))
children = int(input("enter the number of children attending"))
for x in range(children):
    input("enter dietary requirments for each child")

if adults+children>20:
    venue = 0
else:
    venue = 0 

cost = child_buffet*children + Cakecost + venue

print("The cost for the party is £",cost)