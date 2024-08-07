from plyer import notification
import win32com.client
import time

def reminder():
    a=win32com.client.Dispatch("SAPI.spVoice")
    notification.notify(title = "REMINDER", message=a.speak("Water Time"), timeout = 1)

while True:
    reminder()
    time.sleep(10)
    quit()