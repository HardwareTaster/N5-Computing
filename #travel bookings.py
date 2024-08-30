#travel bookings

travel_agent = []
booking_number = []
dates = []

for index in range (3):
    travelagent = input("enter travel agent")
    bookingnumber = int(input("enter booking number"))
    date = input("Enter date")
    travel_agent.append(travelagent)
    booking_number.append(bookingnumber)
    dates.append(date)

print(travel_agent)
print(booking_number)
print(dates)