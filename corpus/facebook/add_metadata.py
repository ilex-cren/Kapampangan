# add metadata to facebook_sentences.txt.conllu
import csv

def get_text(sent):
   sentence = ''
   columns = csv.reader(sent, delimiter='\t')
   for word in columns[1]:
      sentence += ' '
      sentence += word
      
f1 = open('facebook_sentences.txt.conllu', 'r')
f2 = open('facebook.conllu', 'w')

metadata = '\n# sent_id =\n# text ={}\n# text[eng] =\n# labels ='
lines = f1.read().split('\n\n')

for line in lines:
   print(metadata.format(get_text(line)))
   print(line)

f1.close()
f2.close()

