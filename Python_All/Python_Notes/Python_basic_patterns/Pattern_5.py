# Pattern_5

# Output
# A
# B B
# C C C
# D D D D
# E E E E E

rows = 70
for i in range(65, rows):
    for j in range(65, i+1):
        print(chr(i), end=" ")
    print("")
