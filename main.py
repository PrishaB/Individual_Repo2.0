# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# import funcy
from week_0.boatanim import ship
from week_0.tree import holidaybush
from week_0.square import square

from week_1.fibonacci import fibonacci
from matrix import print_matrix
from week_2.imperative_evens import findevens
from week_2.class_evens import Evens
from week_2.factorial import print_factorial

from week_1.list import for_loop
from week_1.list import while_loop
from week_1.list import recursive_loop
from week_2.palindrome import driver
# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()


# Submenu list of [Prompt, Action]
# Works similarly to main_menu
def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed

def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu


printing_practice = {
    1: {"display":"Funcy",
        "exec":ship,
        "type":"func"},
    2: {"display":"Tree",
        "exec":holidaybush,
        "type":"func"},
    3: {"display":"Square",
        "exec":square,
        "type":"func"}
}


math_practice = {
    1: {"display":"Matrix Practice",
        "exec":print_matrix,
        "type":"func"},
    2: {"display":"Fibonacci",
        "exec":fibonacci,
        "type":"func"},
    3: {"display":"Factorial",
        "exec":print_factorial,
        "type":"func"},
    4: {"display":"Imperative Evens",
        "exec":findevens,
        "type":"func"},
    5: {"display":"Class Evens",
        "exec":Evens,
        "type":"func"}
}


lists = {
    1: {"display":"For",
        "exec":for_loop,
        "type":"func"},
    2: {"display":"While",
        "exec":while_loop,
        "type":"func"},
    3: {"display":"Recursive",
        "exec":recursive_loop(),
        "type":"func"}
}


other_practice = {
    1: {"display":"List",
        "exec":lists,
        "type":"dict"},
    2: {"display":"Palindrome",
        "exec":driver,
        "type":"func"}
}

main_menu = {
    1: {"display":"Printing Practice",
        "exec":printing_practice,
        "type":"dict"},
    2: {"display":"Math",
        "exec":math_practice,
        "type":"dict"},
    3: {"display":"Other",
        "exec":other_practice,
        "type":"dict"},
    4: {"display":"Quit Program",
        "exec":quit,
        "type":"func"}
}


if __name__ == "__main__":
    while True: #forever loop
        presentMenu(main_menu)
