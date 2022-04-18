import sys
import re

# first read in all the input and replace the delimiter
# with a standard one
inp = sys.stdin.read()
inp = re.sub('\n[—-]+\n?', '\n----------\n', inp)


block_id = 1
sent_id = 1

# for each of the blocks in the input, where a block is 
# two lines:
#  1. date
#  2. one or more sentences
for block in inp.split('----------'):
	# strip off extra whitespace and split the lines on newline
	# then lines[0] should be the date and lines[1] should be the 
	# sentence(s)
	lines = block.strip().split('\n')

	#print('>>', lines)

	# keep a track of the date
	date = lines[0]

	# define a new function called "segment" that takes a single argument, line
	def segment(line):
                outp = line
		# replace any number of sequential ! ? or . with that 
		# and a newline
                outp = re.sub('([!.?]+)', '\g<1>\n', outp)
                outp = re.sub('([!.?]+)\n"', '\g<1>"\n', outp)
                outp = re.sub('(["]+)',' " ', outp)
                outp = re.sub('([ ]+)', ' ', outp)
		# ['káyi Kapampángán nómang Gen Z déng tútúlak kang Bongbong kéti...', ' dána...', ' bísá lá mú yátang live Sábung ding alti...', '']
                outp = re.sub('([!.?]+)\n( *dána)([!.?]+)\n', '\g<1>\g<2>\g<3>', outp)
		# split the string on newlines to get the list of sentences
                return outp.split('\n')

	# a function to tokenise sentences into tokens
	# for example "This is a test." -> ["This", "is", "a", "test", "."]
	def tokenise(sent):
                outp = sent
		# add spaces around punctuation characters
                outp = re.sub('([!.?:]+)', ' \g<1> ', outp)
                outp = re.sub('(,)', ' \g<1> ', outp)
		# replace multiple spaces
                outp = re.sub('  *', ' ', outp)
		# remove spaces at the beginning and end
                outp = outp.strip()
                return outp.split(' ')

	# next, for each of the sentences in the line. for this we need
	# a tokenisation function.
	sents = segment(lines[1])

	for sent in sents:
		if sent.strip() == '':
			continue

		print('# sent_id = facebook:%d:%d' % (block_id, sent_id))
		print('# text = %s' % sent)	
		print('# date = %s' % date)	

		tokens = tokenise(sent)
		for (i, token) in enumerate(tokens):
			print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (i+1, token))
	
		sent_id += 1
		
		print('')
	
	block_id += 1
