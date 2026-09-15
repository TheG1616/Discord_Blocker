import text_moudle

string_1 = "yali, gabay. hello,// world$ niger knife ## "
print(text_moudle.remove_punct(string_1))
print(text_moudle.if_severe_sentence(text_moudle.text_analyzer(text_moudle.remove_punct(string_1))))