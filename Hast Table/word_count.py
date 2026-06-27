
word_count = {}
with open('Hast Table/poem.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        token = line.strip().split(' ')
        for word in token:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
    print(word_count)