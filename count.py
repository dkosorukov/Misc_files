import collections


def count_unique_words(filename):
    # your code here 
    words = {}
    with open(filename, 'rt') as infile:
        for line in infile:
            normalized = line.split()
            for word in normalized:
                if word not in words:
                    words[word] = 0
                words[word] += 1    
    return words
    


if __name__ == '__main__':
    words = count_unique_words('IntermidiatePython/hamlet.txt')
    print(words['the'])
