import nltk

text2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> DT NOM | DT NN
NOM -> ADJ NOM | ADJ NN | ADJ ADJ NN
VP -> VB PP Conj VP | VB RB
PP -> IN NP
DT -> 'the'
Conj -> 'and'
NN -> 'dog' | 'cat'
ADJ -> 'big' | 'black' | 'white'
RB -> 'away'
IN -> 'at'
VB -> 'barked' | 'chased'
""")
text1 = nltk.tokenize.word_tokenize("the big black dog barked at the white cat and chased away")
print(text1)
print()
parser = nltk.ChartParser(text2)
for tree in parser.parse(text1):
    print(tree)
    tree.pretty_print()