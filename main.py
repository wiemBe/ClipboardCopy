import win32clipboard

win32clipboard.OpenClipboard()
clipboardData = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
win32clipboard.CloseClipboard()

print("twxt from clipboard", clipboardData.decode("utf-8"))