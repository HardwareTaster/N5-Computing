#Anton artikov
#vehicle charging costs
PriceperMile = 0
milesTravelled = 0
totalstagecost = 0
totaljourneycost = 0
totalmiles = 0
#get journey details
startMiles = int(input("Enter your mileage at the start of the journey"))
NumberofStations = int(input("Enter the number of charging stations"))

#calculate and store the cost of each stage of the journey
for index in range(NumberofStations):
    currentMiles = int(input("enter milage at this charging station"))
    kWRating = int(input("Enter the kW rating of this charging station"))
    while not (kWRating  == 7 or  kWRating  == 22 or   kWRating  == 55):
        print("error, kW rating must be 7, 22 or 55")
        kWRating = int(input("Enter the kW rating of this charging station"))
    if kWRating == 7:
        PriceperMile = 0
    elif kWRating == 22:
        PriceperMile =0.005
    else:
        PriceperMile = 0.01
    milesTravelled = currentMiles - startMiles
    startMiles = currentMiles
    stagecost = PriceperMile*milesTravelled
    print("journey stage", index)
    totaljourneycost += stagecost
    totalmiles += milesTravelled

print ("your total journey cost is ",round(totaljourneycost,2))
print("your total miles travelled is ", totalmiles)

