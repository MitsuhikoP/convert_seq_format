#!/usr/bin/env python3
# copyright (c) 2019 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8

def CheckExt(ext):
    short_ext={
        "fa": "fasta",
        "fas": "fasta",
        "phy": "phylip",
        "nex": "nexus",
    }
    out_ext=ext
    if ext in short_ext:
        out_ext=short_ext[ext]
    return out_ext

def main():
    from Bio import SeqIO
    from Bio.Alphabet import IUPAC
    from argparse import ArgumentParser
    parser=ArgumentParser(description="",usage="python3 convert_seq_format.py -i input.phylip -o output.nexus", epilog="")
    parser.add_argument("-i",type=str,required=True, metavar="str",help="input file.")
    parser.add_argument("-o",type=str,required=True, metavar="str",help="output file.")
    args = parser.parse_args()

    in_format=args.i.split(".")[-1]
    out_format=args.o.split(".")[-1]
    in_format=CheckExt(in_format)
    out_format=CheckExt(out_format)

    print("convert from", in_format, "to", out_format)
    
    SeqIO.convert(args.i,in_format, args.o, out_format,alphabet=IUPAC.ambiguous_dna)

    
if __name__ == '__main__': main()
