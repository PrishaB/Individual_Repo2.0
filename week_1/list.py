InfoDb = []
InfoDb.append({
    "Fruit": "Apple",
    "Color": "Red",
    "Family": "Rosaceae",
    "DifferentTypes": ["Fuji", "Honeycrisp", "Granny Smith", "Red Delicious"]
})

InfoDb.append({
    "Fruit": "Orange",
    "Color": "Orange",
    "Family": "Rutaceae",
    "DifferentTypes": ["Navel", "Blood", "Mandarin", "Clementine"]
})


# Variables that take in user input and put it into the diffent loops to search for the variables
# a = input("Type key: " )
# b = input("Type value: " )

## hack 2a: def for_loop()
def for_loop():
    for x in InfoDb:
        for key, value in x.items():
            print(f"{key}: {value}")
        print()
        print("-" * 10)
        print()


## hack 2b: def while_loop(0)
def while_loop():
    x = 0
    while x < len(InfoDb):
        for key, value in InfoDb[x].items():
            print(f"{key}:{value}")
        print()
        print('-' * 10)
        print()
        x += 1


## hack 2c : def recursive_loop(0)
def recursive_loop():
    n = 0
    if n >= len(InfoDb):
        return
    else:
        for key, value in InfoDb[n].items():
            print(f"{key}:{value}")
        print()
        print("-" * 10)
        print()
        if n == 0:
            y = n + 1
            for key, value in InfoDb[y].items():
                print(f"{key}:{value}")
            print()
            print("-" * 10)
            print()
        else:
            return

    # Code for for loop search
    # def for_loop(key, value):
    #     for data in InfoDb:
    #         if(data[key]) == value:
    #             print(data[key])
    #             return
    # for_loop(a,b)
    #
    # # Code for while loop search
    # def while_loop(key, value):
    #     i = 0
    #     while i < len(InfoDb):
    #         if (InfoDb[i][key] == value):
    #             print(InfoDb[i][key])
    #             return
    #         i +=1
    # while_loop(a,b)
    #
    # # Code for recursion loop search
    # def recur_loop(i, key, value):
    #     if (i < len(InfoDb)):
    #         if (InfoDb[i][key] == value):
    #             print(InfoDb[i][key])
    #             return
    #         i += 1
    #         recur_loop(i, key, value)
    #     return
    # recur_loop(0,a,b)
