# put your python code here
classroom1 = int(input())
classroom2 = int(input())
classroom3 = int(input())
desks1 = classroom1 // 2 + classroom1 % 2
desks2 = classroom2 // 2 + classroom2 % 2
desks3 = classroom3 // 2 + classroom3 % 2
desks = desks1 + desks2 + desks3
print(desks)
