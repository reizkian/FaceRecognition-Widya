
"""
 Created by Reizkian Yesaya .R @27 August 2020
 knowledge test PT WIDYA INOVASI INDONESIA - AI ENGINEER
 -------------------------------------------------------
 reizkian-FaceRecognizer app consist of:
 1. main.py (user interface)
 2. capture.py (feature)
 3. train.py (feature)
 4. predict (feature)
"""

import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox,PhotoImage
from tkinter import font as tkfont

from capture import CapImages, CapVideo
from train import TrainImages
from predict import predict

# global variable save user name
names=set()

class MainUserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        global names
        with open("namelist.txt", "r") as filetxt:
            read_filetxt = filetxt.read()
            list_filetxt = read_filetxt.rstrip().split(" ")
            for i in list_filetxt:
                names.add(i)

        tk.Tk.__init__(self, *args, **kwargs)
        self.active_name = None
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("Reizkian - Face Recognizer")
        self.resizable(False, False)
        self.geometry("365x175")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for FRAME in (StartPage,UserInput,PredictionPage,UserListPage):
            frame = FRAME(container,self)
            self.frames[FRAME] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        render = PhotoImage(file='./data/wr.png')
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(columnspan=3, sticky="nsew", ipady=5, ipadx=5)
        button1 = tk.Button(self, text="   User Input  ", fg="#ffffff", bg="#1c5784",command=lambda: self.controller.show_frame(UserInput))
        button2 = tk.Button(self, text="   User List  ", fg="#ffffff", bg="#1c5784",command=lambda: self.controller.show_frame(UserListPage))
        button3 = tk.Button(self, text="   Predict  ", fg="#ffffff", bg="#1c5784",command=lambda: self.controller.show_frame(PredictionPage))
        button1.grid(row=1, column=0, ipady=3, ipadx=7)
        button2.grid(row=1, column=1, ipady=3, ipadx=2)
        button3.grid(row=1, column=2, ipady=3, ipadx=2)

class UserInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        label_instruction = tk.Label(self, text="Please fill the user name, then click 'take images data' or 'take video data' ")
        label_Name = tk.Label(self, text="       user name    ", font="13")
        self.entry_Name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        button_Save = tk.Button(self, text=" save ", fg="#ffffff", bg="#1c5784", command=self.get_username)
        button_Home = tk.Button(self, text="   home   ", fg="#ffffff", bg="#1c5784",command=lambda: self.controller.show_frame(StartPage))
        button_ImageData = tk.Button(self, text="   take images data   ", fg="#ffffff", bg="#1c5784", command=self.CaptureImages)
        button_VideoData = tk.Button(self, text="   take video data   ", fg="#ffffff", bg="#1c5784", command=self.CaptureVideo)

        label_Name.grid(row=0,column=0, pady=15)
        self.entry_Name.grid(row=0,column=1, pady=15)
        button_Save.grid(row=0,column=2, pady=15, padx=5)

        button_ImageData.grid(columnspan=3, pady=5)
        button_VideoData.grid(columnspan=3, pady=5)
        button_Home.grid(columnspan=3, pady=5)

    # def get_username(self):
    #     global names
    #     name = self.entry_Name.get()
    #     names.add(name)
    #     self.active_name = name

    def get_username(self):
        global names
        name = self.entry_Name.get()
        names.add(name)
        self.active_name = name
        filetxt = open ("namelist.txt","a")
        filetxt.write(name + " ")

    def CaptureImages(self):
        messagebox.showinfo("INSTRUCTIONS", "We will Capture 300 pic of your Face\nPlease wait until the Web Cam is oppened")
        name = self.active_name
        CapImages(name)
        self.controller.show_frame(PredictionPage)
    
    def CaptureVideo(self):
        name = self.active_name
        messagebox.showinfo("INSTRUCTIONS", "We will Capture a video\nPlease wait until the Web Cam is oppened")
        CapVideo(name)
        self.controller.show_frame(PredictionPage)

class UserListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global names
        filetxt = open("namelist.txt","r")
        filetxt.read

        self.controller = controller
        tk.Label(self, text="user list", fg="#1c5784", font='Helvetica 12 bold').grid(row=0, column=0, padx=10, pady=10)
        self.buttoncanc = tk.Button(self, text="    cancel    ", command=lambda: controller.show_frame(StartPage), bg="#ffffff", fg="#1c5784")
        self.menuvar = tk.StringVar(self)
        self.dropdown = tk.OptionMenu(self, self.menuvar, *names)
        self.dropdown.config(bg="lightgrey")
        self.dropdown["menu"].config(bg="lightgrey")
        self.buttonext = tk.Button(self, text="    add user    ", command=lambda: controller.show_frame(UserInput), fg="#ffffff", bg="#1c5784")
        
        self.dropdown.grid(row=0, column=1, ipadx=8, padx=10, pady=20)
        self.buttoncanc.grid(row=1, ipadx=5, ipady=4, column=0, pady=10)
        self.buttonext.grid(row=1, ipadx=5, ipady=4, column=1, pady=10)

class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.controller = controller
        render = PhotoImage(file='./data/w.png')
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(rowspan=4,column=1, sticky="nsew", ipady=5, ipadx=5)
       
        label_WebCamRecognizer = tk.Label(self, text="Web Cam Recognizer", fg="#1c5784")
        button_RefreshTraining = tk.Button(self, text="    Data Training   ", fg="#ffffff", bg="#1c5784", command=self.RefreshTraining)
        button_WebCam = tk.Button(self, text="   Open Web Cam  ", fg="#ffffff", bg="#1c5784", command=self.WebCamFaceRecognition)
        button_Home = tk.Button(self, text="   home   ", fg="#ffffff", bg="#1c5784",command=lambda: self.controller.show_frame(StartPage))
        
        label_WebCamRecognizer.grid(row=0,column=0)
        button_RefreshTraining.grid(row=1, column=0, pady=5, padx=10)
        button_WebCam.grid(row=2, column=0, pady=10, padx=5)
        button_Home.grid(row=3,column=0, pady=10, padx=5)

    def RefreshTraining(self):
        messagebox.showinfo("INSTRUCTIONS", "Training on the new collected images dataset\nPlease wait.")
        TrainImages()
    def WebCamFaceRecognition(self):
        predict()

app = MainUserInterface()
app.mainloop()