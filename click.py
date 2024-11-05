import time
from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()
clicking = False

# 設定點擊間隔（秒）與點擊次數
click_interval = 0.1  # 點擊間隔，例如 0.1 秒
click_count = 10  # 連點次數

def on_press(key):
    global clicking
    if key == keyboard.Key.f8:  # 按下 F8 開始連點
        clicking = True
    elif key == keyboard.Key.f9:  # 按下 F9 停止連點
        clicking = False
    elif key == keyboard.Key.esc:  # 按下 ESC 退出程式
        return False

def click_mouse():
    for _ in range(click_count):
        if not clicking:
            break
        mouse.click(Button.left)
        time.sleep(click_interval)

def start_clicking():
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            if clicking:
                click_mouse()
            time.sleep(0.1)  # 減少 CPU 負載
        listener.join()

if __name__ == "__main__":
    print("按下 F8 開始連點，F9 停止連點，ESC 退出程式。")
    start_clicking()
