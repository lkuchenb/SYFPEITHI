# SYFPEITHI command line interface

## Installation

1. Create a **Python 2.7** vitual environment and install [Fred-2](https://github.com/FRED-2/Fred2). For this instructions, we assume the location of this virtual environment to be `/usr/local/lib/fred-2.venv`.
1. Copy `syfpeithi.py` to `/usr/local/lib`
1. Copy `syfpeithi` to `/usr/local/bin`

For setups with alternative paths for the virtual environment or python script, adjust the content of the `syfpeithi` file accordingly.

## Usage

Give a plain text file with peptides and a list of candidate HLA alleles, a table with four columns representing

* The peptide sequence
* The HLA allele
* The raw SYFPEITHI score
* The normalized SYFPEITHI score [0..1]

can be obtained by invoking

```
$ syfpeithi -p /tmp/mypeptides 'HLA-A*11:01' 'HLA-A*02:01' | column -t -s'      '
Using TensorFlow backend.
Peptide      Allele       SyfpeithiRawScore  SyfpeithiNormScore
YSKNLVTE     HLA-A*11:01  NA                 NA
AYIPTNVI     HLA-A*11:01  NA                 NA
DRFQILTL     HLA-A*11:01  NA                 NA
YSKNLVTE     HLA-A*02:01  NA                 NA
AYIPTNVI     HLA-A*02:01  NA                 NA
DRFQILTL     HLA-A*02:01  NA                 NA
AVFDNLIQL    HLA-A*11:01  20                 0.588235294118
DRYISKMFL    HLA-A*11:01  0                  0.0
GVDLDQLLD    HLA-A*11:01  19                 0.558823529412
KPKAPPPSL    HLA-A*11:01  2                  0.0588235294118
LLDMSYEQL    HLA-A*11:01  6                  0.176470588235
SVAKTILKR    HLA-A*11:01  27                 0.794117647059
YEYQHSNLY    HLA-A*11:01  2                  0.0588235294118
AVFDNLIQL    HLA-A*02:01  22                 0.611111111111
DRYISKMFL    HLA-A*02:01  10                 0.277777777778
GVDLDQLLD    HLA-A*02:01  6                  0.166666666667
KPKAPPPSL    HLA-A*02:01  14                 0.388888888889
LLDMSYEQL    HLA-A*02:01  22                 0.611111111111
SVAKTILKR    HLA-A*02:01  15                 0.416666666667
YEYQHSNLY    HLA-A*02:01  4                  0.111111111111
AVTRLEGVDE   HLA-A*11:01  17                 0.515151515152
FRQGTPLIAF   HLA-A*11:01  5                  0.151515151515
KCDIDIRKDL   HLA-A*11:01  0                  0.0
PGGVYATRSS   HLA-A*11:01  1                  0.030303030303
QQSISDAEQR   HLA-A*11:01  9                  0.272727272727
SLAPNIISQL   HLA-A*11:01  12                 0.363636363636
SSDPASQLSY   HLA-A*11:01  18                 0.545454545455
VIADGGIQNV   HLA-A*11:01  10                 0.30303030303
AVTRLEGVDE   HLA-A*02:01  7                  0.205882352941
FRQGTPLIAF   HLA-A*02:01  8                  0.235294117647
KCDIDIRKDL   HLA-A*02:01  10                 0.294117647059
PGGVYATRSS   HLA-A*02:01  -1                 -0.0294117647059
QQSISDAEQR   HLA-A*02:01  0                  0.0
SLAPNIISQL   HLA-A*02:01  30                 0.882352941176
SSDPASQLSY   HLA-A*02:01  7                  0.205882352941
VIADGGIQNV   HLA-A*02:01  26                 0.764705882353
QDATAEEEGEF  HLA-A*11:01  NA                 NA
KSGVDADSSYF  HLA-A*11:01  NA                 NA
QDATAEEEGEF  HLA-A*02:01  NA                 NA
KSGVDADSSYF  HLA-A*02:01  NA                 NA
```
