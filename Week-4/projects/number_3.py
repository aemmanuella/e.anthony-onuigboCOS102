number = int(input("Enter the positive integer: "))
def find_factors():
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

factors = find_factors()
print(f"The factors of {number} are: ", factors)