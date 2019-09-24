#!/usr/bin/env python
#
# Copyright (c) 2019, University of Tuebingen
# Author: Leon Kuchenbecker
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright and
#       author notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the distribution.
#     * Neither the name of the University of Tuebingen nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import sys

from Fred2.Core import Allele, Peptide
from Fred2.EpitopePrediction import EpitopePredictorFactory

####################################################################################################

parser = argparse.ArgumentParser('SYFPEITHI')
parser.add_argument('-p', '--peptides', metavar='path', type = argparse.FileType('r'), default = sys.stdin, help = 'Path to peptide list. Default: stdin')
parser.add_argument('alleles', metavar='allele', nargs = '+',  type = str, help = 'HLA alleles to predict against.')
args = parser.parse_args()

####################################################################################################

# Convert raw peptide sequences to Fred2.Core.Peptide objects
all_peptides = [ Peptide(row.strip()) for row in args.peptides ]

# Separate peptides by length
peptides_by_length = {}
for peptide in all_peptides:
    if not len(peptide) in peptides_by_length:
        peptides_by_length[len(peptide)] = []
    peptides_by_length[len(peptide)].append(peptide)

# Convert raw allele strings to Fred2.Core.Allele objects
alleles =  [ Allele(allele) for allele in args.alleles ]

# Instatiate predictor
predictor = EpitopePredictorFactory("Syfpeithi")

def matrix_max(matrix):
    """Returns the maximum attainable score for a pssm"""
    return sum([ max(value.values()) for _, value in matrix.items() ])

def load_allele_model(allele, length):
    """Returns the SYFPEITHI pssm for a given allele"""
    allele_model = "%s_%i" % (allele, length)
    try:
        return matrix_max(getattr(__import__("Fred2.Data.pssms.syfpeithi" + ".mat." + allele_model, fromlist=[allele_model]), allele_model))
    except ImportError:
        return None

# Calculate the maximum attainable score for each allele
converted_alleles = dict(zip(alleles, predictor.convert_alleles(alleles)))
max_score_by_allele = {
        (allele, length) : load_allele_model(converted_alleles[allele], length) for length in predictor.supportedLength for allele in alleles
    }

# Run predictions and output results
print 'peptide_sequence\tallele\traw_score\tnorm_score'
for pep_len, peptides in peptides_by_length.items():
    for allele in alleles:
        if (allele, pep_len) in max_score_by_allele and max_score_by_allele[allele, pep_len]:
            results = predictor.predict(peptides, alleles = [allele])
            for index, row in results.iterrows():
                print '{}\t{}\t{}\t{}'.format(str(index[0]), allele, row[allele], float(row[allele])/max_score_by_allele[allele, pep_len])
        else:
            for peptide in peptides:
                print '{}\t{}\t{}\t{}'.format(peptide, allele, 'NA', 'NA')
