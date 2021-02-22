import re
import random

def read(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        return data

if __name__ == "__main__":
    o = read('../data/qaqc/train_5.txt')
    t = read('../data/temp/swe_train_5.txt')
    c = read('../data/swe_qaqc/swe_train_corrected.txt')

    for i, e in enumerate(o):
        o[i] = e.split(sep=' ', maxsplit=1)[1]

    assert(len(o) == len(t))
    assert(len(t) == len(c))

    output = []
    sep = ' // '

    for i in range(len(o)):
        if t[i] == c[i]:
            rest = t[i]
        else:
            rest = t[i] + c[i]

        s = o[i] + rest
        output.append(s)

    random.shuffle(output)

    pre_text = 'Original\nTranslated\nCorrected (if missing then translation was not corrected)\n'
    sep = '\n' + '*'*50 + '\n\n'
    
    with open('power_of_google_translate.txt', 'w') as f:
        f.write(pre_text)

        for e in output:
            f.write(sep)
            f.write(e)