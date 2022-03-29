matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

# print each sublist in new row
# for row in matrix:
#   print (row, sep=',')
# a = matrix[0
# print(a)

a = matrix[0][0], matrix[0][1], matrix[0][2]
b = matrix[1][0], matrix[1][1], matrix[1][2]
c = matrix[2][0], matrix[2][1], matrix[2][2]
print(*a, sep=" ")
print(*b, sep=" ")
print(*c, sep=" ")


def print_matrix():
    for i in matrix:
        print(str(i).replace('[', '').replace('[', '').replace(']', ''))
