from pathlib import Path

txt_file = Path("keywords.txt")


def return_keys():
    if txt_file.is_file():
        txt = open("keywords.txt", "r+")
        list_key_words = [word for line in txt for word in line.split()]
        key_words = list_key_words
        return key_words
    else:
        list_key_words = []
        key_words = list_key_words
        return key_words


print(return_keys())


def write_keywords(keywords_text):
    txt = open("keywords.txt", "w")
    txt.truncate(0)
    txt.write(keywords_text)
    txt.close()
    return_keys()
