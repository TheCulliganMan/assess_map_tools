#!/usr/bin/env python

import os
import MapAssessTools

bamdir = os.getcwd()
bamfiles = [i for i in os.listdir(bamdir) if i.endswith("bam")]
ref_file = [i for i in os.listdir(fadir) if i.endswith(".fa") or i.endswith('.fasta')][0]

for bamfile in bamfiles:
    base = os.path.basename(bamfile).rsplit('.', 1)[0]
    vcf = base + ".vcf"
    variant_count = base + ".variant_count.txt"
    average_cov = base + ".avarage_cov.txt"
    mapped_reads = base + ".mapped_reads.txt"
    MapAssessTools.get_vcf(bamfile, ref_file, vcf)
    MapAssessTools.count_mapped_reads(bamfile, mapped_reads)
    MapAssessTools.count_variants(bamfile, variant_count)
    MapAssessTools.calculate_average_coverage(bamfile, average_cov)
