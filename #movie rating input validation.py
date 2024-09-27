#movie rating input validation
#anton
print("MOVIE RATINGS")
print("Please select an option from the menu")
print(" 1.Add movie")
print(" 2.view movie list")
print(" 3.search movies")
print(" 4.exit")
menuselect = int(input("input a number to select an option"))
while menuselect  <1 or menuselect>4:
    print("ERROR, please select a number between 1 and 4")
    menuselect = int(input("input a number to select an option"))
    