import googletrans
from googletrans import Translator

translator = Translator()

def _file_():
    str_total = []
    f = open("input", "rt", encoding='UTF8')
    lines = f.readlines()
    for line in lines:
        strs = line.strip("\n")
        if strs != "":         
            str_total.append(strs)
    f.close()
    result_str = " ".join(str_total)
    return result_str


def _log_write_(text):
    f = open("log", 'a')
    date = "\n\n============\nAdd Text===\n============\n"
    f.write(date)
    f.write(text)
    f.close()


if __name__ == '__main__':
    str_=_file_()
    query = str_.replace(". ", ".\n")
    targets = query.split("\n")

    log_str = []

    # list로 문장 번역
    for target in targets:
        trans = translator.translate(target, src="en", dest="ko")
        print("\n+---------------")
        log_str.append("\n+--------------")

        trans_target = ">>(" + target+ ")"        
        print(trans_target)
        log_str.append(trans_target)
        
        print(trans.text)
        log_str.append(trans.text)

    log_str = '\n'.join(log_str)
    _log_write_(log_str)

    print("end...")

