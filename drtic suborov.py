fr = open('subory/data.txt', 'r', encoding='utf8')
#citacia hlava sa nastavila na zaciatok
#1. sposob citania suboru
#for row in fr:
    #print (row)

#2. sposob
#jozo = fr.readlines()
#vytvorim list , ktoreho prvkami su cele riadky
#print (jozo)

#3.sposob
#first_line = fr.readline()
#print(first_line)

def is_cool (word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
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