import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def main():
   f = open('facebook_sentences.txt', 'r')
   raw = f.read().strip()
   sentences = sent_tokenize(raw)
   print("Sentences: ", len(sentences))
   print("Tokens: ", len(word_tokenize(raw)))
   print("Types: ", len(sorted(set(word_tokenize(raw)))))
   f.close()
main()
