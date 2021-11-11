import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def main():
   f = open('facebook_sentences.txt', 'r')
   raw = f.read().strip()
   sentences = sent_tokenize(raw)
   rem_dup = []
   [rem_dup.append(s) for s in sentences if s not in rem_dup]
   output = open('sentences_no_duplicates.txt', 'w')
   [output.write(s) for s in rem_dup]
   print("Sentences: ", len(sentences))
   print("Unique Sentences: ", len(rem_dup))
   print("Tokens: ", len(word_tokenize(raw)))
   print("Types: ", len(sorted(set(word_tokenize(raw)))))
   f.close()
main()
