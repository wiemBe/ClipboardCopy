import win32clipboard
import schedule
import time 

def job():

    win32clipboard.OpenClipboard()
    clipboardData = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    win32clipboard.CloseClipboard()

    print("Text from clipboard:", clipboardData.decode("utf-8"))

schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

