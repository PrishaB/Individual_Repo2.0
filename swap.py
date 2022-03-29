print("This program orders two numbers from greatest to least...")
x = input("Please enter your first number:")
y = input("Please enter your second number:")

def swap1(x, y):
    if y > x:
        temp = x
        x = y
        y = temp
        print("Swap Result: ", x, '>', y)
    else:
        print("No Change Required: ", x, '>', y)
    return x, y

if __name__ == "__main__":
    swap1(x, y)