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
key_words = ["simone", "html", "js"]

# uploading file


def upload():
    file_path = filedialog.askopenfilename()
    data_path = Path(file_path)
    name, extension = os.path.splitext(file_path)

    if extension == '.pdf':
        text_to_analyze = ''
        results = []
        with pdfplumber.open(data_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                text_to_analyze = text_to_analyze + '\n' + page_text
            for key_word in key_words:
                count = text_to_analyze.count(key_word)
                print(key_word)
                if count == 0:
                    print("count is 0")
                    key_word_upper = key_word.upper()
                    print(key_word_upper)
                    count = text_to_analyze.count(key_word_upper)
                    results.append(count)
                else:
                    results.append(count)
            print(results)
            # print(text_to_analyze)

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
