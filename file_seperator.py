import os, shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  
new=tk.Tk()
new.geometry("200x100")
new.title('seperator')

table_label=ttk.Label(new,text="Enter URL   ").grid(row=0,column=0,sticky=tk.W)
name_var=tk.StringVar()
name_entry=ttk.Entry(new,width=20,textvariable=name_var).grid(row=0,column=1)
ttk.Label(new,text="   ").grid(row=1,column=0,sticky=tk.W)
def action():
    try:
        dict_extensions = {
        'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
        'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
        'document_extensions' : ('.doc', '.pdf', '.txt'),
        'walpaper_extensions' : ('.jpg','.png'),
        }


        folderpath =name_var.get()
    

        def file_finder(folder_path, file_extensions):
            files = []
            for file in os.listdir(folder_path):
                for extension in file_extensions:
                    if file.endswith(extension):
                        files.append(file)
            return files

        for extension_type, extension_tuple in dict_extensions.items():
            folder_name = extension_type.split('_')[0] + 'Files'
            folder_path = os.path.join(folderpath, folder_name)
            os.mkdir(folder_path)
            for item in file_finder(folderpath, extension_tuple):
                item_path = os.path.join(folderpath,item)
                item_new_path = os.path.join(folder_path,item)
                shutil.move(item_path,item_new_path)
        top = tk.Tk()  
        top.geometry("100x100")  
        messagebox.showinfo("information","files seperated")
        top.mainloop()  
    except:
        top = tk.Tk()  
        top.geometry("100x100")  
        messagebox.showerror("error","Error")  
        top.mainloop()  


submit_button=ttk.Button(new,text="submit",command=action)
submit_button.grid(row=4,column=1)

new.mainloop()
