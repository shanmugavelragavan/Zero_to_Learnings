# Pattern_2

# Output
# A
# A B
# A B C
# A B C D
# A B C D E

rows = 70
for i in range(65, rows):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print("")