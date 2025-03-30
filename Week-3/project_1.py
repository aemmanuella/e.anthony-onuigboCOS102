names = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna', 'Waje', 'Tola', 'Aisha', 'Latifa', 'Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola', 'Kunle', 'George', 'Thomas', 'Wesley']
age = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17, 19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
height = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5, 5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49, 74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# ':<' is used for alignment 
print(f"{'Name':<10} {'Age':<5} {'Height':<5} {'Score':<5} ")
print("=" * 30)

for i in range(len(names)):
    print(f"{names[i]:<10} {age[i]:<5} {height[i]:<5} {scores[i]:<5}")
