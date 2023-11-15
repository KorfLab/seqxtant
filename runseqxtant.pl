use strict;
use warnings;

open(my $fh, "../imeter/eie.fa") or die;
while (<$fh>) {
	next unless /^>(\S+) Chr(\S+) (\S) (\S+) (\S+)\-(\S+) (\S+) (\S+)/;
	my $loc = $2;
	my $str = $3;
	my $gene = $4;
	my $beg = $5;
	my $odir = "$gene-$beg";
	print STDERR "$odir\n";
	`python3 seqxtant --env plants cluster --genome A.thaliana --location $2 --paralogs --odir $odir --cpus 4`;
}