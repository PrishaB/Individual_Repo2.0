def holidaybush(n):
    int(input("How tall do you want your tree to be?"))
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x+=2
        z-=1
    print('    ***    ')
    print('    ***    ')