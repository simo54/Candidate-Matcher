import PyPDF2
from PyPDF2 import PdfFileReader
from tkinter import Button, Tk, filedialog

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
    file = filedialog.askopenfilename()
    if file != file.lower().endswith(('.pdf', '.doc', '.docx', '.odt', '.txt', '.xml', '.xps', 'rtf')):
        print("ah")


# widgets list
button_upload = Button(root, text="Upload", padx=10, pady=5, command=upload)

# display widgets
button_upload.pack()

# runner
root.mainloop()
