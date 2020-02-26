import os
with open('t.txt') as f:
	a = f.readlines()
	b = a[1].split(' ')
	ip = b[-2]
print(ip)
os.system('adb tcpip 5555')
os.system(f'adb connect {ip}:5555')
