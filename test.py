# https://aclanthology.org/O89-1008.pdf
import nltk
from nltk.tokenize import RegexpTokenizer


with open("Data_2.txt", 'r') as file:
    sentence = file.read()

sentence_lower = sentence.lower()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(sentence_lower)

sentence_cleaned = ' '.join(tokens)

text2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> DT NOM | DT NN
NOM -> ADJ NOM | ADJ NN | ADJ ADJ NN
VP -> VP Conj VP | VB RB | VB PP
PP -> IN NP
DT -> 'the'
Conj -> 'and'
NN -> 'dog' | 'cat'
ADJ -> 'big' | 'black' | 'white'
RB -> 'away'
IN -> 'at'
VB -> 'barked' | 'chased'
""")
text1 = nltk.tokenize.word_tokenize(sentence_cleaned)
print(text1)
print()
parser = nltk.ChartParser(text2)
for tree in parser.parse(text1):
    print(tree)
    tree.pretty_print()