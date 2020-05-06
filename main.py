import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet
String = open('Temp.txt', 'r').read()

#String = 'Hi this is Niranjan'
print(String)
Sentences = nltk.sent_tokenize(String)
Tokens = []
for Sent in Sentences:
    Tokens.append(nltk.word_tokenize(Sent)) 
Words_List = [nltk.pos_tag(Token) for Token in Tokens]

Nouns_List = []

for List in Words_List:
    for Word in List:
        if re.match('[NN.*]', Word[1]):
             Nouns_List.append(Word[0])

Names = []
for Nouns in Nouns_List:
    if not wordnet.synsets(Nouns):
        Names.append(Nouns)

print (Names)