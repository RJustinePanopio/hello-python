import sys

x = sys.argv[1]
x=float(x)

if x >= 220.0:
    print("SuperTyphoon")
elif x >= 118.0:
    print ("Typhoon")
elif x >= 89.0:
    print ("Severe Tropical Storm")
elif x >= 62.0:
    print ("Tropical Storm")
elif x <=61.0:
    print ("Tropical Storm")