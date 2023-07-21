n = int(input("Enter the number (n) to generate the multiplication table: "))        
# Multiplication Table
print("Multiplication Table:\n")

print("    ", end="")

#Print Top Row
for i in range(1, n + 1):
    print(f"{i:3} ", end="")
print() 

#Your Code Starts Here
for i in range(1, n + 1):
    print(f"{i:3} ", end="")
    for j in range(1, n + 1):
        result = i * j
        print(f"{result:3} ", end="")
    print()