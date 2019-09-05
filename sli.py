import pyautogui
import time
import keyboard
import random

def ran_bot_det_prot(to):
	return random.randint(1,to)

def ran_bot_coord_x(frm, to):	
	x = random.randint(frm, to)
	if(not(1100 > x > 800)):
		return x
	else:
		return ran_bot_coord_x(frm, to)
	
def ran_bot_coord_y(frm, to):
	return random.randint(frm,to)


def call_keyboard_or_mouse_func(nr):
	if(nr is 1):
		pyautogui.moveTo(ran_bot_coord_x(16, 27), ran_bot_coord_y(796, 811))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(2))
		pyautogui.moveTo(ran_bot_coord_x(16, 27), ran_bot_coord_y(796, 811))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(3))
		pyautogui.moveTo(ran_bot_coord_x(16, 27), ran_bot_coord_y(796, 811))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(4))
		pyautogui.moveTo(ran_bot_coord_x(16, 27), ran_bot_coord_y(796, 811))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(4))
		pyautogui.moveTo(ran_bot_coord_x(14, 23), ran_bot_coord_y(870, 889))
		pyautogui.click()
	elif(nr is 2):
		pyautogui.moveTo(ran_bot_coord_x(1437, 1441), ran_bot_coord_y(1049, 1052))
		pyautogui.click()
	elif(nr is 3):
		pyautogui.moveTo(ran_bot_coord_x(23, 27), ran_bot_coord_y(800, 805))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(2))
		pyautogui.moveTo(ran_bot_coord_x(23, 26), ran_bot_coord_y(800, 802))
		pyautogui.click()
	elif(nr is 4):
		keyboard.press_and_release('o')
		time.sleep(ran_bot_det_prot(5))
		keyboard.press_and_release('o')
	elif(nr is 5):
		keyboard.press_and_release('t')
		time.sleep(ran_bot_det_prot(2))
		keyboard.press_and_release('t')
	elif(nr is 6):
		pyautogui.moveTo(ran_bot_coord_x(21, 26), ran_bot_coord_y(787, 794))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(2))
		pyautogui.moveTo(ran_bot_coord_x(23, 26), ran_bot_coord_y(786, 792))	
		pyautogui.click()
	elif(nr is 7):
		time.sleep(ran_bot_det_prot(2))
		pyautogui.moveTo(ran_bot_coord_x(1800, 1826), ran_bot_coord_y(200, 216))
		pyautogui.click()
		time.sleep(ran_bot_det_prot(3))		
		pyautogui.moveTo(ran_bot_coord_x(1800, 1826), ran_bot_coord_y(200, 216))
		pyautogui.click()		
	elif(nr is 8):
		keyboard.press_and_release('l')
		time.sleep(ran_bot_det_prot(7))
		keyboard.press_and_release('l')
	elif(nr is 10):
		keyboard.press_and_release('p')
		time.sleep(ran_bot_det_prot(3))
		keyboard.press_and_release('p')	
		
call_keyboard_or_mouse_func(1)
try:
	while True:
		time.sleep(random.randint(4,5))
		call_keyboard_or_mouse_func(ran_bot_det_prot(11))
		while(random.randint(1,10) < random.randint(1,10)):	
			time.sleep(random.randint(1,2))	
			pyautogui.moveTo(ran_bot_coord_x(1, 1400), ran_bot_coord_y(1, 1000))
			pyautogui.click()
except KeyboardInterrupt:
    pass
	