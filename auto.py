import pyautogui as auto
import time 


print("start")
print(f"screen size: {auto.size()}")
print(auto.position())

auto.press('f3')
auto.moveTo(1406, 68, duration=2)
auto.click()

time.sleep(0.5)

auto.press('esc')

time.sleep(0.5)
auto.keyDown('ctrl')
auto.press('right')
auto.keyUp('ctrl')

time.sleep(0.5)


#print(f"mouse pos: {auto.position()}") # 1375 270
auto.moveTo(1375, 270, duration=2)
auto.click()

auto.keyDown('command')
auto.press('down')
auto.keyUp('command')
