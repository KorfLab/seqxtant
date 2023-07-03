SEQXTANT README
===============

`seqxtant` organizes related genomic sequences in order to study orthologs and
paralogs in greater detail.

## Overview ##

+ Install `blast-legacy` via bioconda
+ Get `grimoire` from KorfLab GitHub
+ Get `seqxtant` from KorfLab GitHub
+ Create a directory where you want to store the seqxtant database files
+ Point `SEQXTANT` to the database directory or use the `--env` option
+ Download genomic fasta, masked, and gff3 files for your favorite genomes
	+ Possible custom post-processing required here
+ Use `seqxtant create` to make a new database
+ Use `seqxtant add` to add fasta and gff files to database
+ Use `seqstant validate` to check overall genome stats
+ Use `seqxtant cluster` to cluster related sequences...

## Dev Notes ##

Some clades for testing

+ worms (705M)
	+ C. angaria
	+ C. brenneri
	+ C. briggsae
	+ C. elegans
	+ C. japonica
	+ C. remanei
	+ C. tropicalis
+ plants
+ flies