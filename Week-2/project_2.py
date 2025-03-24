def solve_quadratic(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + (discriminant ** 0.5)) / (2 * a)
        root2 = (-b - (discriminant ** 0.5)) / (2 * a)
        roots = (root1, root2)
    else:
        real_part = -b / (2 * a)
        imag_part = (abs(discriminant) ** 0.5) / (2 * a)
        roots = (real_part + imag_part * 1j, real_part - imag_part * 1j)
    print("Roots:", roots)

def solve_cubic(a, b, c, d):
    x = "x"
    equation = [a, b, c, d]
    print("Roots:", equation)

def solve_quartic(a, b, c, d, e):
    x = "x"
    equation = [a, b, c, d, e]
    print("Roots:", equation)

def main():
    print("Choose the type of equation to solve:")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        solve_quadratic(a, b, c)
    elif choice == "2":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        solve_cubic(a, b, c, d)
    elif choice == "3":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        e = float(input("Enter coefficient E: "))
        solve_quartic(a, b, c, d, e)
    else:
        print("Invalid choice.")

main()
