import os

from load_and_write import load_and_write


def upload_un_files(file):
    score = "unsupported file (not a .pdf nor .docx"
    email_user = "unsupported file (not a .pdf nor .docx"
    phone_number = "unsupported file (not a .pdf nor .docx"
    value_row = [[str(os.path.basename(file)), str(score),
                  str(email_user), str(phone_number)]]
    load_and_write(value_row)
