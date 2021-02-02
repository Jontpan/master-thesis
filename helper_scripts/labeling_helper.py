import sys


def read(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        return data

def get_current_line(target):
    try:
        with open(target) as f:
            return len(f.readlines())
    except IOError:
        return 0

def labeler(filename, q, a, count):
    assert(len(q) == len(a))

    with open(filename, 'a') as f:
        for i in range(count, len(q)):
            print('Count: {} out of {}\n'.format(i+1, len(q)))
            print('Question: ', q[i])
            print('Answer:', a[i])

            x = input()
            f.write(x + '\n')
            f.flush()

            print()
            print('*'*50)

if __name__ == "__main__":
    q = read('../data/temp/swe_q')
    a = read('../data/temp/swe_a')
    count = get_current_line('qa_labels.txt')

    labeler('qa_labels.txt', q, a, count)
