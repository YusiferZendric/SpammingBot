file = input('Enter the file name which contains the content to be written!\n>> ')
dur = int(input("Enter the duration of typing in seconds: "))
def main(filename, duration):
	import time
	import pyautogui 
	time.sleep(5)
	intial_time = time.time()
	a = open(filename, 'r')
	aread = a.read()
	while True:
		final_time = time.time() - intial_time
		pyautogui.FAILSAFE = False
		pyautogui.typewrite(aread)
		if final_time>=duration:
			exit()
main(file, dur)
