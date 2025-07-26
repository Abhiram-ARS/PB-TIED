# -----------------------------------------------------------------------------
# Title       : PB-FED (Password-Based File Encrption-Decryption) Tool
# Author      : https://github.com/Abhiram-ARS
# Description : This Python-based tool provides a simple yet secure way 
#               to encrypt and decrypt messages using a password.
# Version     : Graphical User Interface - I (gui-1) : Windows
# -----------------------------------------------------------------------------
import tkinter as tk
import art
from pbfedFunctions import pbfedFunctions as pf

def closeWindow():
    root.destroy()

def MainMenu():
    def message_Button():
        message_Menu()

    def textFile_Button():
        textFile_Menu()

    def image_Button():
        image_Menu()

    def pdf_Button():
        pdf_Menu()
        
    
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("PB-FED",) #adding Title to a program

    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('consolas',12),bg='#C2C2C2',fg="black")
    button1 = tk.Button(root,text='Message',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=message_Button)
    button2 = tk.Button(root,text='Text File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=textFile_Button)
    button3 = tk.Button(root,text='Image File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=image_Button)
    button4 = tk.Button(root,text='PDF & Other File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=pdf_Button)
    button5 = tk.Button(root,text='Exit',font=('Ariel',16),width='20',bg='#FF7878',command=root.destroy)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=10)          
    button2.pack(pady=10)           
    button3.pack(pady=10)
    button4.pack(pady=10)
    button5.pack(pady=10)

    root.mainloop() # Calling Window to pop-up
def home():
    MainMenu()

# ================================================================================================================================================
# =============================================================================== Message ========================================================
# ================================================================================================================================================
def message_Menu():
    def encryptMessage_Button():
        encryptMessage_Menu()
    
    def decryptMessage_Button():
        decryptMessage_Menu()

    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Message") #adding Title to a program

    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label
    button1 = tk.Button(root,text='Encrypt Message',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptMessage_Button)
    button2 = tk.Button(root,text='Decrypt Message',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptMessage_Button)
    button3 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=20)          
    button2.pack(pady=20)           
    button3.pack(pady=20)

    root.mainloop()

def encryptMessage_Menu():
    def encryptMessage():
        from tkinter import messagebox
        message = tbdata.get()
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "msg" : message, 
                "file": file}

        result = pf.encryptMessage_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Encrypt Message") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" Message   :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbdata=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))
    label4=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Encrypt Message',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptMessage)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)

    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbdata.grid(row=0,column=1,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    label4.grid(row=2,column=0,pady=10)
    tbfile.grid(row=2,column=1,pady=10)

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

def decryptMessage_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def decryptTextFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}

        result = pf.decryptTextFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Decrypt File") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Decrypt Message',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptTextFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()


# ================================================================================================================================================
# =========================================================================== Text File ==========================================================
# ================================================================================================================================================
def textFile_Menu():
    def encryptMessage_Button():
        encryptTextFile_Menu()
    
    def decryptMessage_Button():
        decryptTextFile_Menu()

    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Text File") #adding Title to a program

    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label
    button1 = tk.Button(root,text='Encrypt Text File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptMessage_Button)
    button2 = tk.Button(root,text='Decrypt Text File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptMessage_Button)
    button3 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=20)          
    button2.pack(pady=20)           
    button3.pack(pady=20)

    root.mainloop()

def encryptTextFile_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def encryptTextFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}

        result = pf.encryptTextFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Encrypt File") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Encrypt File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptTextFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

def decryptTextFile_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def decryptTextFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}

        result = pf.decryptTextFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Decrypt File") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Decrypt File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptTextFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

# ================================================================================================================================================
# ========================================================================= IMAGE Encryption =====================================================
# ================================================================================================================================================

def image_Menu():
    def encryptImage_Button():
        encryptImage_Menu()
    
    def decryptImage_Button():
        decryptImage_Menu()

    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Image File") #adding Title to a program

    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label
    button1 = tk.Button(root,text='Encrypt Image',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptImage_Button)
    button2 = tk.Button(root,text='Decrypt Image',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptImage_Button)
    button3 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=20)          
    button2.pack(pady=20)           
    button3.pack(pady=20)

    root.mainloop()

def encryptImage_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("Images", ("*.jpg", "*.jpeg", "*.png"))]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def encryptImageFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}
        
        result = pf.encryptBinFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Encrypt Image") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" File____:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Encrypt Image',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptImageFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

def decryptImage_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a Image File",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def decryptImageFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}
        
        result = pf.decryptBinFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Decrypt Image") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Decrypt Image',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptImageFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

# ================================================================================================================================================
# ========================================================================= PDF Encryption =====================================================
# ================================================================================================================================================

def pdf_Menu():
    def encryptPdf_Button():
        encryptPdf_Menu()
    
    def decryptPdf_Button():
        decryptPdf_Menu()

    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("PDF File") #adding Title to a program

    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label
    button1 = tk.Button(root,text='Encrypt File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptPdf_Button)
    button2 = tk.Button(root,text='Decrypt File',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptPdf_Button)
    button3 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=20)          
    button2.pack(pady=20)           
    button3.pack(pady=20)

    root.mainloop()

def encryptPdf_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a PDF File",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def encryptPdfFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}
        
        result = pf.encryptBinFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Encrypt PDF") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="#4D4D4D") # defining Label

    label2=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Encrypt PDF',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=encryptPdfFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

def decryptPdf_Menu():
    def browse_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            tbfile.delete(0, tk.END)
            tbfile.insert(0, file_path)

    def decryptPdfFile():
        from tkinter import messagebox
        passwd = tbpwd.get()
        file = tbfile.get()
        data = {"pwd" : passwd,
                "file": file}
        
        result = pf.decryptBinFile_funct(data)
        if result['stat']==1:
            messagebox.showinfo("Notification", "Sucess :"+result['note'])
        else:
            messagebox.showerror("Notification", "Failed :"+result['note'])
                     
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg="#C2C2C2")
    root.title("Decrypt PDF") #adding Title to a program

    frame=tk.Frame(root,bg='#C2C2C2')
    title = art.text2art("PB-FED", font="Tarty1")
    label1=tk.Label(root,text=title,font=('Consolas',12),bg='#C2C2C2',fg="black") # defining Label

    label2=tk.Label(frame,text=" File______:",font=('Times New Roman',18),bg="#4D4D4D",fg="White")
    tbfile=tk.Entry(frame,width='40',font=('Ariel',24))
    label3=tk.Label(frame,text=" Password  :",font=('Times New Roman',18),bg='#4D4D4D',fg="White")
    tbpwd=tk.Entry(frame,width='40',font=('Ariel',24))

    button1 = tk.Button(root,text='Decrypt PDF',font=('Ariel',16),width='20',bg='#4D4D4D',fg="White",command=decryptPdfFile)
    button2 = tk.Button(root,text='BACK',font=('Ariel',16),width='20',bg='#FF7878',command=home)
    button_brs = tk.Button(frame, text="Browse",bg="#030303",fg="White",command=browse_file)


    label1.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0,pady=10)
    tbfile.grid(row=0,column=1,pady=10)
    button_brs.grid(row=0, column=2,pady=10)
    label3.grid(row=1,column=0,pady=10)
    tbpwd.grid(row=1,column=1,pady=10)
    

    button1.pack(pady=20)          
    button2.pack(pady=20)

    root.mainloop()

# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================


MainMenu()
