# Pattern_11

# Output
	#     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *

n = 5
k = 2 * n - 2
x = 0
for i in range(0, n):
    x += 1
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("*", end=" ")
    print(" ")
    k = k + 1