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


if __name__ == '__main__':
    str_=_file_()
    query = str_.replace(". ", ".\n")
    
    # 엔터 제거
    targets = query.split("\n")
    
        
    print(targets)