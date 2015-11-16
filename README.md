FRAG_SNP_calling
================

Organism: *Arabidopsis thaliana*

Data Requirement:

        Aligned sam files to reference genome -
          100% of parent A
          100% of parent B
          F1 hybrid of parent A x B
          
        Aligned sam files of plants of interest
        

Important to note that: 

(a) Having good coverage for SNP list generation in Part A is crucial. Can combine reads from multiple individuals that are 100% of parent A/B or the 50% F1 hybrid to maximize SNP discovery.

(b) Variability between descendants of the various ecotypes mean that the 'Col-0' you used may be different from the reference genome, so I do find that re-sequencing the parental lines used in each experiment is crucial as well.

-----------------------------------

Part A. Generating SNP list
===========================

I. Convert uniquely mapping reads to bam
----------------------------------------



Part B. Generating SNP plots for individuals
============================================
