# Platform
The goal of the project:
The purpose of this project is to convert old and unupdated Android devices (API level 16 and above) into threads using Python. Python codes are run on devices using Chaquopy and the APK file is ready-compiled. On Android devices, Python codes are run with the Chaquopy (details: https://chaquo.com/chaquopy/) tool. If you know Kotlin or Java, you can edit the android application according to your needs.

Platfom GUI:
Connected Device Information:
It shows instantly connected android devices and creates a log in txt format. The log file is automatically saved in the same location as the executable (exe) file.

Reflesh(Reset Selected Files):
You can update connected devices with this button. It should be noted that the selected files are reset every time you refresh. Please be careful.

In the first window, you can install the APK file you want, and after the APK is installed, it will automatically check the installation. If you have installed the Platfom application on your device, you can delete it with the "Remove Analysis App from Device" button, or you can list and delete the desired applications with the "Remove Desired Apps from Device" button. If you have too many applications installed on your device, scanning time may increase, please be patient.

In the second window (if you are using the analysis application), you must select the code folder and\n the input data folder and send them. If the application is not installed on your Android device, you\n cannot select a folder and send it. The selected folders are placed in the Input folder using the\n "/sdcard/Android/data/com.example.platform_min_50(or 41)/files/Input/" path directory of the\n analysis application. Home folders are divided into two: Data and Code folders. You cannot integrate\n ready-made packages into the application (if you have installed the ready-made analysis APK file), so\n place the packages you will use in the analysis in the Code folder and use the sample hierarchical\n structure (available in the downloaded files). Please install only one analysis application according to\n the API level of the devices. If you install both analysis applications (41 and 50) on the same device, \n it will only launch Platform_min_4.1 application (prioritizing Platform_min_4.1 application). While \n the analysis is in progress, you can stop the application and analysis. After the analysis is completed, \n you can save the output data (from "/sdcard/Android/data/com.example.platform_min_50(or\n 41)/files/Output/") to the desired location on your computer. After getting the data, don't forget to\n delete the data on your android device.

Note: Platform_min_41 application supports python version 3.8 and the minimum API level is 16.\n Platform_min_50 application supports python version 3.11 and the minimum API level is 21. For\n detailed information, see the sites "https://chaquo.com/chaquopy/" and "https://apilevels.com/".

In the third window, the ADB command list (most of all commands) and their explanations are \n available. You can enter the command you want in this window. If you use commands that constantly\n wait for input, such as Logcat, you may need to terminate the ADB server (or restart the program) to\n finalize the output.

The fourth window contains general information about the connected devices. You can check the \n files you selected from this window.

While the program is running, freezes may occur due to customTkinter. Please let me know if any\n function does not work or malfunctions.
Molecular Biologist: Zafer AKAR


You can access the source codes of Platform_min_41 and Platform_min_50 applications from my profile.
