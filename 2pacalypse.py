import os
import twopac
import random
import base64
import tempfile
import winsound
import ipaddress
import threading
import tkinter as tk
from time import sleep
from io import BytesIO
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as tkm


class Gui:
	def __init__(self, root, title):
		self.width = 800
		self.height = 450
		self.root = root
		self.title = title
		self.root.title(self.title)
		self.root.geometry(f"{self.width}x{self.height}")
		self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

		# self.correctParameters = [False, False]
		self.tempFilePath = ""
		self.botnets = random.randint(10,90)
		self.audioplaying = True

		self.root.resizable(0,0)
		self.root.configure(bg="black")
		self.root.iconphoto(True, ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(twopac.data["img_blank"])))))
		self.root.wm_attributes('-toolwindow', True)

		self.frame = ttk.Frame(self.root, padding=0, borderwidth=0)
		self.frame.grid()

		self.audioctrl = ttk.Button(text="pause", command=self.music)
		self.audioctrl.grid(row=0, column=0)
		self.audioctrl.place(x=10, y=10)

		self.fakeip = None
		self.fakeport = None

		self.pactext = ttk.Label(
			self.root,
			text="2PACALYPSE 2.5",
			background="black",
			foreground="#16B60C",
			font=("Arial", 25)
			)
		self.pactext.grid(pady=20, row=0)
		self.pactext.place(anchor="center", relx=0.5, rely=0.1)

		self.author = ttk.Label(self.root,
			text="-Coded by evenblad3",
			background="black",
			foreground="#16B60C",
			font=("Arial", 15),
			).place(x=575, y=20)

		#######################  Start of IP and PORT
		# IP Text
		self.iptext = ttk.Label(
			self.root,
			text="IP: ",
			foreground="white",
			background="black",
			font=("Arial", 25),
			)
		self.iptext.grid(row=0, column=0)
		self.iptext.place(x=30, y=100)
		# IP Entry
		self.askip = ttk.Entry(
			self.root,
			text="64.231.75.201"
			)
		self.askip.grid(row=0, column=0)
		self.askip.place(x=80, y=110)
		# self.askip.lift()

		# PORT Text
		self.port = ttk.Label(
			self.root,
			text="Port: ",
			foreground="white",
			background="black",
			font=("Arial", 25),
			)
		self.port.grid(row=0, column=0)
		self.port.place(x=225, y=100)
		# IP Entry
		self.askport = ttk.Entry(
			self.root,
			width=6
			)
		self.askport.grid(row=0, column=0)
		self.askport.place(x=225+80, y=110)
		####################### END of IP and PORT

		self.real = tk.Label(self.root,
			text="r.i.p 2pac u were the meanin\nof lyfe -moneymack",
			font=("Arial", 20),
			foreground="#16B60C",
			background="#000"
			)
		self.real.grid(row=0, column=0)
		self.real.place(x=450, y=100-25)

		# Show number of botnets
		self.shownbotnets = ttk.Label(self.root, text=f"Botnets Online: {self.botnets}",
			font=("Arial", 20),
			background="black",
			foreground="white"
			)
		self.shownbotnets.lift()
		self.shownbotnets.grid(row=0, column=0)
		self.shownbotnets.place(x=20, y=400)

		self.ddosn_ = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(twopac.data["img_ddos"]))))
		self.ddosbutton = tk.Button(
			self.root,
			image=self.ddosn_,
			borderwidth=0,
			background="black",
			command=self.start_ddos
			)
		self.ddosbutton.place(x=100, y=200)

		self.pac = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(twopac.data["img_2pac"]))).resize((800-4, 350)))
		self.tupac = ttk.Label(self.root,
			image=self.pac,
			borderwidth=0,
			background="black" # There was no way to get rid of the border
			)
		self.tupac.grid(padx=0, pady=0, row=0, column=0)
		self.tupac.place(x=300+100, y=100)
		self.tupac.lower(self.real)

	def music(self):
		if self.audioplaying:
			self.audioplaying = False
			self.audioctrl.config(text="pause")
			#print("audio is playing")
			self.playmusic()
		else:
			self.audioplaying = True
			self.audioctrl.config(text="play")
			#print("audio is not playing")
			self.stopmusic()

	# def print_ddos_info(self):
	# 	print("DDOS Started!")
	# 	for i in range(100):
	# 		print(f"Attacking {self.fakeip}:{self.fakeport}")
	# 		sleep(random.randint(0, 2))


	def start_ddos(self):
		def showiperror():
			tkm.showerror(self.title, "yoyo chill invalid ip homie")
		def showporterror():
			tkm.showerror(self.title, "yoyo that no valid port bruh")

		try:
			self.fakeport = int(self.askport.get())
			if self.fakeport < 1 or self.fakeport > 65536:
				showporterror()
		except Exception as e:
			print(e)
			showporterror()

		try:
			self.fakeip = self.askip.get()
			ipaddress.ip_address(self.fakeip)
		except Exception as e:
			print(e)
			showiperror()

	def playmusic(self):
		try:
			audpath = base64.b64decode(twopac.data["aud_keygen"])
			with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tempFile:
				tempFile.write(audpath)
				self.tempFilePath = tempFile.name
	
			winsound.PlaySound(self.tempFilePath, winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_NODEFAULT)
		except Exception as e:
			print(f"Couldn't play the audio.\n{e}")
		finally:pass
			# print(self.tempFilePath)
	
	def stopmusic(self):
		winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_PURGE | winsound.SND_NODEFAULT)

	def run(self):
		self.root.mainloop()

	def onClosing(self):
		try:
			if os.path.exists(self.tempFilePath):
				# print(self.tempFilePath)
				os.unlink(self.tempFilePath)
			else:pass
		except Exception as e:
			print(e)
		finally:
			root.destroy()

root = tk.Tk()
g = Gui(root, "2PACALYPSE 2.5")
g.music()
g.run()
