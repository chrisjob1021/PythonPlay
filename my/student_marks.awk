BEGIN {
	max = 0
}
{
	for (i=3; i<=NF; i++) {
		line[$1] += $i 
	}
	if (NF>max) {
		max = NF
	}
}
END {
	for (i in line) {
		printf "%s %.0f\n", i, line[i]/(max-2)
	}
}