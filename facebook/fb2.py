# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore


# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

import math

dinos = { }
g = 9.8

with open('dataset2.csv') as f:
	for line in f:
		if 'bipedal' in line:
			s = line.split(',')
			dinos[s[0]] = { }
			dinos[s[0]]['stride_length'] = float(s[1])

with open('dataset1.csv') as f:
	for line in f:
		s = line.split(',')
		if s[0] in dinos:
			dinos[s[0]]['speed'] = ((dinos[s[0]]['stride_length'] / float(s[1])) - 1) * math.sqrt(float(s[1]) * g)

def sortDict(key):
	if 'speed' in dinos[key]:
		return dinos[key]['speed']

print sorted(dinos, key=sortDict, reverse=True)


