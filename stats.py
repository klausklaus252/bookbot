def getbooktext (file_path):
    with open(file_path) as f:
        file_content = f.read()

        return file_content

def get_num_words (path_to_book):
    count = 0
    book = getbooktext(path_to_book)
    words = book.split()
    for word in words:
        count = count +1
    
    return count


def get_num_characters(path_to_book):
    string = getbooktext(path_to_book)
    chars_dict = {}
    for i in string:
        if i.lower() in chars_dict:
            chars_dict[i.lower()] += 1
            
        else:
            chars_dict.update({i.lower(): 1})


    return chars_dict

def sort_char (chars_dict):
    sorted_chars =[]
    for i in chars_dict:
        if i.isalpha():
            sorted_chars.append({"char": i.lower(), "num": chars_dict[i]} )
    
    return sorted_chars
