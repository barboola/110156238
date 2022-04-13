n=int(input("請輸入階層值M:"))
h=0
sum=1
while True:
    h+=1
    sum*=h
    if sum > n:
        print("超過M為%d的最小階層N值為%d" % (n,h))
        break    