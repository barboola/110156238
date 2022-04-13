a = int(input("請輸入月租費形式："))
b = int(input("請輸入通話時間："))
if a == 186 :
    c = round(b*0.09)
    if c<=186 :
        print("通話費為：186")
    else :
        if c <= (186*2):
            c = round(c*0.9)
            print("通話費為：" , c)
        elif c > (186*2):
            c = round(c*0.8)
            print("通話費為：" , c)
elif a == 386 :
    c = round(b*0.08)
    if c<=186 :
        print("通話費為：386")
    else :
        if c <= (386*2):
            c = round(c*0.8)
            print("通話費為：" , c)
        elif c > (386*2):
            c = round(c*0.7)
            print("通話費為：" , c)
elif a == 586 :
    c = round(b*0.07)
    if c<=186 :
        print("通話費為：586")
    else :
        if c <= (586*2):
            c = round(c*0.7)
            print("通話費為：" , c)
        elif c > (586*2):
            c = round(c*0.6)
            print("通話費為：" , c)
elif a == 986 :
    c = round(b*0.06)
    if c<=986 :
        print("通話費為：986")
    else :
        if c <= (986*2):
            c = round(c*0.6)
            print("通話費為：" , c)
        elif c > (986*2):
            c = round(c*0.5)
            print("通話費為：" , c)