# SNP-Comparison
SNP Comparison Project for Bioinformatics 527

This script compares the SNPs present in two VCF files. The output will give information on the overall number of SNPs, number of SNPs that are present in both files, and a comparison of the genotypes of those SNPs. 

VCF Format Requirement
If the two VCF files are not formatted the same way for genotype, formatter.py can be used. 

Usage

vcf_comparator.py <File1><File2> > output.txt

formatter.py <File> <Output.vcf>
