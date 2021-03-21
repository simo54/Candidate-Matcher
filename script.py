from __future__ import division
from pathlib import Path
from tkinter import Button, Tk, filedialog, messagebox, PhotoImage, Label, Toplevel, Text
from tkinter.font import Font
from openpyxl import Workbook, load_workbook
from upload_pdf import upload_pdf
from upload_docx import upload_docx
from PIL import ImageTk, Image
from key_words import write_keywords, return_keys
from upload_un_files import upload_un_files

import os
import webbrowser


def main():
    # GUI Specifications
    root = Tk()
    root.title("ATS")
    root.configure(background='#F0F3F7')
    root.iconbitmap('assets/mac_icon-icons.com_54610.ico')

    # GUI position
    window_width = 600
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2)-(window_width / 2)
    y = (screen_height / 2)-(window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    # Assets Images
    upload_button = PhotoImage(file='assets/button_upload.png')
    keys_button = PhotoImage(file='assets/button_keywords.png')
    quit_button = PhotoImage(file='assets/button_exit.png')
    main_picture = Image.open("./assets/cup-of-coffee-1280537_1920.png")
    main_picture = main_picture.resize((550, 350), Image.ANTIALIAS)
    main_picture = ImageTk.PhotoImage(main_picture)

    def upload():

        file_path_list = filedialog.askopenfilenames(
            initialdir="/", title='Upload single or multiple .pdf and/or .docx files')

        if len(file_path_list) != 0:
            window_width = 100
            window_height = 100
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2)-(window_width / 2)
            y = (screen_height / 2)-(window_height / 2)
            popup_loading = Toplevel()
            popup_loading.geometry(
                f'{window_width}x{window_height}+{int(x)}+{int(y)}')

            info = Label(
                popup_loading, text="Loading...")
            info.pack(fill='x', padx=15, pady=15)

            for file in file_path_list:
                name, extension = os.path.splitext(file)
                if extension == '.pdf':
                    upload_pdf(file)
                elif extension == '.docx':
                    upload_docx(file)
                else:
                    upload_un_files(file)

            popup_loading.after(5000, lambda: popup_loading.destroy())

    def define_keywords():
        def get_text():
            text_to_pass = input_keywords.get(1.0, "end-1c")
            write_keywords(text_to_pass)

        window_width = 600
        window_height = 550
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2)-(window_width / 2)
        y = (screen_height / 2)-(window_height / 2)
        window = Toplevel()
        window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

        info = Label(
            window, text="Please declare here your keywords following this example: ")
        example = Label(window, text="Example: ")
        input_keywords = Text(window)
        input_keywords.insert(1.0, return_keys())
        button_save = Button(window, text="Save",
                             command=get_text)
        button_close = Button(window, text="Close", command=window.destroy)

        info.pack(fill='x', padx=15, pady=3)
        example.pack(fill='x')
        input_keywords.pack(padx=15, pady=3)
        button_save.pack()
        button_close.pack()

    def open_url():
        url = "https://github.com/simo54/free_ats/blob/main/README.md"
        webbrowser.open_new(url)

    # widgets list
    title_font = Font(family="Courier", size=36)
    title_text = Label(root, text="ATS", font=title_font)
    label_picture = Label(image=main_picture)
    button_guide = Button(root, text="info",
                          padx=10, pady=5, borderwidth=0, command=open_url)
    button_upload = Button(root, image=upload_button,
                           padx=10, pady=5, command=upload, borderwidth=0)
    button_keywords = Button(root, image=keys_button,
                             padx=10, pady=5, command=define_keywords, borderwidth=0)
    button_quit = Button(root, image=quit_button,
                         borderwidth=0, padx=10, pady=5, command=root.quit)

    title_text.grid(row=0, column=0, columnspan=5)
    label_picture.grid(row=1, column=0, columnspan=5)
    button_guide.grid(row=2, column=1, columnspan=1)
    button_upload.grid(row=2, column=2, columnspan=1)
    button_keywords.grid(row=2, column=3, columnspan=1)
    button_quit.grid(row=2, column=4, columnspan=1)

    # runner
    root.mainloop()


if __name__ == "__main__":
    main()
