## Key Learnings

### Tech Talk 0:
```python
def menu():
    title = "Prisha's Practice Code Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Printing Practice", printing])
    menu_list.append(["Math", math])
    menu_list.append(["Other", other])
    buildMenu(title, menu_list)
```
This week we started learning how to build menues and how to add to them. That's the main thing I learned in this Tech Talk along with some animating stuff.

### Tech Talk 1:
```python
# Program to display the Fibonacci sequence up to n-th term
def fibonacci():
    terms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0


    if terms <= 0:
        print("Please enter a positive integer")
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence for", terms, "number of terms:")
        while count < terms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
```
Learned how to use different loops to build repetitive functions.

### Tech Talk 2:
```python
class Evens:
    def __init__(self):
        self.minimum = min
        self.maximum = max

    def __call__(self):
        for number in range(self.minimum, self.maximum + 1):
            if number % 2 == 0:
                return print(number)

```
Learned how to utilize classes ✨
