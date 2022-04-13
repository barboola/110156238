n = int(input('輸入一個正整數:'))
if n >= 11 & n <= 100 :
    if n % 2 == 0 and n % 11 == 0 and n % 5 != 0 and n % 7 !=0:
        print('yes')
    else:
        print('no')
else:
    print('輸入數字錯誤')