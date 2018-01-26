# DNA_Analyzer
Python program to analyze DNA knock-out screens

The goal of the program is to read in fastq files, check if the target sequence is in the screening library, and compile a dataframe of hit counts.

The next step is too compare the background screen with a targeted screen to measure relative enrichment. This will be done using MAGeCK (https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0554-4).

Using GeckoV2 A+B screening libraries (http://www.nature.com.proxy.lib.fsu.edu/articles/nmeth.3047)
