#!/usr/bin/env python
import subprocess as sp

def samtools_depth_cmd(input_file):
    cmd = [
        "samtools",
        "depth",
        input_file
    ]
    return cmd

def calculate_average_coverage(input_file, output_file):
    """ calculates average coverage """
    samtools_cmd = samtools_depth_cmd(input_file)
    awk_cmd = ['awk', "'"+'{sum+=$3; sumsq+=$3*$3} END { print Average = ",sum/NR; print "Stdev = ",sqrt(sumsq/NR - (sum/NR)*2)}'+"'"]


    with open(output_file, "w+") as output_handle:
        p1 = sp.Popen(samtools_cmd, stdout=sp.PIPE)
        p2 = sp.Popen(awk_cmd, stdin=p1.stdout, stdout=output_handle)
        p2.communicate()

    return True
