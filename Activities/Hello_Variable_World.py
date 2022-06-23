# Create a variable called 'name' that holds a string
Name = "Emily"

# Create a variable called 'country' that holds a string
country = "USA"

# Create a variable called 'age' that holds an integer
age = 30

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 32

# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Print out "Hello <name>!"
print("Hello " + Name + "!")

# Print out what country the user entered
print(Name + " lives in " + country)

# Print out the user's age
print(Name + " is " + str(age) + " years old")

#print out the daily wage that was calculated
print(Name + " earns " + str(daily_wage) + "  dollars per day")

# With an f-string, print out the daily wage that was calculated
print(f"Emily makes {hourly_wage * 8}  per day")
print(f"Emily makes {daily_wage}  per day")

# With an f-string, print out whether the users were satisfied
print(f"Is Emily satisfied with the wage? {satisfied}")
