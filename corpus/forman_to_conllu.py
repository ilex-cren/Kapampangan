import re
f = open("forman.txt", 'r')
items = re.split(r'\s*\n\s*\n\s*',f.read()) 
for item in items:
   print('# sent_id = grammar:')
   split_pam = item.split('\n')
   pam = split_pam[0]
   print('# text =', pam)
   rest = split_pam[1]
   page = re.search('\d+', rest)
   eng = re.sub('\(\d+\)', '', rest)
   q = {'‘':'', '.’':'.'}
   for i,j in q.items():
      eng = eng.replace(i, j)
   print('# text[eng] =', eng)
   print('# labels = forman:71:', page.group(), sep='')
   print('\n')
f.close()


