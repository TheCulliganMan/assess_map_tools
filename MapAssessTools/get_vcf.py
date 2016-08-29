#!/usr/bin/env python
import subprocess as sp

def get_vcf(bamfile, ref, vcf):
    with open(vcf, 'w+') as output_handle:
        cmd = ['samtools', 'mpileup', '-C50' '-uf', ref, bam]
        sp.call(cmd, stdout=output_handle)
