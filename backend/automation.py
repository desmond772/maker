import pyautogui
import random
import time

def human_click(x, y):
    # Random curve mouse move, click, then random empty click
    pyautogui.moveTo(x + random.randint(-6,6), y + random.randint(-6,6), duration=random.uniform(0.3,1.1))
    time.sleep(random.uniform(0.4,1.3))
    pyautogui.click()
    # random click on empty space
    empty_x = random.randint(80, 400)
    empty_y = random.randint(100, 700)
    pyautogui.moveTo(empty_x, empty_y, duration=random.uniform(0.3,0.7))
    pyautogui.click()

def human_typing(text, field_location):
    pyautogui.click(field_location)
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.09,0.18))

def execute_trade(data):
    action = data.get("action")
    amount = data.get("amount", 1)
    timeframe = data.get("timeframe", "TF1")
    signal = data.get("signal", "CADUSD")
    # Simulate human-like trade execution
    trade_button_coords = (random.randint(120, 200), random.randint(300, 380))
    human_click(*trade_button_coords)
    # Typing signal
    signal_field_coords = (random.randint(250, 350), random.randint(420, 440))
    human_typing(signal, signal_field_coords)
    time.sleep(random.uniform(1.5, 2.8))
    return {
        "status": "success",
        "action": action,
        "amount": amount,
        "timeframe": timeframe,
        "signal": signal
  }
