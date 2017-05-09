{
	for(i=3; i<=NF; i++) {
		tests[i] += $i
	}
}
END {
	for(i in tests) {
		print "test"i-2, tests[i]/NR
	}
}
