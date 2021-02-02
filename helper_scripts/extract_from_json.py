import json
import sys
import re

def read(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data

def extract_qa(data):
    q = []
    a = []

    for p in data["data"]:
        q.append(p["question"])

        for choice in p["choices"]:
            if choice["type"] == "Correct answer":
                a.append(choice["text"])
                break

    assert(len(q) == len(a))
    return q, a

def write(filename, data):
    with open(filename, 'a') as f:
        for d in data:
            d = re.sub(r'\n', '', d)
            f.write(d + '\n')

if __name__ == "__main__":
    data = read(sys.argv[1])
    q, a = extract_qa(data)
    write('swe_q', q)
    write('swe_a', a)
