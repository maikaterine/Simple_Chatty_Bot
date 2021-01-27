# put your python code here
days = int(input())
food_cost = days * int(input())
flight_cost = 2 * int(input())
nights_cost = (days - 1) * int(input())
money = flight_cost + food_cost + nights_cost
print(money)
