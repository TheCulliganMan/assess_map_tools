#!/usr/bin/env python
import subprocess as sp

def samtools_view_cmd(input_file):
    ''' returns a samtools view command '''
    cmd = [
        "samtools", "view",
        "-F", "0x40", input_file,
    ]
    return cmd

def count_mapped_reads(input_file, output_file):
    ''' counts the number of mapped reads in a bamfile '''
    samtools_cmd = samtools_view_cmd(input_file)
    cut_cmd = ['cut', '-f1']
    sort_cmd = ['sort']
    wc_cmd = ['wc', '-l']

    with open(output_file, "w+") as output_handle:
        p1 = sp.Popen(samtools_cmd, stdout=sp.PIPE)
        p2 = sp.Popen(cut_cmd, stdin=p1.stdout, stdout=sp.PIPE)
        p3 = sp.Popen(sort_cmd, stdin=p2.stdout, stdout=sp.PIPE)
        p4 = sp.Popen(wc_cmd, stdin=p3.stdout, stdout=output_handle)
        p4.communicate()

    return True
