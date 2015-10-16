import tkinter as tk
from tkinter import *
def runHelpWindowGUI():
	class helpWindow(tk.Frame):
		def __init__(self,master=None):
			tk.Frame.__init__(self,master,width=0,height=0)
			self.pack()
			self.grid(row=30,column=30)
			self.createWidgets()
			master.minsize(width=640,height=480)
			master.maxsize(width=640,height=480)
			master.title("FileExplorer by grapek9")
		def createWidgets(self):
			mainframe = tk.Frame(self,bg="orange",width=640,height=480)
			mainframe.grid(row=0,column=0)
			mainframe.pack()
			#two separated tables
			label1 = tk.Label(mainframe,bg="red",width=45,height=480)
			label2 = tk.Label(mainframe,bg="green",width=45,height=480)
			label1.grid(row=0,column=0)
			label2.grid(row=0,column=1)
			
	root= tk.Tk()
	app = helpWindow(master=root)
	app.mainloop()
	print("Help Window Closed")