# add metadata to facebook_sentences.conllu

f = open('facebook_sentences.conllu', 'r')
metadata = '\n# sent_id =\n# text ={}\n# text[eng] =\n# labels ='

# read lines from facebook_sentences.conllu

# if line begins with 1, insert metadata above it
#   - text = words from column 2 in sentence form
#   - text[eng] leave blank for now
#   - labels blank for now?

f.close()
