import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def main():
   f = open('facebook_sentences.txt', 'r')
   raw = f.read().strip()
   sentences = sent_tokenize(raw)
   print(sentences)
   print(len(sentences))
   f.close()
main()
