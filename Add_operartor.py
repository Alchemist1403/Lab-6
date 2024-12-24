class Number:

    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return Number(self.value + other.value)


number1 = Number(2)
number2 = Number(3)
number3 = number1 + number2
print(number3.value)