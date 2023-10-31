import datetime
import re
import time
from tkinter import filedialog
import os
import subprocess
from CTkMessagebox import CTkMessagebox


command_list = [["adb devices	", "    Lists all connected devices"
], ["adb devices -l	"	,	"   Lists connected devices (long information)	"
], ["adb usb	"	,	"	To reboot adb device in USB mode	"
], ["adb forward –list	"	,	"	Lists all forward socket connections	"
], ["adb forward tcp:xxxx tcp:xxxx	"	,	"	Sets port forwarding(sets forwarding of computer port xxxx to Android device port xxxx)	"
], ["adb start-server	"	,	"	Starts the ADB server process	"
], ["adb kill-server	"	,	"	To kill the adb server process	"
], ["adb tcpip xxxx adb connect 192.xxx.xxx.xxadb devices	"	,	"	Connect a device using a Wi-Fi network to set the target device to listen for the TCP/IP connection on port xxxx. Verify that your host computer is also connected to the Android device via Wi-Fi.	"
], ["adb install <your_apk_name.apk>	"	,	"	To install a single application on the device.	"
], ["adb install-multiple <your_apk_name1.apk> <your_apk_name2.apk>	"	,	"	To install multiple applications on the device.	"
], ["adb install-multi-package <your_apk_name1.apk> <your_apk_name2.apk>	"	,	"	Automatically installs multiple applications on the device	"
], ["adb install -r <your_apk_name.apk>	"	,	"	It replaces the existing application while preserving its data.	"
], ["adb install -s <your_apk_name.apk>	"	,	"	Installs APK to external storage	"
], ["adb install -t <your_apk_name.apk>	"	,	"	Allows test suites	"
], ["adb uninstall <your_package_name>	"	,	"	Uninstalls APK by package name	"
], ["adb uninstall -k <your_package_name>	"	,	"	Removes apk by package name while preserving cache and app data	"
], ["adb shell pm clear <your_package_name>	"	,	"	Clears app data by package name	"
], ["adb shell pm uninstall -k –user 0 <your_package_name>	"	,	"	Uninstalls the system application by package name	"
], ["adb shell pm disable <your_package_name>	"	,	"	Disables application by package name	"
], ["adb shell pm disable-user –user 0 <your_package_name>	"	,	"	Disables the application by package name for the system user	"
], ["adb shell pm enable <your_package_name>	"	,	"	Re-enables disabled application by package name	"
], ["adb shell pm hide <your_package_name>	"	,	"	Hides the application by package name	"
], ["adb shell pm unhide <your_package_name>	"	,	"	Shows the application by package name	"
], ["adb shell pm suspend <your_package_name>	"	,	"	Suspends any application by package name	"
], ["adb shell pm unsuspend <your_package_name>	"	,	"	Reactivates suspended application by package name	"
], ["adb shell pm list packages	"	,	"	Lists the package name of all installed apks	"
], ["adb shell pm list packages -s	"	,	"	Lists the package name of all system applications	"
], ["adb shell pm list packages -3	"	,	"	Lists the package name of third-party applications installed on the device	"
], ["adb shell pm list packages -d	"	,	"	Lists the package name of disabled apps on the device	"
], ["adb shell pm list packages -e	"	,	"	Lists the package name of only active apps on the device	"
], ["adb shell pm list packages -u	"	,	"	Lists the package name of applications removed from the device	"
], ["adb reboot	"	,	"	Restarts the device	"
], ["adb reboot bootloader	"	,	"	Reboots the device in bootloader or fastboot mode	"
], ["adb reboot recovery	"	,	"	Restarts the device in recovery mode	"
], ["adb root	"	,	"	ADB reboots device with root permission	"
], ["adb unroot	"	,	"	ADB reboots device without root permission	"
], ["adb sideload ota-updatefile.zip	"	,	"	Manually installs the OTA package using recovery mode	"
], ["adb logcat	"	,	"	Displays all logcat data on the computer screen	"
], ["adb logcat -c	"	,	"	Clears existing logcat data	"
], ["adb logcat -d <path>	"	,	"	Saves current logcat data to local file	"
], ["adb bugreport <path>	"	,	"	Creates an error report of the connected device	"
], ["adb get-serialno	"	,	"	Gets the serial number of the connected device	"
], ["adb wait-for-device	"	,	"	Puts the Android device on hold until the current operation is completed	"
], ["adb get-state	"	,	"	Gets device status at the command prompt	"
], ["adb jdwp	"	,	"	Lists JDWP (Java Debug Wire Protocol) processes of the Android device	"
], ["adb backup //	"	,	"	Takes a full backup of Android device to computer	"
], ["adb restore //	"	,	"	Restores backup from computer to device	"
], ["adb backup -apk -all -f backup.ab	"	,	"	Backs up apps and settings	"
], ["adb backup -apk -shared -all -f backup.ab	"	,	"	Backs up apps, app settings, and shared storage	"
], ["adb backup -apk -nosystem -all -f backup.ab	"	,	"	Only backups third-party apps	"
], ["adb connect ip_address_of_device	"	,	"	Connects to the device using its IP address	"
], ["adb restore backup.ab	"	,	"	Restores a previously created backup	"
], ["adb pull /system/app/<your_apkname.apk>	"	,	"	Copies a file from device storage to computer	"
], ["adb push /local/path/<your_apkname.apk> /sdcard/apps/	"	,	"	Transmits a file from a computer to a device	"
], ["adb shell<enter>cp /sdcard/<oyur_filename.extension> /sdcard/foldername	"	,	"	Copy files from device storage from one folder to another	"
], ["adb shell<enter>mv /sdcard/<your_filename.extension> /sdcard/foldername	"	,	"	Moves files from one folder to another in device storage	"
], ["adb shell<enter>mv /sdcard/<your_filename.extension> /sdcard/apps/<newfilename.extension>	"	,	"	Moves the file to the device storage and renames the file in the destination folder	"
], ["adb shell	"	,	"	Starts the remote shell console	"
], ["adb shell wm density	"	,	"	Retrieves Android device's pixel density, screen resolution, refresh rate and DPI information	"
], ["adb shell wm size 1080×720	"	,	"	Changes the screen resolution of the Android device (Note: you must enter the values ​​according to the supported resolution of the device)	"
], ["adb shell wm density 450	"	,	"	Changes the pixel density of the Android device (Note: you must enter the values ​​according to the supported density of the device)	"
], ["adb shell<enter>cd /system	"	,	"	Changes directory to /system	"
], ["adb shell<enter>rm -f /sdcard/<your_apkname.apk>	"	,	"	Deletes the file from the device	"
], ["adb shell<enter>rm -d /sdcard/test	"	,	"	Deletes the folder from the device	"
], ["adb shell<enter>mkdir /sdcard/test	"	,	"	Creates folder on device	"
], ["adb shell<enter>netstat	"	,	"	Check Android device's network statistics	"
], ["adb shell<enter>ip -f inet addr show wlan0	"	,	"	Shows the WIFI IP address information of the device	"
], ["adb shell<enter>top	"	,	"	Shows all processes running on android device	"
], ["adb shell<enter>getprop ro.build.version.sdk	"	,	"	Shows properties of Android build.prop configuration	"
], ["adb shell<enter>setprop net.dns1 4.4.4.0	"	,	"	Allows setting properties of Android build.prop configuration	"
], ["adb shell dumpsys display	"	,	"	Shows on-screen information of the device regarding software and hardware configuration	"
], ["adb shell dumpsys battery	"	,	"	Shows device battery information regarding software and hardware configuration	"
], ["adb shell dumpsys batterystats	"	,	"	Shows device battery statistics regarding software and hardware configuration	"
], ["adb shell screencap /sdcard/screenshot.png	"	,	"	Takes screenshots using ADB command	"
], ["adb shell screenrecord /sdcard/movie.mp4	"	,	"	Starts screen recording using ADB command(Note: Press CTRL+C or COMMAND+C to stop screen recording)	"
], ["adb shell screenrecord –size 1080 x 2200 /sdcard/movie.mp4", "Starts screen recording by defining the output resolution using the ADB command (Note: 1. Press CTRL+C or COMMAND+C2 to stop screen recording. Resolution values must be entered according to the supported resolution of the device"
], ["adb shell screenrecord –time-limit <seconds> /sdcard/movie.mp4	"	,"Start screen recording using ADB command and set the recording duration(Note: Replace 'Seconds' with the desired value in seconds)"
], ["adb shell screenrecord –bit-rate <value> /sdcard/movie.mp4	"	,	"	Start screen recording using ADB command and adjust the bitrate of the video output file	"
], ["fastboot devices	"	,	"	Lists all fastboot devices	"
], ["fastboot oem unlock	"	,	"	Unlocks the bootloader of the connected fastboot device	"
], ["fastboot oem lock	"	,	"	Relocks the bootloader of the connected fastboot device	"
], ["fastboot reboot bootloader	"	,	"	Reboots the device from fastboot mode to fastboot or bootloader mode	"
], ["fastboot flash boot boot.img	"	,	"	Flashes the boot image using fastboot mode	"
], ["fastboot flash recovery recovery.im	"	,	"	Flash the recovery image using fastboot mode	"
], ["fastboot boot filename.img	"	,	"	Launches custom Image on device without flashing the Image file	"
], ["adb shell ls	"	,	"	Lists directory contents	"
], ["adb shell ls -s	"	,	"	Prints the size of each file in the selected directory	"
], ["adb shell ls -R	"	,	"	Recursively prints list of subdirectories	"
], ["adb get-statе	"	,	"	Prints the status of the device	"
], ["adb shell dumpsys iphonesybinfo	"	,	"	Prints the IMEI of the connected device	"
], ["adb shell netstat	"	,	"	TCP Prints connection related information such as IP and connections	"
], ["adb shell pwd	"	,	"	Prints information of the current working directory	"
], ["adb shell pm list features	"	,	"	Prints a list of phone features	"
], ["adb shell service list	"	,	"	Prints a list of all services for the device	"
], ["adb shell dumpsys activity <package>/<activity>	"	,	"	Prints application event information by package and event name	"
], ["adb shell ps	"	,	"	Prints the process status	"
], ["adb shell wm size	"	,	"	Prints current screen resolution information	"
], ["dumpsys window windows | grep -E ‘mCurrentFocus|mFocusedApp’	"	,	"	Prints the activity of the currently open application	"
], ["adb shell dumpsys package packages	"	,	"	Lists information of all opened applications	"
], ["adb shell dump <app_name>	"	,	"	Shows information for a specific app	"
], ["adb shell path <package_name>	"	,	"	Shows the path to the application by package name	"
], ["adb shell dumpsys battery set level <n>	"	,	"	Changes the device's battery level	"
], ["adb shell dumpsys battery set status<n>	"	,	"	Changes the device's battery status	"
], ["adb shell dumpsys battery reset	"	,	"	Resets the device's battery status	"
], ["adb shell dumpsys battery set usb <n>	"	,	"	Changes the USB status of the device	"
], ["adb shell input keyevent 0	"	,	"	Transmits keycode unknown/0 using ADB	"
], ["adb shell input keyevent 1	"	,	"	Transmits keycode MENU/SOFT_LEFT using ADB	"
], ["adb shell input keyevent 2	"	,	"	Transmits keycode SOFT_RIGHT using ADB	"
], ["adb shell input keyevent 3	"	,	"	Passes keycode to HOME using ADB	"
], ["adb shell input keyevent 4	"	,	"	Transmits the key code BACK using ADB	"
], ["adb shell input keyevent 5	"	,	"	CALL transmits keycode using ADB	"
], ["adb shell input keyevent 6	"	,	"	END CALL using ADB to transmit keycode	"
], ["adb shell input keyevent 7	"	,	"	Transmits keycode 0 using ADB	"
], ["adb shell input keyevent 8	"	,	"	Transmits keycode 1 using ADB	"
], ["adb shell input keyevent 9	"	,	"	Transmits keycode 2 using ADB	"
], ["adb shell input keyevent 10	"	,	"	Transmits keycode 3 using ADB	"
], ["adb shell input keyevent 11	"	,	"	Transmits keycode 4 using ADB	"
], ["adb shell input keyevent 12	"	,	"	Transmits keycode 5 using ADB	"
], ["adb shell input keyevent 13	"	,	"	Transmits keycode 6 using ADB	"
], ["adb shell input keyevent 14	"	,	"	Transmits keycode 7 using ADB	"
], ["adb shell input keyevent 15	"	,	"	Transmits keycode 8 using ADB	"
], ["adb shell input keyevent 16	"	,	"	Transmits keycode 9 using ADB	"
], ["adb shell input keyevent 17	"	,	"	Transmits keycode STAR using ADB	"
], ["adb shell input keyevent 18	"	,	"	Transmits keycode POUND using ADB	"
], ["adb shell input keyevent 19	"	,	"	Transmits keycode DPAD_UP using ADB	"
], ["adb shell input keyevent 20	"	,	"	Transmits keycode DPAD_DOWN using ADB	"
], ["adb shell input keyevent 21	"	,	"	Transmits keycode DPAD_LEFT using ADB	"
], ["adb shell input keyevent 22	"	,	"	Transmits keycode DPAD_RİGHT using ADB	"
], ["adb shell input keyevent 23	"	,	"	Transmits keycode DPAD_CENTER using ADB	"
], ["adb shell input keyevent 24	"	,	"	Transmits keycode VOLUME_UP using ADB	"
], ["adb shell input keyevent 25	"	,	"	Transmits keycode VOLUME_DOWN using ADB	"
], ["adb shell input keyevent 26	"	,	"	Transmits keycode POWER using ADB	"
], ["adb shell input keyevent 27	"	,	"	Transmits keycode CAMERA using ADB	"
], ["adb shell input keyevent 28	"	,	"	Transmits keycode CLEAR using ADB	"
], ["adb shell input keyevent 55	"	,	"	Transmits keycode COMMA using ADB	"
], ["adb shell input keyevent 56	"	,	"	Transmits keycode PERIOD using ADB	"
], ["adb shell input keyevent 57	"	,	"	Transmits keycode ALT_LEFT using ADB	"
], ["adb shell input keyevent 58	"	,	"	Transmits keycode ALT_RİGHT using ADB	"
], ["adb shell input keyevent 59	"	,	"	Transmits keycode SHIFT_LEFT using ADB	"
], ["adb shell input keyevent 60	"	,	"	Transmits keycode SHIFT_RIHGT using ADB	"
], ["adb shell input keyevent 61	"	,	"	Transmits keycode TAB using ADB	"
], ["adb shell input keyevent 62	"	,	"	Transmits keycode SPACE using ADB	"
], ["adb shell input keyevent 63	"	,	"	Transmits keycode SYM using ADB	"
], ["adb shell input keyevent 64	"	,	"	Transmits keycode EXPLORER using ADB	"
], ["adb shell input keyevent 65	"	,	"	Transmits keycode ENVELOPE using ADB	"
], ["adb shell input keyevent 66	"	,	"	Transmits keycode ENTER using ADB	"
], ["adb shell input keyevent 67	"	,	"	Transmits keycode DEL using ADB	"
], ["adb shell input keyevent 68	"	,	"	Transmits keycode GRAVE using ADB	"
], ["adb shell input keyevent 69	"	,	"	Transmits keycode MINUS using ADB	"
], ["adb shell input keyevent 70	"	,	"	Transmits keycode EQUALS using ADB	"
], ["adb shell input keyevent 71	"	,	"	Transmits keycode LEFT_BRACKET using ADB	"
], ["adb shell input keyevent 72	"	,	"	Transmits keycode RIGHT_BRACKET using ADB	"
], ["adb shell input keyevent 73	"	,	"	Transmits keycode BACKSLASH using ADB	"
], ["adb shell input keyevent 74	"	,	"	Transmits keycode SEMICOLON using ADB	"
], ["adb shell input keyevent 75	"	,	"	Transmits keycode APOSTROPHE using ADB	"
], ["adb shell input keyevent 76	"	,	"	Transmits keycode SLASH using ADB	"
], ["adb shell input keyevent 77	"	,	"	Transmits keycode AT using ADB	"
], ["adb shell input keyevent 78	"	,	"	Transmits keycode NUM using ADB	"
], ["adb shell input keyevent 79	"	,	"	Transmits keycode HEADSETHOOK using ADB	"
], ["adb shell input keyevent 80	"	,	"	Transmits keycode FOCUS using ADB	"
], ["adb shell input keyevent 81	"	,	"	Transmits keycode PLUS using ADB	"
], ["adb shell input keyevent 82	"	,	"	Transmits keycode MENU using ADB	"
], ["adb shell input keyevent 83	"	,	"	Transmits keycode NOTIFICATION using ADB	"
], ["adb shell input keyevent 84	"	,	"	Transmits keycode SEARCH using ADB	"
], ["adb shell input keyevent 85	"	,	"	Transmits keycode MEDIA_PLAY/PAUSE using ADB	"
], ["adb shell input keyevent 86	"	,	"	Transmits keycode MEDIA_STOP using ADB	"
], ["adb shell input keyevent 87	"	,	"	Transmits keycode NEXT using ADB	"
], ["adb shell input keyevent 88	"	,	"	Transmits keycode PREVIOUS using ADB	"
], ["adb shell input keyevent 89	"	,	"	Transmits keycode MEDIA_REWIND using ADB	"
], ["adb shell input keyevent 90	"	,	"	Transmits keycode MEDIA_FAST_FORWARD using ADB	"
], ["adb shell input keyevent 91	"	,	"	Transmits keycode MUTE using ADB	"
], ["adb shell input keyevent 92	"	,	"	Transmits keycode PAGE UP using ADB	"
], ["adb shell input keyevent 93	"	,	"	Transmits keycode PAGE DOWN using ADB	"
], ["adb shell input keyevent 94	"	,	"	Transmits keycode PICT SYMBOLS using ADB	"
], ["adb shell input keyevent 122	"	,	"	Transmits keycode MOVE_HOME using ADB	"
], ["adb shell input keyevent 123	"	,	"	Transmits keycode MOVE_END using ADB	"
]]
def uygulama_kontrol_et(j):
    kontrol_ana_liste = []
    uygulama_kontrol_1 = os.popen(
        'adb -s {} shell pm list packages com.example.platform_min_41'.format(j)).read()

    cikti = re.split("\n", uygulama_kontrol_1)
    cikti_liste = []  # uygulama isminin olduğu liste com.example.platform_min_41

    for uygulama41 in cikti:
        if uygulama41 == 'package:com.example.platform_min_41':
            cikti_liste.append(uygulama41)
    kontrol_ana_liste.append(cikti_liste)

    uygulama_kontrol_2 = os.popen(
        'adb -s {} shell pm list packages com.example.platform_min_50'.format(j)).read()
    cikti2 = re.split("\n", uygulama_kontrol_2)
    cikti_liste2 = []  # uygulama isminin olduğu liste com.example.platform_min_50
    for uygulama50 in cikti2:
        if uygulama50 == 'package:com.example.platform_min_50':
            cikti_liste2.append(uygulama50)
    print(cikti_liste2)
    kontrol_ana_liste.append(cikti_liste2)

    return kontrol_ana_liste


def kod_dosya_sec(j):
    uygulama_kontrol_et_degiskeni = uygulama_kontrol_et(j)
    global kod_klasoru
    try:

        if uygulama_kontrol_et_degiskeni[0] == [] and uygulama_kontrol_et_degiskeni[1] == []:
            CTkMessagebox(title="Error!!!", message="Platform App Not Installed!!!", option_1="OK", icon="cancel")
        else:
            kod_klasoru = filedialog.askdirectory(
                    title='Select Input Data Folder',
                    initialdir='/')
            if len(kod_klasoru) > 0:
                    CTkMessagebox(title="Information!!!", message="Folder Named {} was Selected".format(kod_klasoru),
                                  option_1="Tamam")
            else:
                    CTkMessagebox(title="Information!!!", message="Code Folder Not Selected", option_1="OK", icon="warning")
            return kod_klasoru
    except NameError:
        pass

def kod_dosyasi_yollama(*c):
    global listeler
    try:
        try:
            listeler = uygulama_kontrol_et(c[0])
            cikti_liste = listeler[0]
        except IndexError:
            cikti_liste = []

        try:
            listeler = uygulama_kontrol_et(c[0])
            cikti_liste2 = listeler[1]

        except IndexError:
            cikti_liste2 = []

        if c == () or c[1] == '' or c[1] == None:
            CTkMessagebox(title="Warning!!!", message="Code Folder Not Found!!!\n  (Code Folder Not Selected)", icon="warning", option_1="OK")
        else:#1. değer cihaz id numarası 2.değer seçili klasör

            if cikti_liste == ['package:com.example.platform_min_41']:

                CTkMessagebox(title="Information!!!", message="Files Are Transferring to Platform_min_4.1 Application!!!",option_1="OK")
                ters_slash_yapma = re.split("/", c[1])
                birlestirme_karakteri = str("\ ")
                boslugu_sil = re.split(" ", birlestirme_karakteri)
                tam_konum_tirnaksiz = boslugu_sil[0].join(ters_slash_yapma)
                tam_konum = ("\"{}\" ".format(tam_konum_tirnaksiz))
                a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(tam_konum) + '/sdcard/Android/data/com.example.platform_min_41/files/Input').read()

                while a.find("error") != -1 or a.find("failed") != -1:
                    a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(
                        tam_konum) + '/sdcard/Android/data/com.example.platform_min_41/files/Input').read()
                    print(a)
                CTkMessagebox(title="Information!!!",
                                  message="Selected Code Folder Sent",
                                  width=400, icon="check", option_1="OK")

            elif cikti_liste2 == ['package:com.example.platform_min_50']:

                CTkMessagebox(title="Information!!!", message="Files Are Transferring to Platform_min_5.0 Application!!!",
                                       option_1="OK")
                ters_slash_yapma = re.split("/", c[1])
                birlestirme_karakteri = str("\ ")
                boslugu_sil = re.split(" ", birlestirme_karakteri)
                tam_konum_tirnaksiz = boslugu_sil[0].join(ters_slash_yapma)
                tam_konum = ("\"{}\" ".format(tam_konum_tirnaksiz))
                a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(tam_konum) + '/sdcard/Android/data/com.example.platform_min_50/files/Input').read()
                while a.find("error") != -1 or a.find("failed") != -1:
                    a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(
                        tam_konum) + '/sdcard/Android/data/com.example.platform_min_41/files/Input').read()
                    print(a)
                CTkMessagebox(title="Information!!!",
                                      message="Selected Code Folder Sent",
                                      width=400,option_1="OK")
            else:
                CTkMessagebox(title="Error!!!",
                                      message="Selected Code Folder Failed to Send!!!\nUnknown Error!!!",
                                      width=400, icon="cancel", option_1="OK")
    except IndexError:
        pass





def veri_dosya_sec(j):
    uygulama_kontrol_et_degiskeni = uygulama_kontrol_et(j)
    global veri_klasoru
    try:

        if uygulama_kontrol_et_degiskeni[0] == [] and uygulama_kontrol_et_degiskeni[1] == []:
            CTkMessagebox(title="Error!!!", message="Platform App Not Installed!!!", option_1="OK", icon="cancel")
        else:
            veri_klasoru = filedialog.askdirectory(
                title='Select Input Data Files',
                initialdir='/')
            if len(veri_klasoru) > 0:
                CTkMessagebox(title="Information!!!", message="Folder Named {} was Selected".format(veri_klasoru),
                              option_1="OK")
            else:
                CTkMessagebox(title="Information!!!", message="Input Data Folder Not Selected", option_1="OK", icon="warning")
            return veri_klasoru
    except NameError:
        pass




def veri_dosyasi_yollama(*c):
    global listeler
    try:
        try:
            listeler = uygulama_kontrol_et(c[0])
            cikti_liste = listeler[0]
        except IndexError:
            cikti_liste = []

        try:
            listeler = uygulama_kontrol_et(c[0])
            cikti_liste2 = listeler[1]

        except IndexError:
            cikti_liste2 = []

        if c == () or c[1] == '' or c[1] == None:
            CTkMessagebox(title="Warning!!!", message="Input Data Folder Not Found!!!\n  (Input Data Folder Not Selected)", icon="cancel",
                          option_1="OK")
        else:  # 1. değer cihaz id numarası 2.değer seçili klasör

            if cikti_liste == ['package:com.example.platform_min_41']:

                CTkMessagebox(title="Warning!!!", message="Files Are Transferred to Platform_min_4.1 Application!!!",
                              option_1="OK")
                ters_slash_yapma = re.split("/", c[1])
                birlestirme_karakteri = str("\ ")
                boslugu_sil = re.split(" ", birlestirme_karakteri)
                tam_konum_tirnaksiz = boslugu_sil[0].join(ters_slash_yapma)
                tam_konum = ("\"{}\" ".format(tam_konum_tirnaksiz))
                a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(
                    tam_konum) + '/sdcard/Android/data/com.example.platform_min_41/files/Input/').read()

                while a.find("error") != -1 or a.find("failed") != -1:
                    a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(
                        tam_konum) + '/sdcard/Android/data/com.example.platform_min_41/files/Input').read()
                    print(a)

                CTkMessagebox(title="Information!!!",
                              message="Selected Input Data Folder Sent",
                              width=400, option_1="OK")

            elif cikti_liste2 == ['package:com.example.platform_min_50']:

                CTkMessagebox(title="Information!!!", message="Files Are Transferred to Platform_min_5.0 Application!!!",
                              option_1="OK")
                ters_slash_yapma = re.split("/", c[1])
                birlestirme_karakteri = str("\ ")
                boslugu_sil = re.split(" ", birlestirme_karakteri)
                tam_konum_tirnaksiz = boslugu_sil[0].join(ters_slash_yapma)
                tam_konum = ("\"{}\" ".format(tam_konum_tirnaksiz))
                a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(
                    tam_konum) + '/sdcard/Android/data/com.example.platform_min_50/files/Input/').read()

                while a.find("error") != -1 or a.find("failed") != -1:
                    a = os.popen('adb -s ' + c[0] + ' push ' + "{}".format(
                        tam_konum) + '/sdcard/Android/data/com.example.platform_min_41/files/Input').read()
                    print(a)
                CTkMessagebox(title="Information!!!",
                              message="Selected Input Data Folder Sent",
                              width=400,option_1="OK")
            else:
                CTkMessagebox(title="Error!!!",
                              message="Selected Input Data Folder Failed to Send!!!\nUnknown Error!!!!!!",
                              width=400, icon="cancel", option_1="OK")
    except IndexError:
        print("hata")


#otomatik olarak program konumuna txt dosyası oluşturur paketledikten sonra hata verebilir kontrol et
def dokumantasyon(b, c):
    d = str(c)
    e = str(b)
    h = "Devices List: "+e+"   Date and Time:   "+d
    with open("Log.txt", "a") as f:
        f.write("{}\n \n".format(h))


def baglicihazlar_adb():

    x = datetime.datetime.now()
    a = os.popen('adb devices').read()
    ters_slash_n_ve_t_sil = re.split("\n|\tdevice|List of devices attached\n", a)
    kumeye_cevir = set(ters_slash_n_ve_t_sil)
    kumeye_cevir.remove('')
    bagli_cihaz_listesi = list(kumeye_cevir)
    #bagli_cihaz_listesi.append(x)
    #print(bagli_cihaz_listesi, x, "Bağlı Cihaz Sayısı:", len(bagli_cihaz_listesi))

    dokumantasyon(bagli_cihaz_listesi, x)

    return bagli_cihaz_listesi, x

from time import sleep

def analiz_baslatma(j):#j = cihaz id
    global baslatilan_uygulama
    try:
        print(j)
        os.popen("adb -s {} logcat -c".format(j))


        uygulama_kontrol_1 = os.popen('adb -s {} shell pm list packages com.example.platform_min_41'.format(j)).read()
        uygulama_kontrol_2 = os.popen('adb -s {} shell pm list packages com.example.platform_min_50'.format(j)).read()

        eklenti_olmadan41 = uygulama_kontrol_1[8:]

        eklenti_olmadan50 = uygulama_kontrol_2[8:]

        if eklenti_olmadan41 == "com.example.platform_min_41\n":
            #os.popen("adb -s {} shell am force-stop com.example.platform_min_41".format(j))
            baslatilan_uygulama = "com.example.platform_min_41"

        elif eklenti_olmadan50 == "com.example.platform_min_50\n":
            #os.popen("adb -s {} shell am force-stop com.example.platform_min_50".format(j))
            baslatilan_uygulama = "com.example.platform_min_50"

        else:
            pass
        #os.popen("adb -s {} shell am force-stop ".format(j) + baslatilan_uygulama)
        #os.popen("adb -s {} logcat -c".format(j))
        os.popen("adb -s {} shell am start -n ".format(j) + baslatilan_uygulama +"/.MainActivity")
        time.sleep(3)
        os.popen("adb -s {} shell am start -n ".format(j) + baslatilan_uygulama +"/.is_parcacigi_baslatma")

        def logcat_calistir(cmd_girdi):
            p = subprocess.Popen(cmd_girdi,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            return iter(p.stdout.readline, b'')

        cmd_girdi = ('adb -s {} logcat -s zafer'.format(j)).split()
        for satir in logcat_calistir(cmd_girdi):
            satir2 = str(satir)
            cikis2 = satir2.find("python_analizi_baslatildi")
            cikis = satir2.find("python_islemi_bitti")

            if cikis2 == -1:
                pass
            else:
                CTkMessagebox(title="Information!!!",
                              message="Analysis Started on Device {}".format(j), option_1="OK")

            if cikis == -1:
                pass
            else:
                CTkMessagebox(title="Information!!!",
                              message="Analysis finished on device {}".format(j), option_1="OK")
                os.popen("adb -s {} shell am force-stop ".format(j) + baslatilan_uygulama)
                break
    except NameError:
        CTkMessagebox(title="Error!!!", message="No Analysis Application Found Installed on Device {}".format(j),
                      option_1="OK",
                      icon="cancel")

def analiz_durdur(j):
    global baslatilan_uygulama
    baslatilan_uygulama = None
    uygulama_kontrol_1 = os.popen('adb -s {} shell pm list packages com.example.platform_min_41'.format(j)).read()
    uygulama_kontrol_2 = os.popen('adb -s {} shell pm list packages com.example.platform_min_50'.format(j)).read()
    eklenti_olmadan41 = uygulama_kontrol_1[8:]

    eklenti_olmadan50 = uygulama_kontrol_2[8:]

    if eklenti_olmadan41 == "com.example.platform_min_41\n":
        baslatilan_uygulama = "com.example.platform_min_41"
    elif eklenti_olmadan50 == "com.example.platform_min_50\n":
        #os.popen("adb -s {} shell am force-stop com.example.platform_min_50".format(j))
        baslatilan_uygulama = "com.example.platform_min_50"
    else:
        pass
    try:
        os.popen("adb -s {} shell am force-stop ".format(j) + baslatilan_uygulama),
        CTkMessagebox(title="Information!!!", message="Analysis Stopping on Device {}!!!".format(j),
                      option_1="OK")
    except TypeError:
        CTkMessagebox(title="Error!!!", message="No Analysis Application Found Installed on Device {}".format(j),
                      option_1="OK",
                      icon="cancel")










def abd_bagli_cihaz_android_surum_durumu():
    surum=[]
    cihaz_listesi=baglicihazlar_adb()
    cihaz_listesi2 = cihaz_listesi[0]

    for cihaz_surum in range(len(cihaz_listesi2)):
        c = cihaz_listesi[0][cihaz_surum]#sıfırıncı index bağlı cihaz listesi birinci index saat ve tarihtir
        b = 'adb -s '
        d = ' shell getprop ro.build.version.release'
        e = b+c+d
        a = os.popen(e).read()
        ters_slash_n_ve_t_sil = re.split("\n", a)
        #print(ters_slash_n_ve_t_sil)
        f = ters_slash_n_ve_t_sil[0]
        surum.append(f)
    return surum

abd_bagli_cihaz_android_surum_durumu()
baglicihazlar_adb()


def surum_ve_cihaz_id():
    listezort=[]
    y = abd_bagli_cihaz_android_surum_durumu()
    z = baglicihazlar_adb()
    z2 = z[0]

    for zort in range(len(z2)):

        son = ("{} --- {}".format(y[zort], z2[zort]))
        listezort.append(son)

    return listezort#bağlı cihazların listesi(sürüm ve id birleşik)
print(len(surum_ve_cihaz_id()))




#matris oluşturmak için kullan
ana_liste = []
for cihaz_sayisi in range(len(surum_ve_cihaz_id())):
    ic_liste = []
    ana_liste.append(ic_liste)

print(ana_liste)








def apk_sec():
    try:
        apk_dosyasi_liste = []
        dosya_tipi = (
            ('.apk', '*.apk'),

        )
        apk_dosyasi = filedialog.askopenfilename(
            title='Select Apk File',
            initialdir='/',
            filetypes=dosya_tipi
            )

        if len(apk_dosyasi) > 0:
            CTkMessagebox(title="Information!!!", message="APK File Named {} was Selected".format(apk_dosyasi), option_1="OK")



        else:
            CTkMessagebox(title="Information!!!", message="APK File Not Selected", option_1="OK", icon="warning")



        apk_dosyasi_liste.append(apk_dosyasi)
        print(apk_dosyasi_liste)
        return apk_dosyasi
    except AttributeError:
        CTkMessagebox(title="Information!!!", message="APK File Not Selected", option_1="OK", icon="warning")




def klasor_olusturma(j):#j cihaz id numarası, id numarası ile output klasörüne yönlendir
    global uygulama
    try:
        x = datetime.datetime.now()
        zaman_yazi = str(x)
        iki_nokta_sil = re.split("[: ]", zaman_yazi)
        belirtec = '_'.join(iki_nokta_sil)

        # anlık zaman
        kaynak_uzanti = filedialog.askdirectory(title='Select Folder Path:')


        path = os.path.join(kaynak_uzanti + "/" + 'Platform_{}_{}'.format(j, belirtec))
        os.makedirs(path)
        print(path)

        if path[:9] == "/Platform":
            CTkMessagebox(title="Information!!!", message="Folder Not Selected!!!", option_1="OK", icon="warning")
        else:
            time.sleep(2)
            ters_slash_yapma = re.split("/", path)
            bosluk = ''
            if bosluk in ters_slash_yapma:
                ters_slash_yapma.remove('')
            else:
                pass
            #print(ters_slash_yapma)
            birlestirme_karakteri = str("\ ")
            boslugu_sil = re.split(" ", birlestirme_karakteri)
            #print(boslugu_sil[0])
            tam_konum_tirnaksiz = boslugu_sil[0].join(ters_slash_yapma)
            tam_konum_tirnaksiz2 = "{}".format(tam_konum_tirnaksiz)
            tam_konum = ("\"{}\"".format(tam_konum_tirnaksiz2))

            uygulama_surum_kontrol = uygulama_kontrol_et(j)#[[],[]]
            if uygulama_surum_kontrol[0] == ["package:com.example.platform_min_41"]:
                uygulama = "com.example.platform_min_41"
            elif uygulama_surum_kontrol[1] == ["package:com.example.platform_min_50"]:
                uygulama = "com.example.platform_min_50"
            else:
                pass

            klasor_cek = os.popen("adb -s {} pull -a /storage/emulated/0/Android/data/".format(j) + uygulama + "/files/Output {} ".format(tam_konum)).read()
            print(klasor_cek)
    except NameError:
        CTkMessagebox(title="Error!!!", message="Platform App Not Installed!!!", option_1="OK", icon="cancel")



#install in sonuna r ekledim sıkıntı çıkarsa çöz
def apk_kurma(*c):
    try:
        cihaz_id = str(c[0])
        konum = c[1]
        print(cihaz_id)
        ters_slash_yapma = re.split("/", konum)
        print(ters_slash_yapma)
        konum_uzunluk = len(ters_slash_yapma)-1
        apk_ismi = ters_slash_yapma[konum_uzunluk]
        birlestirme_karakteri = str("\ ")
        boslugu_sil = re.split(" ", birlestirme_karakteri)
        tam_konum_tirnaksiz = boslugu_sil[0].join(ters_slash_yapma)
        tam_konum = ("\"{}\"".format(tam_konum_tirnaksiz))

        adb_shell = os.popen('adb -s '+cihaz_id+' install -r {}'.format(tam_konum)).read()
        print(adb_shell)

        #uygulama_listesi_uygulama_yuklendikten_sonra = os.popen('adb -s ' + cihaz_id + ' shell pm list packages').read()

        #ters_slash_n_sil_2 = re.split("\n", uygulama_listesi_uygulama_yuklendikten_sonra)
        #print(ters_slash_n_sil_2)
        #print(len(ters_slash_n_sil_2))
        try:
            os.popen('adb -s ' + cihaz_id + ' shell am start -n com.example.platform_min_41/.MainActivity').read()
            os.popen('adb -s ' + cihaz_id + ' shell am start -n com.example.platform_min_50/.MainActivity').read()

        except None:
            pass

        #apk kurulumunun sağlanması
        n_sil = re.split("\n", adb_shell)
        kurulum_belirtme = []
        a = 0
        for kelime in n_sil:
            if kelime == 'Success':

                kurulum_belirtme.append(kelime)

            else:
                pass
            a = a + 1

        if kurulum_belirtme[0] == "Success":
            print("APK Installation Successful")
            CTkMessagebox(title="Information!!!",
                          message="The Installation of The APK Named \"{}\" On The Device With Serial Number \"{}\" Was Successful.".format(apk_ismi, cihaz_id),
                           width=400, icon="check", option_1="OK")


        else:

            CTkMessagebox(title="Error!!!",
                          message="Installation Of Package Named \"{}\" On Device With Serial Number \"{}\" Failed.\"(APK File Not Selected or Incompatible API Level)!!!".format(
                              cihaz_id, apk_ismi), icon="cancel", width=460, option_1="OK")



    except IndexError:
        CTkMessagebox(title="Warning!!!",
                      message="APK File Not Found!!!\n  (APK File Not Selected)",
                      icon="warning", width=460, option_1="OK")


def kod_sil(j):
    uygulama_kontrol = uygulama_kontrol_et(j)#sıfırıncı index 41 uygulaması birinci index 50 uygulaması [[41],[50]]
    print(uygulama_kontrol)
    if uygulama_kontrol[0] == ["package:com.example.platform_min_41"]:
        CTkMessagebox(title="Information!!!", message="Analysis Code Folder in Platform_min_4.1 Application is Deleting!!!", option_1="OK")
        os.popen("adb -s {} shell rm -r /storage/emulated/0/Android/data/com.example.platform_min_41/files/Input/Code".format(j))

    elif uygulama_kontrol[1] == ["package:com.example.platform_min_50"]:
        CTkMessagebox(title="Information!!!", message="Analysis Code Folder in Platform_min_5.0 Application is Deleting!!!", option_1="OK")
        os.popen("adb -s {} shell rm -r /storage/emulated/0/Android/data/com.example.platform_min_50/files/Input/Code".format(j)).read()
    else:
        CTkMessagebox(title="Error!!!", message="Platform App Not Installed!!!", option_1="OK", icon="cancel")

def veri_sil(j):
    uygulama_kontrol = uygulama_kontrol_et(j)  # sıfırıncı index 41 uygulaması birinci index 50 uygulaması [[41],[50]]
    print(uygulama_kontrol)
    if uygulama_kontrol[0] == ["package:com.example.platform_min_41"]:
        CTkMessagebox(title="Information!!!", message="Analysis Input Data Folder in Platform_min_4.1 Application is Deleting!!!",
                      option_1="OK")
        os.popen(
            "adb -s {} shell rm -r /storage/emulated/0/Android/data/com.example.platform_min_41/files/Input/Data".format(
                j))

    elif uygulama_kontrol[1] == ["package:com.example.platform_min_50"]:
        CTkMessagebox(title="Information!!!", message="Analysis Input Data Folder in Platform_min_5.0 Application is Deleting!!!",
                      option_1="OK")
        os.popen(
            "adb -s {} shell rm -r /storage/emulated/0/Android/data/com.example.platform_min_50/files/Input/Data".format(
                j)).read()
    else:
        CTkMessagebox(title="Error!!!", message="Platform App Not Installed!!!", option_1="OK", icon="cancel")


def cihaz_yuklu_uygulamalar(c):
    cihaz_id = str(c)
    uygulama_listesi = os.popen('adb -s ' + cihaz_id + ' shell pm list packages').read()
    print(uygulama_listesi)
    uygulama_listesi_parcali = re.split("\n", uygulama_listesi)
    kumeye_cevir_uygulama_listesi = set(uygulama_listesi_parcali)
    kumeye_cevir_uygulama_listesi.remove('')
    arindirilmis_uygulama_listesi = list(kumeye_cevir_uygulama_listesi)
    print(arindirilmis_uygulama_listesi)  # yüklü uygulamaların listesi
    print(len(arindirilmis_uygulama_listesi))
    return arindirilmis_uygulama_listesi


def uygulama_silme(uygulama, j):
    uygulama_ismi_eklenti_olamadan = uygulama[8:]
    uygulama_sil = os.popen('adb -s ' + j + ' uninstall ' + uygulama_ismi_eklenti_olamadan).read()
    print(uygulama_sil)

    if uygulama_sil == ("Success\n"):
        print("başarılı")
        CTkMessagebox(title="Information!!!",
                      message="Package Named {} Removed from Device Serial Number {}!!!".format(uygulama, j), width=400, icon="check", option_1="OK")


    else:
        print("Uygulama kaldırılamadı")
        CTkMessagebox(title="Error!!!",
                      message="Package Named {} Couldn't Be Found Or Removed From Device Serial Number {}!!!".format(uygulama, j), width=400,
                      icon="cancel", option_1="OK")



def analiz_uygulama_silme(j):
    print(j)

    try:
        uygulama_sil = os.popen('adb -s ' + j + ' uninstall com.example.platform_min_41').read()

        print(uygulama_sil)
        n_sil = re.split("\n", uygulama_sil)
        silme_belirtme = []
        a = 0
        for kelime in n_sil:
            if kelime == 'Success':

                silme_belirtme.append(kelime)

            else:
                pass
            a = a + 1

        if silme_belirtme[0] == "Success":
                CTkMessagebox(title="Information!!!",
                              message="Platform_min_4.1 App Removed from Device",
                              width=400, option_1="OK")


    except IndexError:
        CTkMessagebox(title="Error!!!",
                      message="Platform_min_4.1 Application Not Found on the Device",
                      width=400,
                      icon="cancel", option_1="OK")
    #cihaz id numarası = j

    try:
        uygulama_sil2 = os.popen('adb -s ' + j + ' uninstall com.example.platform_min_50').read()
        print(uygulama_sil2)
        n_sil = re.split("\n", uygulama_sil2)
        silme_belirtme2 = []
        a = 0
        for kelime in n_sil:
            if kelime == 'Success':

                silme_belirtme2.append(kelime)

            else:
                pass
            a = a + 1

        if silme_belirtme2[0] == "Success":
            CTkMessagebox(title="Information!!!",
                          message="Platform_min_4.1 App Removed from Device",
                          width=400, option_1="OK")


    except IndexError:
        CTkMessagebox(title="Error!!!",
                      message="Platform_min_5.0 Application Not Found on the Device",
                      width=400,
                      icon="cancel", option_1="OK")



    #uygulama_sil = os.popen('adb -s ' + cihaz_id_eklenti_olamadan + ' uninstall paket ismi').read()
    #apk dosyalarının paket isimlerini sırası ile sil hata adb içerisinde olacak programı etkilemez
    #uyarı mesajı ekle
    #try except ile yaz hata vericek çünkü



def cihaz_bilgileri(j):
    try:
        cihaz_sdk_seviyesi = os.popen('adb -s ' + j + ' shell getprop ro.build.version.sdk ').read()

        cihaz_sdk_seviyesi_tam_sayi = int(cihaz_sdk_seviyesi)

        if 15 < cihaz_sdk_seviyesi_tam_sayi < 24:
        #cihaz harici depolama alan bilgileri
            uygulama_harici_depolama = os.popen('adb -s ' + j + ' shell df sdcard ').read()

            ters_slash_n_sil = re.split("\n", uygulama_harici_depolama)
            ters_slash_n_sil.remove('')
            ters_slash_n_sil.remove('')
            ters_slash_n_sil.remove('')

            sadece_depolama_bilgisi = ("Total Storage / Storage Used / Empty Storage / Block Limit : {}".format(ters_slash_n_sil[1][20:]))


        else:
            uygulama_harici_depolama = os.popen('adb -s ' + j + ' shell df sdcard -h ').read()

            ters_slash_n_sil = re.split("\n", uygulama_harici_depolama)
            ters_slash_n_sil.remove('')
            son_durum = ters_slash_n_sil[-1][:-17]
            # print(son_durum[9:])
            sadece_depolama_bilgisi = ("Block Limit / Storage Used / Empty Storage / Usage Percentage (%): {}".format(son_durum[11:]))

        #cihaz ram bilgileri:
        uygulama_ram_miktari = os.popen('adb -s ' + j + ' shell "cat /proc/meminfo"').read()
        ters_slash_n_sil2 = re.split("\n", uygulama_ram_miktari)
        #print(ters_slash_n_sil2)

        toplam_ram_miktari = ("Total RAM: {}".format(ters_slash_n_sil2[0][9:]))#toplam ram miktarı kb cinsinden

        if 15 < cihaz_sdk_seviyesi_tam_sayi < 24:
            kullanilabilir_ram_miktari = ("Available RAM Space:{}".format(ters_slash_n_sil2[2][8:]))#kullanılabilir ram miktarı

        else:
            kullanilabilir_ram_miktari = ("Available RAM Space:{}".format(ters_slash_n_sil2[1][8:]))  # kullanılabilir ram miktarı

        #cihaz işlemci bilgisi
        islemci_bilgisi = os.popen('adb -s ' + j + ' shell getprop ro.product.cpu.abi').read()

        ters_slash_n_sil3 = re.split("\n", islemci_bilgisi)
        islemci_bilgisi_2 = ("Device Processor Information:          {}".format(ters_slash_n_sil3[0]))





        cihaz_bilgileri_tek_parca = ("---{}  ---\n---   {}  ---\n---    {}  ---\n---    {}  ---".format(sadece_depolama_bilgisi, toplam_ram_miktari, kullanilabilir_ram_miktari, islemci_bilgisi_2))
    except ValueError:
        cihaz_bilgileri_tek_parca = ""


    return cihaz_bilgileri_tek_parca
