import time
import pyautogui
import datetime
import socket

image_dir = "./Users/gerrardxcc/Documents/IT@JCU"

while True:
    curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    image_file = f"{image_dir}/image_{curr_time}.png"
    print(socket.gethostname(),"save image:",image_file)
    pyautogui.screenshot(image_file)
    time.sleep(5)