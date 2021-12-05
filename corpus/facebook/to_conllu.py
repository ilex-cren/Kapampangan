from nltk.tokenize import sent_tokenize, word_tokenize
f = open("sentences_no_duplicates.txt", 'r')
g = open("facebook.conllu", 'a')
raw = f.read().strip()
sents = sent_tokenize(raw)
for sent in sents:
   g.write('# sent_id = facebook:\n# text = {}\n# text[eng] =\n# labels =\n'.format(sent))
   lines = []
   for i in range(len(word_tokenize(sent))):
     number = str(i+1)
     word = word_tokenize(sent)[i]
     line = number + '\t' + word + 8 * ('\t' + '_')
     lines.append(line)
     lines.append('\n')
   g.writelines(lines) 
   g.write('\n')

f.close()
g.close()


