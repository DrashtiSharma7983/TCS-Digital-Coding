r = int(input("enter the no. of row:\n"))
c = int(input("enter the no. of column:\n"))
matrix = []
print("enter no. row wise:3")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()

suml = 0
sumr = 0
for i in range(r):
    for j in range(c):
        if i==j:
            suml = suml + matrix[i][j]
        if i+j == 2:
            sumr = sumr + matrix[i][j]
print("left diagonal sum:",suml)
print("right diagonal sum:",sumr)
rslt = abs(suml) - abs(sumr)
result = abs(rslt)
print(result)
