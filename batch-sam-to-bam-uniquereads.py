#! /usr/bin/env python

# Han Tan
# UC Davis
# October 2013

# Takes .sam files, filters for reads that align uniquely to
# the genome, converts this to .bam and created the .sorted.bam
# file to be used for SNP calling

# Usage batch-sam-to-bam-uniquereads.py

import os, sys, math

li = os.listdir(os.getcwd())
print li
todo = filter(lambda x: x[-4:] == '.sam', li)
todo.sort()
print todo

pathSam = "/usr/bin/"

# Prepare result directories
li = os.listdir(os.getcwd())
dirs = ['BAM_files']
if False in list((x in li for x in dirs)):
	os.system("mkdir BAM_files")

# Read into each .sam file
# Filter for uniquely matching reads, convert to .bam
# and sorts this .bam file to make the _aln.sorted.bam files

for file in todo:
	print file
	name = file.split('.')[0]
	sam = open(file)
	f = open(name+"_unique.sam",'w')
	
	while True:
		line = sam.readline()
		if line == '':
			break
		if line[0] == '@':
			f.write(line)
		else:
			l = line.split()
			if len(l) > 13:
				if l[11][5] == 'U':
					f.write(line)
				
	f.close()
    
	os.system(pathSam+"samtools view -bS "+name+"_unique.sam"+" > "+name+"_aln.bam")
	os.system(pathSam+"samtools sort "+name+"_aln.bam"+" "+name+"_aln.sorted")
	os.system("rm -f "+name+"_aln.bam")        	
	os.system("rm -f "+name+"_unique.sam")
	
os.system("mv *.bam BAM_files/")
