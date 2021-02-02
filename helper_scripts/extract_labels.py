import sys


labels = []
with open(sys.argv[1], 'r') as f:
    text = f.readlines()

    for line in text:
        labels.append(line.split(" ", 1)[0])

labelset = set(labels)
labels = list(labelset)
labels.sort()

with open('labels.txt', 'w') as f:
    for label in labels:
        f.write(label + '\n')


        


