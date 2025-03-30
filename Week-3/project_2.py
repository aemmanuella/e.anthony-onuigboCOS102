experience = int(input("Enter years of experience: "))
age = int(input("Enter your age: "))

if experience > 25 and age >= 55:
    print("Your Annual Tax Revenue(ATR) is N5,600,000")
elif experience > 20 and age >= 45:
    print("Your Annual Tax Revenue(ATR) is N4,480,000")
elif experience > 10 and age >= 35:
    print("Your Annual Tax Revenue(ATR) is N1,500,000")
else:
    print("Your Annual Tax Revenue(ATR) is N550,000")