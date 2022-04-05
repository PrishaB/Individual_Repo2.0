# Same logic as imperative but using classes instead of imperative form

mini = int(input("Lower bound: "))
maxi = int(input("Upper bound: "))


class Evens:
    def __init__(self):
        self.minimum = mini
        self.maximum = maxi

    def __call__(self):
        for number in range(self.minimum, self.maximum + 1):
            if number % 2 == 0:
                return print(number)


if __name__ == "__main__":
    Evens()
