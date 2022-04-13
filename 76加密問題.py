
pwd = []
password = str(input("請輸入傳送密碼（6位數）："))
if len(password) != 6:
    password = str(input("長度不足6位數，請輸入傳送密碼（6位數）："))
else :
    for i in range(0,6):
        a = ((int(password[i]))*4)%7
        pwd.append(a)

print("解密後的密碼：",str(pwd))