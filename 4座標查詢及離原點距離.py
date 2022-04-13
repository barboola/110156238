X=int(input("X座標:"))
Y=int(input("Y座標:"))
if X>0 and Y>0:
    print("該點位於第一象限,離原點距離為開根號%d" % (X**2+ Y**2))
elif X<0 and Y>0:
    print("該點位於第二象限,離原點距離為開根號%d" % (X**2+ Y**2))
elif X<0 and Y<0:
    print("該點位於第三象限,離原點距離為開根號%d" % (X**2+ Y**2))
elif X>0 and Y<0:
    print("該點位於第四象限,離原點距離為開根號%d" % (X**2+ Y**2))
elif X==0 and Y>0:
    print("該點位於上半平面Y軸上,離原點距離為開根號%d" % (X**2+ Y**2))
elif X==0 and Y<0:
    print("該點位於下半平面Y軸上,離原點距離為開根號%d" % (X**2+ Y**2))
elif X>0 and Y==0:
    print("該點位於右半平面X軸上,離原點距離為開根號%d" % (X**2+ Y**2))
elif X<0 and Y==0:
    print("該點位於左半平面X軸上,離原點距離為開根號%d" % (X**2+ Y**2))
elif X==0 and Y==0:
    print("該點位於原點")