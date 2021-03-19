import pdfplumber
import re
import os

from xlsx_file import workbook, excel_file
from openpyxl import load_workbook
from key_words import key_words


def upload_pdf(file):
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
    email_user = re.search(r'[\w\.-]+@[\w\.-]+', text_formatted)

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
