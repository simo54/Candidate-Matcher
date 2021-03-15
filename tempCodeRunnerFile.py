  # text_to_analyze = ''
            # results = []
            # with pdfplumber.open(data_path) as pdf:
            #     for page in pdf.pages:
            #         page_text = page.extract_text()
            #         page_text.lower()
            #         text_to_analyze = text_to_analyze + '\n' + page_text

            #     text_formatted = text_to_analyze.lower()

            #     for key_word in key_words:
            #         key_word_formatted = key_word.lower()
            #         match = text_formatted.count(key_word_formatted)
            #         results.append(match)
            # print(results)
            # print(len(results))
            # hits = [x for x in results if x != 0]
            # print(hits)
            # print(len(hits))
            # no_hits = [x for x in results if x == 0]
            # print(no_hits)
            # print(len(no_hits))
            # print("{:.0%}".format(len(hits) / len(results)))