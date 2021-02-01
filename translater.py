from google.cloud import translate_v2 as translate
import numpy as np
import sys
import re
from tqdm import tqdm

def read(filename):
    f = open(filename)

    try:
        text = f.readlines()
    finally:    
        f.close()
        
    return text
        

def clean_text(text):
    for i, q in enumerate(text):
        q = re.sub(r'\n', '', q)
        q = re.sub(r'`', '\'', q)
        q = re.sub(r'\'\'', '"', q)
        q = re.sub(r'\s([?!.\',])', r'\1', q) 
        text[i] = q

def split_text(text):
    labels = []
    data = []

    for sentence in text:
        split_sentence = sentence.split(" ", 1)
        labels.append(split_sentence[0])
        data.append(split_sentence[1])

    return labels, data


def translate_text(text):
    translate_client = translate.Client(target_language='swe')
    result = translate_client.translate(text, source_language='en')

    return result

def write(filename, text):
    with open(filename, 'w') as f:
        for s in text:
            f.write(s + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify filename")
        exit()
    
    text = read(sys.argv[1])
    labels, data = split_text(text)
    clean_text(data)

    swe_data = []
    for s in tqdm(data):
        trans_text = (translate_text(s))
        swe_data.append(trans_text["translatedText"])
    
    labels_filename = "labels_swe_" + sys.argv[1]
    data_filename = "swe_" + sys.argv[1]

    np.savetxt(labels_filename, np.array(labels), delimiter='\n', fmt='%s')
    np.savetxt(data_filename, np.array(swe_data), delimiter='\n', fmt='%s')
    


