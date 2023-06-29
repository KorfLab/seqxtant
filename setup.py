import argparse
import os
import re
import shutil

# CLI
parser = argparse.ArgumentParser(description='seqxtant database setup')
parser.add_argument('dir', type=str, help='path to Phytozome directory')
arg = parser.parse_args()

# Get the genomes in the current build directory
genomes = []
for root, dirs, files in os.walk('build'):
	for name in files:
		m = re.search('(.+).readme.txt', name)
		if m: genomes.append(m.group(1))

# Add new genomes as necessary
for root, dirs, files in os.walk(arg.dir):
	for filename in files:
		found = False
		for genome in genomes:
			if re.match(genome, filename):
				found = True
				break
		if found: pass # print('found', genome, 'in', filename)
		else: print('this not found', filename)
"""
		m = re.search('(.+).readme.txt', name)
		if m: genomes.append(m.group(1))
		src = os.path.join(root, name)
		dst = f'build/{name}'
		shutil.copy(src, dst)
"""
