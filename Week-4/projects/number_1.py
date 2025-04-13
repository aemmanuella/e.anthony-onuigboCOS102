def calculate_area():
    radius = float(input("Enter the radius of the circle(cm): "))
    area = 3.14 * (radius**2)
    return area

area = calculate_area()
print("The area is:", area)

