FRAG_SNP_calling
================

Organism: *Arabidopsis thaliana*

**Requirements:**

(a) Python, samtools, ref genome (TAIR10 in this case)

(b) Aligned sam files to reference genome:
  - parent A
  - parent B
  - F1 hybrid of parent A x B

(c) Aligned sam files of plants of interest

**Important to note that:**

(a) Having good coverage for SNP list generation in Part A is crucial. Can combine reads from multiple individuals that are 100% of parent A/B or the 50% F1 hybrid to maximize SNP discovery.

(b) Variability between descendants of the various ecotypes mean that the 'Col-0' you used may be different from the reference genome, so I do find that re-sequencing the parental lines used in each experiment is crucial as well.

----------------

Part A. Generating SNP list
===========================

I. Convert uniquely mapping reads to bam
----------------------------------------

After mapping reads to reference genome, get unique reads (XT:A:U) from the sam file, covert to bam and make the sorted file using this python script:

        batch-sam-to-bam-uniquereads.py

This generates a folder with the unique, sorted bam files

II. Convert bam to mpileup and parse the pileup file
----------------------------------------------------



III. Find SNPs from the parsed pileup file
------------------------------------------


Part B. Generating SNP plots for individuals
============================================
