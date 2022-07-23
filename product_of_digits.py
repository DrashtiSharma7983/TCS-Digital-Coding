i = int(input("enter number to find the product:"))
prod = 1
while (i>0):
    prod = prod * (i%10)
    i = i//10
print("sum of digits is:",prod)