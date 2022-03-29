#function for finding even numbers within an automated list from a minimum value to a maximum value
def findevens(min, max):
    #looks through values between minimum value and maximum value
    for number in range(min, max+1):
        #check to see if number divided by 2 has no remainder
        if (number % 2 == 0):
            #if no remainder when divided by 2, print that number, otherwise skip
            print(number)

#running function for values between 2 and 8
if __name__ == "__main__":
    findevens(2, 8)
