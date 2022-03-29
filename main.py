# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# import funcy


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [

]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
printing_practice = [
    ["Funcy (not fixed yet)", "Week 0/boatanim.py"],
    ["Tree", "Week 0/tree.py"],
    ["Square", "Week 0/square.py"],
]

math_practice = [
    ["Matrix Practice", "matrix.py"],
    ["Fibonacci", "Week 1/fibonacci.py"],
    ["Factorial", "Week 2/factorial.py"],
    ["Imperative Evens", "Week 2/imperative_evens.py"],
    ["Class Evens (doesn't work on this replit)", "Week 2/class_evens.py"],

]
other_practice = [
    ["List", "Week 1/list.py"],
    ["Palindrome", "Week 2/palindrome.py"],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Prisha's Practice Code Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Printing Practice", printing])
    menu_list.append(["Math", math])
    menu_list.append(["Other", other])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def printing():
    title = "Printing Practice Menu" + banner
    buildMenu(title, printing_practice)

def math():
    title = "Math Menu" + banner
    buildMenu(title, math_practice)

def other():
    title = "Search Menu" + banner
    buildMenu(title, other_practice)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()