import ai
import text_moudle as tx



def main():
    string_1 = "shit ass"
    string_1 = tx.remove_punct(string_1).strip()
    print(string_1)
    if tx.if_severe_sentence(tx.text_analyzer(string_1)):
        res = ai.generate_ai_check_message(string_1)
        print(res)

if __name__ == '__main__':
    main()