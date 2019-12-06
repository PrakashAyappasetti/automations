set ip=%1
adb tcpip 5555
adb connect %ip%:5555
echo "connected succcefully"
