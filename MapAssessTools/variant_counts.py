#!/usr/bin/env python
import subprocess as sp

def grep_command(input_file):
    """ Returns a grep command """
    cmd = [
        "grep", "-c",
        "-v", '"^#"', input_file,
    ]
    return cmd

def count_variants(input_file, output_file):
    """ counts the number of variants in a vcf """
    with open(output_file, "w+") as output_handle:
        status = sp.call(grep, stdout=output_handle)
    return status
