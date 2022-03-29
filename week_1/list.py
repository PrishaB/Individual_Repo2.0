def lists():
    InfoDb = []
    # List with dictionary records placed in a list
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
    a = input("Type key: " )
    b = input("Type value: " )

    # Code for for loop search
    def for_loop(key, value):
        for data in InfoDb:
            if(data[key]) == value:
                print(data[key])
                return
    for_loop(a,b)

    # Code for while loop search
    def while_loop(key, value):
        i = 0
        while i < len(InfoDb):
            if (InfoDb[i][key] == value):
                print(InfoDb[i][key])
                return
            i +=1
    while_loop(a,b)

    # Code for recursion loop search
    def recur_loop(i, key, value):
        if (i < len(InfoDb)):
            if (InfoDb[i][key] == value):
                print(InfoDb[i][key])
                return
            i += 1
            recur_loop(i, key, value)
        return
    recur_loop(0,a,b)

if __name__ == "__main__":
    lists()