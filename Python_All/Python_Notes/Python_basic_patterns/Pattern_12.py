# Pattern_12

# Output
#         1
#        2 2
#       3 3 3
#      4 4 4 4
#     5 5 5 5 5


n = 5
k = 2 * n - 2
x = 0
for i in range(0, n):
    x += 1
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print(x, end=" ")
    print(" ")
k = n - 2