from xlsx_file import workbook, excel_file
from openpyxl import load_workbook


def load_and_write(value_row):
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
