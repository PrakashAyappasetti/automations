cd /d %~dp0

adb shell ip route > t.txt
python p.py
