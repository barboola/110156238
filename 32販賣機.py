from configparser import RawConfigParser
m = int(input('輸入m元:'))
n = int(input('輸入n種飲料:'))

np=[]
for i in range(n):
    np.append(int(input('請輸入第'+str(i+1)+'幾種飲料的錢:')))
c = 0
for i in range(n):
    if m >= np[i]:
        c = c + 1
print('總共可以買:',c,'杯')