
with open("Data_2.txt", 'r') as file:
    sentence = file.read()
    
print(sentence)
print()
#NLTK POS Tagger
# https://www.educba.com/nltk-pos-tag/
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
py_sword = set(stopwords.words('english'))
py_token = sent_tokenize(sentence)
print("NLTK POS Tagger:")
for i in py_token:
    py_lword = nltk.word_tokenize(i)
    # py_lword = [w for w in py_lword if not w in py_sword]
    py_tag = nltk.pos_tag(py_lword)
    print(py_tag)


# textblob POS tagger
# https://www.geeksforgeeks.org/python-part-of-speech-tagging-using-textblob/
from textblob import TextBlob

print()
print('TextBlob POS Tagger:')
blob_object = TextBlob(sentence)
print(blob_object.tags)

# Regular Expression tagger
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

print()
print("Regex Tagger:")
patterns = [
    (r'.*ing$', 'VBG'),             
    (r'.*ed$', 'VBD'),              
    (r'.*es$', 'VBZ'),              
    (r'.*ould$', 'MD'),             
    (r'.*\'s$', 'NN$'),             
    (r'.*s$', 'NNS'),               
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'^\d+$', 'CD'),               
    (r'.*ing$', 'VBG'),             
    (r'.*ment$', 'NN'),             
    (r'.*ful$', 'JJ'),
    (r'\b(?:and)\b', 'CC'),
    (r'\b(?:away)\b', 'RB'),
    (r'(The|the|A|a|An|an)$', 'AT'),
    (r'\b(?:big|black|white)\b', 'JJ'),
    (r'\b(?:at)\b', 'IN'),
    (r'\.$', 'PUN'),
    (r'.*', 'NN'),
]


tagger = nltk.tag.sequential.RegexpTagger(patterns)

tokenized_text = word_tokenize(sentence)
print(tagger.tag(tokenized_text))