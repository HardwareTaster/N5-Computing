# Set total to 0
total = 0
# Loop 7 times
for index in range(12):
    # Get this months savings from user
    savings = float(input("Enter this months savings: "))
    # Add savings to total
    total = total + savings
    print(total)

# Display total rounded to 2 decimal places
print(round(total,2))
