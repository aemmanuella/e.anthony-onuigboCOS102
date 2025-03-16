PMT = float(input("Enter the periodic payment (PMT): "))
R = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
n = int(input("Enter the number of compounding periods per year (e.g., 12 for monthly): "))
t = int(input("Enter the number of years: "))

a = PMT * ((1 + R/n) ** (n * t) - 1) / (R/n)


print("The Compound interest is ₦", a)
