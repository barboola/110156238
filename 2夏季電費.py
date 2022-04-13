nu = int(input("輸入一個度數（正整數）："))

if nu <= 120 :
    s = nu*2.10
    ns = nu*2.10
    print("Summer months:" , s)
    print("Non-Summer months:" , ns)
elif nu >= 121 and nu <= 330 :
    s = ((120*2.10) + ((nu-120) *3.02))
    ns = (((120*2.10) + (nu-120)*2.68))
    print("Summer months:" , s)
    print("Non-Summer months:" , ns)
elif nu >= 331 and nu <= 500 :
    s = ((120*2.10) + (210*3.02) + ((nu-330) *4.39))
    ns = (((120*2.10) + (210*2.68) + (nu-330)*3.61))
    print("Summer months:" , s)
    print("Non-Summer months:" , ns)
elif nu >= 501 and nu <= 700 :
    s = ((120*2.10) + (210*3.02) + (170*4.39) + ((nu-500) *4.97))
    ns = (((120*2.10) + (210*2.68) + (170*3.61) + (nu-500)*4.01))
    print("Summer months:" , s)
    print("Non-Summer months:" , ns)
elif nu >= 701 :
    s = ((120*2.10) + (210*3.02) + (170*4.39) + (200*4.97) + ((nu-700) *5.63))
    ns = (((120*2.10) + (210*2.68) + (170*3.61) + (200*4.97) + (nu-700)*4.50))
    print("Summer months:" , s)
    print("Non-Summer months:" , ns)