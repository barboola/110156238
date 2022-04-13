b = input("輸入值:")
c = 0
a = []
for i in range(0,len(b),2):
    a.append((b[i]))

a.sort(reverse=True)
max = ""
for k in range(0,len(a)):
    max = max + a[k]

a.sort(reverse=False)
min = ""
for u in range(0,len(a)):
    min = min + a[u]

c = int(max) - int(min)
print("最大值數列與最小值數列差值為:",c)