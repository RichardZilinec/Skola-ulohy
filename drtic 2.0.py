fr = open('subory/data.txt', 'r', encoding='utf8')
def is_cool (word):
    vowels = 'aeiouy'
    for vowel in vowels:
        if vowel in word:
            return False
    return True

words = 0
words_no_E = 0
cool_words = 0
for row in fr:
    row = row.strip()   #oddrbal som posledny enter
    words += 1
    if 'e' not in row:
       words_no_E += 1
    if is_cool(row) == True:
        cool_words +=1
        print(row)
print(words, words_no_E,cool_words)