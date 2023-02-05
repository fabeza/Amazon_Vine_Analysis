import nltk
from nltk import word_tokenize
text = word_tokenize("I like lychee bubble tea")
output = nltk.pos_tag(text)
print(output)
