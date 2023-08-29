#!/usr/bin/env python3

import argparse
import json
import subprocess

parser = argparse.ArgumentParser(description='Brief description of program')
parser.add_argument('-q', type=str, help='set path to query sequence')
parser.add_argument('-e', type=str, help='set environment/database path')
parser.add_argument('-o', type=str, help='set output directory')
parser.add_argument('-d', type=str, default=True, 
	help='delete all produced files')
parser.add_argument('--verbose', action='store_true',
	help='see behind the scenes messages')
arg = parser.parse_args()

def run(arg, cmd):
	if arg.verbose: print(cmd, file=sys.stderr, end=' ...')
	ret = subprocess.run(cmd, shell=True).returncode
	if ret != 0:
		raise Exception(f'{cmd} failed with status {ret}')
	if arg.verbose: print(f' done', file=sys.stderr)
	

def mk_gff(arg, env):
	run(arg, f'touch {env}/eie_cp.gff3')

def seqxtant_add(arg):
	params = (
		f"seqxtant --env {arg.e} add",
		f"--fasta {arg.q}",
		f"--gff3 {arg.e}/eie_cp.gff3",
		f"--genome eie"
	)
	cmd = ' '.join(params)
	run(arg, cmd)

def seqxtant_cluster(arg, env, odir):
	f = open(f'{env}/eie.fa')
	intron_lens = []
	full_lens = []
	full_len = 0
	
	# read seq
	while True:
		l = f.readline()
		l = l.rstrip()
		if l.startswith('>'): 
			intron_len = 0
			full_lens += [full_len]
		elif l.islower(): 
			intron_len = len(l)
			intron_lens += [intron_len]
		elif l.isupper():
			full_len = intron_len + len(l)
		elif l == '': 
			full_lens = full_lens[1:] + [full_len]
			break


	for i in range(len(full_lens)):
		params = (
			f'seqxtant --env {env} cluster',
			f'--genome eie',
			f'--location eie-{i}:1-{full_lens[i]}',
			f'--odir {arg.o}/eie-{i}'
		)
		cmd = ' '.join(params) 
		run(arg, cmd)

		
def db_del(arg, env):
	run(arg, f'rm {env}/eie*')
	with open(f'{env}/seqxtant.json', 'r') as f:
		db = json.load(f)
		db['genomes'].remove('eie')
	with open(f'{env}/seqxtant.json', 'w') as f:
		f.write(json.dumps(db, indent=4))



mk_gff(arg, arg.e)
seqxtant_add(arg)
seqxtant_cluster(arg, arg.e, arg.o)
db_del(arg, arg.e)


