# Class for making a factorial program
class Factorial:
    # Starting variables, self.start is set equal to what every factorial contains and self.n creates an n value
    def __init__(self):
        self.start = 1
        self.n = int(input("Enter a number:"))
    # Code for the factorial itself
    def __call__(self):
        b = self.n - 1
        #When n is less than 0 what happens
        if self.n < 0:
            print("Invalid input")
        # When n is equal to 0 or one, it calls self.start and returns value of 1
        elif self.n==0 or self.n==1:
            return self.start
        # When n is greater than 1, it should repeat this function until n becomes 1, didn't work yet though
        else:
            count = self.n
            one = 1
            while count > one:
                a = self.n * b
                self.n = b
                b = int(b) - 1
                count -=1
                return a

# So far, code only works for 0, 1, 2, and 3. Need to figure out how to get while loop to repeat.

#Calling the class, taking out an object and printing it.
obj = Factorial()
f = obj.__call__()
print("Factorial is:", f)