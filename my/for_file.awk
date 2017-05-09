{
	for (i=1; i<=NF; i++) {
		if (line[i] == "") {
			line[i] = $i
		}
		else {
			line[i] = line[i]" "$i
		}
	}
}
END {
	for (i in line) {
		print line[i]
	}
}