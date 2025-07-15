try:
	# please use .pyw format when running

	from tkinter import *
	from sys import exit
	root=Tk()
	import pyautogui,time,keyboard,random,win32api,win32con,win32process,os
	import pathlib
	dir = pathlib.Path(__file__).parent.resolve() # current directory
	print(f'current file directory = "{dir}"')
	from colorama import Fore, Back, Style
	from pynput.keyboard import Key
	def nothing():
		pass
	def click(x,y):
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
		# time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

	root.title('Autoclicker²')
	root.geometry("300x150")
	root.configure(background='#000000')
	root.wm_attributes("-topmost", 1)
	root.tk_setPalette(background='#000000', foreground='white')
	root.iconphoto(True,PhotoImage(file=f'{dir}/_internal/_tkinter/icon.png'))

	enabled=0
	def update_gui(x=''):
		global mylabel1,mylabel2,mybutton1,mybutton2
		for child in root.winfo_children():child.destroy()
		mylabel1 = Label(root, text='Autoclicker²').grid(row=1,column=3)
		if enabled==1:
			mylabel2 = Label(root, text='ON',fg='green',font='bold',bg='black').grid(row=3,column=3)
			mybutton1 = Button(root, text='enable (F8)', command=enable,padx=20, pady=20, state='disabled').grid(row=2, column=0,columnspan=2)
			mybutton2 = Button(root, text='disable (F8)', command=disable, padx=20, pady=20).grid(row=2, column=4,columnspan=2)
		else:
			mylabel2 = Label(root, text='OFF',fg='red',font='bold',bg='black').grid(row=3,column=3)
			mybutton1 = Button(root, text='enable (F8)', command=enable,padx=20, pady=20).grid(row=2, column=0,columnspan=2)
			mybutton2 = Button(root, text='disable (F8)', command=disable, padx=20, pady=20, state='disabled').grid(row=2, column=4,columnspan=2)
	def toggle(x=''):
		global enabled, mylabel2
		enabled += 1 if enabled == 0 else -1
		update_gui()
	def enable():
		global enabled, mylabel2
		enabled += 1 if enabled == 0 else 0
		update_gui()
	def disable():
		global enabled, mylabel2
		enabled += 0 if enabled == 0 else -1
		update_gui()
	def tick(x=''):
		global enabled
		if keyboard.is_pressed('f8'):
			while keyboard.is_pressed('f8'):
				nothing()
			toggle()
		if enabled==1:
				click(pyautogui.position()[0],pyautogui.position()[1])
		root.after(1,tick)

	root.columnconfigure(0, weight=1)
	root.columnconfigure(1, weight=1)
	root.columnconfigure(2, weight=1)
	root.columnconfigure(3, weight=1)
	root.columnconfigure(4, weight=1)
	root.columnconfigure(5, weight=1)
	root.columnconfigure(6, weight=1)

	update_gui()

	root.after(1,tick)
	root.mainloop()
except Exception as e:
	root.destroy()
	print(f'{Fore.RED}Error:{Style.RESET_ALL} {e}')
	input(f'{Fore.BLUE}press ↵ to exit{Style.RESET_ALL}\n')
	exit()