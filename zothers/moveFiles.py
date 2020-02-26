import os
import shutil
from datetime import date


def mf():
    _date = date.today()
    _day = _date.day
    _month = _date.month
    _year = _date.year
    folder_name = f'{_day}.{_month}.{_year}'

    parent_dir = 'T:\\cust'

    if os.path.exists(f"C:\\Users\\siva2\\{folder_name}\\"):
        print('folder already created')
    else:
        os.mkdir(f"{parent_dir}\\{folder_name}\\")

    src = "C:\\Users\\siva2\\Desktop\\"
    dst = f"{parent_dir}\\{folder_name}\\"

    os.chdir(src)
    ls = os.listdir()

    for i in ls:
        shutil.move(i, dst)


mf()