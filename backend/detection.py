import pyautogui

def detect_trade_result():
    # Use image detection to check for win/loss on screen
    # Place win.png & loss.png in working directory (screenshots of platform's win/loss message for Android)
    if pyautogui.locateOnScreen('win.png', confidence=0.85):
        return 'win'
    elif pyautogui.locateOnScreen('loss.png', confidence=0.85):
        return 'loss'
    else:
        return 'unknown'
