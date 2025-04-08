# Pattern_7

# Output
#         1
#        1 2
#       1 2 3
#      1 2 3 4
#     1 2 3 4 5

n = 5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    x = 1
    for j in range(0, i+1):
        print(x, end=" ")
        x += 1
    print("\r")
k = n - 2