n = int(input())
m = int(input())
p = int(input())
i = 0
for i in range(n-1):
    m = int((m*p)/100)
print(m)