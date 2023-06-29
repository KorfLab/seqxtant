import argparse
import json
import os
import re
import shutil
import sys


def read_db(db):
	with open(db) as fp:
		return json.load(fp)

def write_db(db, d, state):
	d['state'] = state
	with open(db, 'w') as fp:
		fp.write(json.dumps(d, indent=4))

def create(arg, db):
	if os.path.isfile(db):
		raise Exception(f'seqxtant databse already exists at {db}')
	write_db(db, {'genomes':[]}, 'ready')

def status(arg, db):
	if not os.path.isfile(db):
		raise Exception(f'{db} is not a seqxtant database location')
	print(f'Data location: {db}')
	d = read_db(db)
	print(f'Database status: {d["state"]}')
	print(f'Genomes: {len(d["genomes"])}')
	
def add_genome(arg, db):
	d = read_db(db)
	if d['state'] == 'busy':
		raise Exception(f'cannot add genome, {db} is currently busy')
	
	write_db(db, d, 'busy')
	# copy files to build directory under new name
	# uncompress as necessary
	# make blast database
	# clean up
	# get proteins and transcripts?
	
	write_db(db, d, 'ready')

## CLI ##
parser = argparse.ArgumentParser(description='genomic homology multi-mapper')
parser.add_argument('--env', help='set data location instead of $SEQXTANT')
subparsers = parser.add_subparsers(required=True, help='sub-commands')

parse_status = subparsers.add_parser('status', help='db info')
parse_status.set_defaults(func=status)

parse_create = subparsers.add_parser('create', help='new database')
parse_create.set_defaults(func=create)

parse_add = subparsers.add_parser('add', help='add genome')
parse_add.add_argument('fasta', help='genome in fasta')
parse_add.add_argument('masked', help='hard-masked genome in fasta')
parse_add.add_argument('gff3', help='annotation in gff3')
parse_add.set_defaults(func=add_genome)

try:
	arg = parser.parse_args()
except:
	print('choose a sub-command, see --help')
	sys.exit(1)

## ENV ##
if arg.env: env = arg.env
else:       env = os.getenv('SEQXTANT')
if not env: raise Exception('you must set SEQXTANT or use --env option')
db = f'{env}/seqxtant.json'

## Run Subcommand ##
arg.func(arg, db)