use strict;
use warnings;

foreach my $file (`ls AT*/summary.txt`) {
	chomp $file;
	my $at = 0;
	my %og = (
		'A.thaliana' => 0,
		'O.sativa' => 0,
		'P.vulgaris' => 0,
		'S.lycopersicum' => 0,
		'V.vinifera' => 0,
	);
	 for (`cut -f 2 $file | sort | uniq -c`) {
	 	my ($count, $genome) = split;
	 	$og{$genome} = $count;
	}
	my ($geneloc) = $file =~ /^(.+)\/summary/;
	print "$geneloc";
	foreach my $genome (sort keys %og) {
		print "\t$og{$genome}";
	}
	print "\n";
}