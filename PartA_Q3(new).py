import nltk
from nltk import pos_tag, RegexpParser
from textblob import TextBlob

with open("Data_2.txt", 'r') as file:
    sentence = file.read()
    
print(sentence)

# NLTK POS tagging
# https://www.educba.com/nltk-pos-tag/
nltk_tags = pos_tag(nltk.word_tokenize(sentence))

# TextBlob POS tagging
# https://www.geeksforgeeks.org/python-part-of-speech-tagging-using-textblob/
textblob_tags = TextBlob(sentence).tags

# Regular Expression tagging
# https://tedboy.github.io/nlps/generated/generated/nltk.RegexpParser.html
regex_pattern = r'NP: {<DT>?<JJ>*<NN>}'  # Define a simple NP (noun phrase) pattern
regex_parser = RegexpParser(regex_pattern)
regex_tags = regex_parser.parse(nltk_tags)



print("NLTK POS tagging:")
print(nltk_tags)

print("\nTextBlob POS tagging:")
print(textblob_tags)

print("\nRegular Expression tagging:")
print(regex_tags)
