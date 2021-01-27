money = int(input())
i = 0
while money <= 700000:
    money = money + money * 0.071
    i += 1
print(i)
