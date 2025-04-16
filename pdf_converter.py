# pdf_converter.py
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image

def convert_to_pdf(images):
    try:
        images_list = [Image.open(image).convert('RGB') for image in images]

        if not images_list:
            tkinter.messagebox.showerror('Error', 'No images to convert.')
            return

        output_pdf_path = tkinter.filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
        )

        if not output_pdf_path:
            return

        images_list[0].save(output_pdf_path, save_all=True, append_images=images_list[1:])
        tkinter.messagebox.showinfo('Success', 'The images have been successfully converted to PDF!')

    except Exception as e:
        tkinter.messagebox.showerror('Error', f'An error occurred: {e}')
