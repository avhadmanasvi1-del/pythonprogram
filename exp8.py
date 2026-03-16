
n = 10
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


n = int(input("Enter number of rows: "))

for i in range(1, n + 1):          # like: for(i=1; i<=n; i++)
    for j in range(1, i + 1):      # like: for(j=1; j<=i; j++)
        print("*", end=" ")
    print()                        # new line after each row
