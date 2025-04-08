# Pattern_10

# Output
#     E
#    D E
#   C D E
#  B C D E
# A B C D E


alp = 65
r = 5
for i in range(r, 0, -1):
    for j in range(1, i):
        print(end=" ")
    for k in range(i, 6):
        print(chr(alp+k-1), end=" ")
    print(" ")