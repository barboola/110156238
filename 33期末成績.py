c = int(input('國文:'))
e = int(input('英文:'))
pe = int(input('體育:'))
m = int(input('微積分:'))
py = int(input('程式設計:'))

sum = {c:'國文',e:'英文',m:'微積分',pe:'體育',py:'程式設計'}
sum1 = 0
for score in sum:
    sum1 = sum1 + score
print('平均成績:%.2f'%(sum1/len(sum)))
x=list(sum.keys())
y=[]
for i in x:
    y.append(int(i))
y.sort()
ma=sum.get(y[0])

print('最高分數:',sum.get(y[4]),y[4])
print('最低分數:',sum.get(y[0]),y[0])
