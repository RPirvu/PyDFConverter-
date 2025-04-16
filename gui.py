# gui.py
import tkinter
import customtkinter
from CTkListbox import *
from pdf_converter import convert_to_pdf

def create_app():
    customtkinter.set_appearance_mode("System")

    app = customtkinter.CTk()
    app.title('To PDF')
    app.geometry("720x480")

    listbox = CTkListbox(app, command=lambda val: print("Selected:", val), multiple_selection=True)
    listbox.pack(fill="both", expand=True, padx=10, pady=10)

    def browse_images():
        file_types = [('Image files', '*.jpeg *.jpg *.png *.gif *.bmp'), ('All files', '*.*')]
        file_paths = tkinter.filedialog.askopenfilenames(title="Select file(s)", filetypes=file_types)
        for path in file_paths:
            listbox.insert(tkinter.END, path)

    def delete_item():
        for i in reversed(listbox.curselection()):
            listbox.delete(i)

    def clear_list():
        listbox.delete(tkinter.ALL)

    select_button = customtkinter.CTkButton(app, text="Select Images", command=browse_images)
    select_button.pack(fill=tkinter.X)

    convert_button = customtkinter.CTkButton(app, text="To PDF", command=lambda: convert_to_pdf(listbox.get(tkinter.ALL)))
    convert_button.pack(fill=tkinter.X)

    remove_button = customtkinter.CTkButton(app, text='Remove Selected', command=delete_item)
    remove_button.pack(fill=tkinter.X)

    clear_button = customtkinter.CTkButton(app, text='Clear', command=clear_list)
    clear_button.pack(fill=tkinter.X)

    return app
