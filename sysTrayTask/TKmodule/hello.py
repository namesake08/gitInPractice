from tkinter import *



#win = Frame()
#win.pack()
#Label(win, text='Basic demos').pack()
#for(key, value) in demos.items():
#	Buttom(win, text=key, command=value).pack(side=TOP, fill=BOTH)
#win.mainloop()


class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		Label(self, text='Basic demos').pack()
		for(key, value) in demos.items():
			Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
Demo().mainloop()
