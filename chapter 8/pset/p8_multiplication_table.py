from typing import Match, MutableMapping


num = int(input("Enter a number: "))

def multiplicationTable(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

multiplicationTable(num)