import tkinter as tk
from tkinter import ttk
from helpWindow import *
from os import *
def runGui():
	class MainWindow(tk.Frame):
		def __init__(self,master=None):
			tk.Frame.__init__(self,master,width=0,height=0)
			self.pack()
			self.grid(row=30,column=30)
			self.createWidgets()
			master.minsize(width=640,height=480)
			master.maxsize(width=640,height=480)
			master.title("FileExplorer by grapek9")
		def createWidgets(self):
			def openHelpWindow():
				runHelpWindowGUI();
				pass
			actual_path = StringVar()
			actual_path.set("test")
			mainframe = tk.Frame(self,bg="orange",width=640,height=480)
			mainframe.grid(row=0,column=0)
			mainframe.pack()
			#first layer
			frame1 = tk.Frame(mainframe,width=640)
			frame1.grid(row=0,column=0,columnspan=60)
			path = tk.Entry(frame1,width=101,textvariable=actual_path)
			path.grid(row=0,column=0)
			helpButton = tk.Button(frame1,text="Help",borderwidth=.003,command=openHelpWindow)
			helpButton.grid(row=0,column=1)
			#second layer
			frame2 = tk.Frame(mainframe,bg="green",width=640,height=460)
			frame2.grid(row=1,column=0,sticky="nsew",columnspan=60)


<<<<<<< HEAD
			listbox = tk.Listbox(frame2,height=29,width=106)
			listbox.grid(row=0,column=0,sticky=(N,W),columnspan=900)
=======
			listbox = tk.Listbox(frame2,height=29,width=200)
			listbox.grid(row=0,column=0,sticky=(N,W,E,S),columnspan=60)
>>>>>>> 006bba89dd26d0eb68d44afde932f8e110148210

			#scrollbar maybe in future, main idea is to not use mouse with this app
			#scrollbar = tk.Scrollbar(frame2,orient=VERTICAL,command=listbox.yview)
			#scrollbar.grid(row=0,column=1,sticky=(N,E))
			#scrollbar.grid_rowconfigure(0,weight=20)
			#githubproblems :(
			for i in range(1,101):
				listbox.insert("end",'Line %d of 100' %i)
	root= tk.Tk()
	root["bg"] = "grey"
	app = MainWindow(master=root)
	app.mainloop()
	print("Main Window Closed")
	

#reminder = building ui inside frame1