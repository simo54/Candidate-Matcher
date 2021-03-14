import os
import docx
import pdfplumber

from pathlib import Path
from tkinter import Button, Tk, filedialog, messagebox


# GUI Specifications
root = Tk()
root.title("ATS")

# GUI position
window_width = 700
window_height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2)-(window_width / 2)
y = (screen_height / 2)-(window_height / 2)

root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# declaring key words
key_words = ["one", "two", "three"]

# uploading file


def upload():
    file_path = filedialog.askopenfilename()
    data_path = Path(file_path)
    name, extension = os.path.splitext(file_path)

    if extension == '.pdf':
        with pdfplumber.open(data_path) as pdf:
            first_page = pdf.pages[0]
            print(first_page.page_number)
            text = first_page.extract_text()  # type => str
            print(text)
            pdf.close()

    elif extension == '.docx':
        inputStream = docx.Document(data_path)
        print(inputStream)
    else:
        messagebox.showinfo("WARNING", "Please upload a valid document")


# widgets list
button_upload = Button(root, text="Upload", padx=10, pady=5, command=upload)

# display widgets
button_upload.pack()

# runner
root.mainloop()
