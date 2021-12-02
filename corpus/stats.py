import sys
from pathlib import Path

def is_complete(tree):
	n_tokens = 0
	valid = True
	for line in tree.split('\n'):
#		print(line)
		#   0    1                2           3      4    5    6    7        8    9
		# ['8', 'nitzotzocotzi', 'tzocotzi', 'ADJ', '_', '_', '2', 'advcl', '_', '_']
		if line.strip() == '':
			continue
		row = line.split('\t')
		if '-' in row[0] or '.' in row[0]:
			continue
		if '#' in row[0]:
			continue
		if row[3] == '_' or row[6] == '_' or row[7] == '_':
			valid = False
		n_tokens += 1

	return (valid, n_tokens)

total_files = 0
complete_files = 0
total_trees = 0
total_tokens = 0
complete_trees = 0
complete_tokens = 0
total_trees_file = 0

if len(sys.argv) == 2:
	total_files = 1
	complete_trees_file = 0
	total_trees_file = 0
	for tree in open(sys.argv[1]).read().split('\n\n'):
		(valid, n_tokens) = is_complete(tree)
		if valid:
			complete_trees += 1
			complete_trees_file += 1
			complete_tokens += n_tokens
		else:
			print('%d\t%s' % (len([i for i in tree.split('\n') if '#' not in i]), tree.split('\n')[0]))

		total_trees += 1
		total_trees_file += 1
		total_tokens += n_tokens

	if complete_trees_file == total_trees_file:
		complete_files += 1

else:
	for path in Path('.', ".").glob('*.conllu'):
		complete_trees_file = 0	
		total_trees_file = 0	
		for tree in open(path).read().split('\n\n'):
			if tree.strip() == '':
				continue
			(valid, n_tokens) = is_complete(tree)
			if valid:
				complete_trees += 1
				complete_trees_file += 1
				complete_tokens += n_tokens
	
			total_trees += 1
			total_trees_file += 1
			total_tokens += n_tokens
	
		total_files += 1

		if complete_trees_file == total_trees_file:
			complete_files += 1
			print("complete: {}".format(path.name))

	
print('Files:  (%.2f%%) %d/%d' % ((complete_files/total_files)*100,complete_files, total_files))
print('Trees:  (%.2f%%) %d/%d' % ((complete_trees/total_trees)*100, complete_trees, total_trees))
print('Tokens: (%.2f%%) %d/%d' % ((complete_tokens/total_tokens)*100, complete_tokens, total_tokens))
