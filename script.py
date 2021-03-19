from __future__ import division
from pathlib import Path
from tkinter import Button, Tk, filedialog, messagebox, PhotoImage, Label
from tkinter.font import Font
from openpyxl import Workbook, load_workbook
from upload_pdf import upload_pdf
from upload_docx import upload_docx
from PIL import ImageTk, Image

import os


def main():
    # GUI Specifications
    root = Tk()
    root.title("ATS")
    root.configure(background='#F0F3F7')
    root.iconbitmap('assets/mac_icon-icons.com_54610.ico')

    # GUI position
    window_width = 800
    window_height = 550

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2)-(window_width / 2)
    y = (screen_height / 2)-(window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    upload_button = PhotoImage(file='assets/button_upload.png')

    main_picture = Image.open("./assets/cup-of-coffee-1280537_1920.png")
    main_picture = main_picture.resize((550, 350), Image.ANTIALIAS)
    main_picture = ImageTk.PhotoImage(main_picture)

    def upload():
        file_path_list = filedialog.askopenfilenames(
            initialdir="/", title='Upload single or multiple .pdf and/or .docx files')

        for file in file_path_list:
            name, extension = os.path.splitext(file)

            if extension == '.pdf':
                upload_pdf(file)

            elif extension == '.docx':
                upload_docx(file)

            else:
                messagebox.showwarning(
                    "WARNING", "Please upload a valid document")

    def loading():
        messagebox.askquestion("askquestion", "Are you sure?")

    # widgets list
    title_font = Font(family="Courier", size=36)
    title_text = Label(root, text="ATS", font=title_font)

    label_picture = Label(image=main_picture)

    button_upload = Button(root, image=upload_button,
                           padx=10, pady=5, command=upload, borderwidth=0)
    button_quit = Button(root, text="Exit Program", command=root.quit)
    # display widgets
    title_text.pack()
    label_picture.pack()
    button_upload.pack()
    button_quit.pack()

    # runner
    root.mainloop()


if __name__ == "__main__":
    main()
