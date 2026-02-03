# Taking input from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying result
print("Simple Interest =", simple_interest)
