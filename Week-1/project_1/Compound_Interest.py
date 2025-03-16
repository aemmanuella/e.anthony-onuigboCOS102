p = input("Enter Principle Amount(naira): ")
r = input("Enter the Rate(%): ")
t = input("Enter the Time(years): ")
n = input("Enter the number of times: ")

a = float(p) * (1 + (float(r)/float(n)))**(float(n) * float(t))

print("The Compound interest is ₦", a)
