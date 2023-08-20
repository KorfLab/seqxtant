SEQXTANT README
===============

`seqxtant` organizes related genomic sequences in order to study orthologs and
paralogs in greater detail.

## Overview ##

+ Install `ab-blast` via https://www.advbiocomp.com personal license
+ Get `grimoire` from KorfLab GitHub
+ Get `seqxtant` from KorfLab GitHub
+ Create a directory where you want to store the seqxtant database files
+ Point `SEQXTANT` to the database directory or use the `--env` option
+ Download genomic fasta, masked, and gff3 files for your favorite genomes
+ Use `seqxtant create` to make a new database
+ Use `seqxtant add` to add fasta and gff files to database
+ Use `seqxtant status` to get information about the database
+ Use `seqstant validate` to check overall genome stats
+ Use `seqxtant cluster` to cluster related sequences...

## Database ##

The "database" is a file called `seqxtant.json` that lives inside a directory
that is either specified by an environment variable or passed in with the
`--env` option. Probably should be a sqlite database...

## Fasta and GFF3 ##

GFF isn't actually used yet. The only thing that will be required someday will
be the genes, so very large files should be filtered.

## Dev Notes ##

Some clades used for testing

+ worms
	+ C. angaria
	+ C. brenneri
	+ C. briggsae
	+ C. elegans
	+ C. japonica
	+ C. remanei
	+ C. tropicalis
+ plants
+ flies