# Pattern_9

# Output
    
#      A
#     A B
#    A B C
#   A B C D
#  A B C D E

n = 5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ") 
    k = k - 1
    x = 65
    for j in range(0, i+1):
        ch = chr(x)
        print(ch, end=" ")
        x += 1
    print("\r")
k = n - 2