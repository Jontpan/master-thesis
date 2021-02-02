import numpy as np
import re
import sys
import readline


def read(eng, swe):
    e = open(eng)
    s = open(swe)

    eng_text = e.readlines()
    swe_text = s.readlines()

    labels = []

    e.close()
    s.close()

    for i, q in enumerate(eng_text):
        q_both = q.split(' ', 1)
        labels.append(q_both[0])
        q = re.sub(r'\n', '', q_both[1])
        q = re.sub(r'`', '\'', q)
        q = re.sub(r'\'\'', '\"', q)
        q = re.sub(r'\s([?!.\',])', r'\1', q) 
        eng_text[i] = q
        swe_text[i] = re.sub(r'\n', '', swe_text[i])
        swe_text[i] = re.sub(r'(&quot;)', '\"', swe_text[i])
        swe_text[i] = re.sub(r'(&#39;)', '\'', swe_text[i])
    
    return swe_text, eng_text, labels

def get_current_line(target):
    try:
        with open(target) as f:
            return len(f.readlines())
    except IOError:
        return 0

def correct(swe, eng, filename, count, labels):
    assert(len(swe) == len(eng))
    assert(len(swe) == len(labels))

    with open(filename, 'a') as f:
        for i in range(count, len(swe)):
            print('Count: {} out of {}\n'.format(i+1, len(swe)))
            print('Label: ', labels[i])
            print(eng[i])

            readline.set_startup_hook(lambda: readline.insert_text(swe[i]))
            try:
                text = input()
                f.write(text)
                f.write('\n')
                f.flush()
            finally:
                readline.set_startup_hook()
            
            print()
            print('*'*50)




if __name__ == "__main__":
    swe, eng, labels = read(sys.argv[1], sys.argv[2])
    count = get_current_line(sys.argv[3])

    correct(swe, eng, sys.argv[3], count, labels)

    print()
    print('You\'re finished!')

    
