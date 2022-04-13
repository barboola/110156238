n = int(input("整數n："))
a = n
line = []


while (n != 1):
    if n%2 == 0 :
        n = round(n/2)
        line.append(n)
    else :
        n = round(3*n+1)
        line.append(n)
print(a)
for i in line:
    print(i , end=" ")