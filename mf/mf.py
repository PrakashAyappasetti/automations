import os
import shutil

ftt = 'C:\\Users\\wikyprash\\Desktop\\mf\\a'
fd = 'C:\\Users\\wikyprash\\Desktop\\mf\\b'


os.chdir(ftt)
print(os.getcwd())

for f in os.listdir(ftt):
    if f.endswith('.txt'):
        print(f)

    a = f'{ftt}\\{f}' # file name along with directory
    # shutil.move(a, fd)
    
# pyautogui.press("f5")

extensions_folders = {
    '.txt' : r'C:\Users\wikyprash\Desktop\mf\b\txt'
}