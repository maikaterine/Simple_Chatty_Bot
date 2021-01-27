initial_quantity = int(input())
final_quantity = int(input())
days = 0
while initial_quantity >= final_quantity:
    initial_quantity //= 2
    days += 12
print(days)
