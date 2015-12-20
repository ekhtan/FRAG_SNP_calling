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

        run-mpileup.py -r ~ekhtan/genomes/TAIR10_all.fas -o [pileupfile.txt] -s /software/samtools/0.1.19/x86_64-linux-ubuntu14.04/bin/samtools
        
        beta-mpileup-parser.py -t 16 -f [pileupfile.txt]
        

III. Find SNPs from the parsed pileup file
------------------------------------------

        Colsomething_SNPFinder.py parsed_mpileup_SNP[ecotype].txt

This will generate a SNP list file call *Colother_SNPs.txt* file that can be used for the steps below.

Part B. Generating SNP plots for individuals
============================================

Have all the sam files of samples in the same folder. First two steps is the same as above.

I. Convert uniquely mapping reads to bam
----------------------------------------

After mapping reads to reference genome, get unique reads (XT:A:U) from the sam file, covert to bam and make the sorted file using this python script:

        batch-sam-to-bam-uniquereads.py

This generates a folder with the unique, sorted bam files

II. Convert bam to mpileup and parse the pileup file
----------------------------------------------------

        run-mpileup.py -r ~ekhtan/genomes/TAIR10_all.fas -o [pileupfile.txt] -s /software/samtools/0.1.19/x86_64-linux-ubuntu14.04/bin/samtools
        
        beta-mpileup-parser.py -t 16 -f [pileupfile.txt]
        

III. Call alleles at each position and bin the counts 
-----------------------------------------------------

You will need the SNP list from **Part A**.

        CallAllelesCol_Other.py [parsed_mpileupfile.txt] [output.txt] [SNP_file.txt]
        
        bin-by-genotype [alleles] [output.txt] [binsize in bp]
        
        rows2columns.pl [input.txt] > [output.txt]
        

Plot the columns on JMP.
