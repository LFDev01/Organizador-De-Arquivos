import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


class App:
    def __init__(self, root):
        self.master = root
        self.master.geometry(f'{500}x{300}+{int(self.master.winfo_screenwidth()/2 - 500/2)}+{int(self.master.winfo_screenheight()/2 - 300/2)}')
        self.master.title('Organizador de Arquivos')
        self.master.configure(bg='#d9d9d9')
        self.master.iconbitmap('images/folder1.ico')
        self.img = tk.PhotoImage(file='images/folder.png')
        self.img_2 = tk.PhotoImage(file='images/enter.png')
        self.master.resizable(False, False)


    def __setLabelValue(self, event):
        if event:
            self.label.configure(text=self.label_msg)
        else:
            self.label.configure(text='')


    def __Run(self):


        os.chdir(self.path)
        file_list = os.listdir()
  
        files_bytype = {
            'Documentos': ['.pdf', '.docx', '.xls'],
            'Imagens': ['.png', '.jpg', '.gif'],
            'Arquivo de Texto': ['.txt'],   
            'Arquivos Executáveis': ['.exe'],
            'Vídeos': ['.mp4'],
            'Músicas': ['.mp3'],
            'Arquivos Compactados': ['.zip', '.rar']
        }

        fileIsOrganized = None
        for file in file_list:
            fileIsOrganized = False
            get_ext = os.path.splitext(file)

            for foldertype, ext_list in files_bytype.items(): 

                if get_ext[1] in ext_list:
                    fileIsOrganized = True
                    if not os.path.exists(foldertype):
                        os.mkdir(foldertype)

                    shutil.move(file, foldertype)
                    break

        else:
            if fileIsOrganized:
                messagebox.showinfo('Info', 'Arquivos organizados!')
            else:
                messagebox.showinfo('Info', 'Não há arquivos para organizar.')
    
        self.new_btn.destroy()
        self.path_label.destroy()
        self.Start()


    def __OpenDir(self):

        self.path = filedialog.askdirectory()

        if len(self.path) > 0:
            self.label_msg = 'Organizar'
            self.btn.destroy()

            self.new_btn = tk.Button(master=self.master, image=self.img_2, 
            bg='#d9d9d9', borderwidth=0, activebackground='#d9d9d9', command=self.__Run)
            self.new_btn.place(x=220, y=80)
            self.label.place(x=224, y=150)

            self.path_label = tk.Label(master=self.master, text=self.path, bg='#d9d9d9')
            self.path_label.place(x=150, y=50)


            self.new_btn.bind('<Enter>', lambda x: self.__setLabelValue(1))
            self.new_btn.bind('<Leave>', lambda x: self.__setLabelValue(0))


    def Start(self):
        self.path = None
        self.label_msg = 'Escolher Diretório'

        self.btn = tk.Button(master=self.master, image=self.img, 
        bg='#d9d9d9', borderwidth=0, activebackground='#d9d9d9', command=self.__OpenDir, )
        self.btn.place(x=220, y=80)

        self.label = tk.Label(master=self.master, bg='#d9d9d9', font=('Tahoma', 8, 'bold'))
        self.label.place(x=200, y=150)

        self.btn.bind('<Enter>', lambda x: self.__setLabelValue(1))
        self.btn.bind('<Leave>', lambda x: self.__setLabelValue(0))

    
root = tk.Tk()
app = App(root)
app.Start()
root.mainloop()
