import sys, os

m = r'C:\MyPrgrms\flutter\flutter_master'
s = r'C:\MyPrgrms\flutter\flutter_stable'
f = str(sys.argv[1])

if f == 'm':
    os.system(f"SETX FC {m}")
elif f == 's':
    os.system(f"SETX FC {s}")
