# Same logic as imperative but using classes instead of imperative form

min = 1
max = 10


class Evens:
    def __init__(self):
        self.minimum = min
        self.maximum = max

    def __call__(self):
        for number in range(self.minimum, self.maximum + 1):
            if number % 2 == 0:
                return print(number)

def evens():
    obj = Evens()
    f = obj.__call__()
    print("Evens are:", f)
