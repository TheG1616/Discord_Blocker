import re

def read_file(file):
    f = open((file))
    data = f.read()
    return data

def make_list_of_bad_words(data):
    list_of_bad_words = data.split("\n")
    return list_of_bad_words




def remove_punct(text):
    new_words = ""
    for word in text:
        w = re.sub(r'[^\w\s]','',word) #remove everything except words and space
        w = re.sub(r'_','',w) #how to remove underscore as well
        new_words+= w
    return new_words


def text_analyzer(string):
    list_of_bad_words = make_list_of_bad_words(read_file("bad_words"))
    list_sentence = string.split(" ")
    count_bad_words = 0
    for word in list_sentence:
        if word in list_of_bad_words:
            count_bad_words+=1
    return count_bad_words / len(list_sentence)


print(make_list_of_bad_words(read_file("bad_words")))