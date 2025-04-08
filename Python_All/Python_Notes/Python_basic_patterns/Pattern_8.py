# Pattern_8

# Output
#     5
#    4 5
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5


r = 5
for i in range(r, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    for k in range(i, r+1):
        print(k, end=" ")
    print(" ")