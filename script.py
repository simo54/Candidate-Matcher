from __future__ import division
import os
import docx
import pdfplumber

from pathlib import Path
from tkinter import Button, Tk, filedialog, messagebox
from openpyxl import Workbook, load_workbook


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
key_words = ["python", "team", "joy", "javascript", "node"]

# Xlsx file
workbook = Workbook()
excel_file = Path("./score_sheet.xlsx")

# uploading files


def upload():
    file_path_list = filedialog.askopenfilenames(initialdir="/", title='test')

    for file in file_path_list:
        name, extension = os.path.splitext(file)

        if extension == '.pdf':
            text_to_analyze = ''
            results = []
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    page_text.lower()
                    text_to_analyze = text_to_analyze + '\n' + page_text

                text_formatted = text_to_analyze.lower()

                for key_word in key_words:
                    key_word_formatted = key_word.lower()
                    match = text_formatted.count(key_word_formatted)
                    results.append(match)
            hits = [x for x in results if x != 0]
            score = str("{:.0%}".format(len(hits) / len(results)))
            value_row = [[str(os.path.basename(
                file)), str("{:.0%}".format(len(hits) / len(results)))]]

            if excel_file.is_file():
                working_file = load_workbook(filename=excel_file)
                page = working_file.active
                for data in value_row:
                    page.append(data)
                working_file.save(filename=excel_file)
            else:
                page = workbook.active
                for data in value_row:
                    page.append(data)
                workbook.save(filename="score_sheet.xlsx")

        elif extension == '.docx':
            doc = docx.Document(file)
            text_to_analyze = ''
            results = []
            for docpara in doc.paragraphs:
                text_to_analyze += docpara.text

            text_formatted = text_to_analyze.lower()

            for key_word in key_words:
                key_word_formatted = key_word.lower()
                match = text_formatted.count(key_word_formatted)
                results.append(match)
            hits = [x for x in results if x != 0]
            score = str("{:.0%}".format(len(hits) / len(results)))
            value_row = [[str(os.path.basename(
                file)), score]]

            if excel_file.is_file():
                working_file = load_workbook(filename=excel_file)
                page = working_file.active
                for data in value_row:
                    page.append(data)
                working_file.save(filename=excel_file)

            else:
                page = workbook.active
                for data in value_row:
                    page.append(data)
                workbook.save(filename="score_sheet.xlsx")

        else:
            messagebox.showinfo("WARNING", "Please upload a valid document")


# widgets list
button_upload = Button(root, text="Upload", padx=10, pady=5, command=upload)

# display widgets
button_upload.pack()

# runner
root.mainloop()
