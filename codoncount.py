import re 
import sys
from Bio import SeqIO

nucleotide_count1 = {}

fastq_file = sys.argv[1]

for record in SeqIO.parse(fastq_file, "fastq"):
	sequence = record.seq
	codon = sequence[0:3]
	current_count = nucleotide_count1.get(codon,0)
	new_count = current_count + 1
	nucleotide_count1[codon] = new_count


for codon, count in nucleotide_count1.items():
	print(codon + " : " + str(count) + ",")

