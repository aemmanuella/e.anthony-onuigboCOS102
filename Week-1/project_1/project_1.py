
# Collect the input for the values
p = input("Enter Principle Amount(naira): ")
r = input("Enter the Rate(%): ")
t = input("Enter the Time(years): ")

# Create simple interest formula
a = float(p)*(1 + (float(r)/100) * float(t))
print("The Simple interest is ₦", a)
