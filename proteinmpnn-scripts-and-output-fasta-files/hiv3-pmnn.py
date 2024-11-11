#!/usr/bin/env python3

import requests
import os
import json
from pathlib import Path

def get_api_key():
    return os.getenv("NVCF_RUN_KEY") or input("Paste the Run Key: ")

def get_pdb_content():
    return """
ATOM      1  N   GLY A   1      29.975 -17.618   6.944  1.00  0.00
ATOM      2  CA  GLY A   1      30.876 -17.198   5.877  1.00  0.00
ATOM      3  C   GLY A   1      30.353 -15.953   5.172  1.00  0.00
ATOM      4  O   GLY A   1      29.159 -15.842   4.894  1.00  0.00
ATOM      5  N   GLY A   2      31.135 -14.984   5.093  1.00  0.00
ATOM      6  CA  GLY A   2      30.707 -13.762   4.422  1.00  0.00
ATOM      7  C   GLY A   2      30.602 -13.967   2.916  1.00  0.00
ATOM      8  O   GLY A   2      29.735 -13.390   2.260  1.00  0.00
ATOM      9  N   GLY A   3      31.344 -14.871   2.387  1.00  0.00
ATOM     10  CA  GLY A   3      31.279 -15.189   0.966  1.00  0.00
ATOM     11  C   GLY A   3      29.906 -15.727   0.584  1.00  0.00
ATOM     12  O   GLY A   3      29.375 -15.402  -0.478  1.00  0.00
ATOM     13  N   GLY A   4      29.369 -16.573   1.434  1.00  0.00
ATOM     14  CA  GLY A   4      28.032 -17.106   1.202  1.00  0.00
ATOM     15  C   GLY A   4      26.987 -15.998   1.214  1.00  0.00
ATOM     16  O   GLY A   4      26.071 -15.987   0.392  1.00  0.00
ATOM     17  N   GLY A   5      27.111 -15.104   2.151  1.00  0.00
ATOM     18  CA  GLY A   5      26.193 -13.976   2.253  1.00  0.00
ATOM     19  C   GLY A   5      26.247 -13.107   1.003  1.00  0.00
ATOM     20  O   GLY A   5      25.216 -12.661   0.500  1.00  0.00
ATOM     21  N   GLY A   6      27.476 -12.825   0.546  1.00  0.00
ATOM     22  CA  GLY A   6      27.667 -12.010  -0.648  1.00  0.00
ATOM     23  C   GLY A   6      27.091 -12.696  -1.880  1.00  0.00
ATOM     24  O   GLY A   6      26.465 -12.054  -2.724  1.00  0.00
ATOM     25  N   GLY A   7      27.320 -14.002  -1.991  1.00  0.00
ATOM     26  CA  GLY A   7      26.765 -14.764  -3.104  1.00  0.00
ATOM     27  C   GLY A   7      25.243 -14.723  -3.095  1.00  0.00
ATOM     28  O   GLY A   7      24.610 -14.584  -4.142  1.00  0.00
ATOM     29  N   GLY A   8      24.668 -14.815  -1.914  1.00  0.00
ATOM     30  CA  GLY A   8      23.218 -14.757  -1.773  1.00  0.00
ATOM     31  C   GLY A   8      22.676 -13.401  -2.208  1.00  0.00
ATOM     32  O   GLY A   8      21.654 -13.320  -2.889  1.00  0.00
ATOM     33  N   GLY A   9      23.333 -12.356  -1.795  1.00  0.00
ATOM     34  CA  GLY A   9      22.916 -11.002  -2.139  1.00  0.00
ATOM     35  C   GLY A   9      23.017 -10.759  -3.639  1.00  0.00
ATOM     36  O   GLY A   9      22.135 -10.144  -4.239  1.00  0.00
ATOM     37  N   GLY A  10      24.079 -11.289  -4.242  1.00  0.00
ATOM     38  CA  GLY A  10      24.294 -11.123  -5.675  1.00  0.00
ATOM     39  C   GLY A  10      23.236 -11.865  -6.480  1.00  0.00
ATOM     40  O   GLY A  10      22.716 -11.346  -7.468  1.00  0.00
ATOM     41  N   GLY A  11      22.932 -13.075  -6.065  1.00  0.00
ATOM     42  CA  GLY A  11      21.975 -13.904  -6.788  1.00  0.00
ATOM     43  C   GLY A  11      20.567 -13.331  -6.693  1.00  0.00
ATOM     44  O   GLY A  11      19.827 -13.310  -7.677  1.00  0.00
ATOM     45  N   GLY A  12      20.199 -12.854  -5.531  1.00  0.00
ATOM     46  CA  GLY A  12      18.865 -12.293  -5.350  1.00  0.00
ATOM     47  C   GLY A  12      18.717 -10.973  -6.096  1.00  0.00
ATOM     48  O   GLY A  12      17.688 -10.715  -6.721  1.00  0.00
ATOM     49  N   GLY A  13      19.743 -10.178  -6.114  1.00  0.00
ATOM     50  CA  GLY A  13      19.701  -8.901  -6.816  1.00  0.00
ATOM     51  C   GLY A  13      19.603  -9.103  -8.323  1.00  0.00
ATOM     52  O   GLY A  13      18.842  -8.415  -9.003  1.00  0.00
ATOM     53  N   GLY A  14      20.403 -10.063  -8.833  1.00  0.00
ATOM     54  CA  GLY A  14      20.403 -10.344 -10.263  1.00  0.00
ATOM     55  C   GLY A  14      19.054 -10.886 -10.719  1.00  0.00
ATOM     56  O   GLY A  14      18.543 -10.503 -11.771  1.00  0.00
ATOM     57  N   GLY A  15      18.489 -11.783  -9.919  1.00  0.00
ATOM     58  CA  GLY A  15      17.200 -12.375 -10.259  1.00  0.00
ATOM     59  C   GLY A  15      16.096 -11.326 -10.262  1.00  0.00
ATOM     60  O   GLY A  15      15.230 -11.326 -11.137  1.00  0.00
ATOM     61  N   GLY A  16      16.083 -10.476  -9.292  1.00  0.00
ATOM     62  CA  GLY A  16      15.077  -9.425  -9.188  1.00  0.00
ATOM     63  C   GLY A  16      15.174  -8.453 -10.357  1.00  0.00
ATOM     64  O   GLY A  16      14.158  -8.020 -10.902  1.00  0.00
ATOM     65  N   GLY A  17      16.397  -8.088 -10.701  1.00  0.00
ATOM     66  CA  GLY A  17      16.618  -7.172 -11.814  1.00  0.00
ATOM     67  C   GLY A  17      16.132  -7.771 -13.127  1.00  0.00
ATOM     68  O   GLY A  17      15.511  -7.087 -13.940  1.00  0.00
ATOM     69  N   GLY A  18      16.340  -9.086 -13.274  1.00  0.00
ATOM     70  CA  GLY A  18      15.923  -9.760 -14.497  1.00  0.00
ATOM     71  C   GLY A  18      14.409  -9.917 -14.552  1.00  0.00
ATOM     72  O   GLY A  18      13.790  -9.699 -15.593  1.00  0.00
ATOM     73  N   GLY A  19      13.796 -10.218 -13.439  1.00  0.00
ATOM     74  CA  GLY A  19      12.369 -10.512 -13.379  1.00  0.00
ATOM     75  C   GLY A  19      11.542  -9.233 -13.403  1.00  0.00
ATOM     76  O   GLY A  19      10.493  -9.172 -14.044  1.00  0.00
ATOM     77  N   GLY A  20      11.906  -8.219 -12.739  1.00  0.00
ATOM     78  CA  GLY A  20      11.088  -7.024 -12.574  1.00  0.00
ATOM     79  C   GLY A  20      11.693  -5.836 -13.309  1.00  0.00
ATOM     80  O   GLY A  20      10.996  -4.877 -13.639  1.00  0.00
ATOM     81  N   GLY A  21      12.494  -6.054 -14.243  1.00  0.00
ATOM     82  CA  GLY A  21      13.101  -4.963 -14.996  1.00  0.00
ATOM     83  C   GLY A  21      12.080  -4.281 -15.898  1.00  0.00
ATOM     84  O   GLY A  21      12.075  -3.057 -16.030  1.00  0.00
ATOM     85  N   GLY A  22      11.021  -4.798 -16.165  1.00  0.00
ATOM     86  CA  GLY A  22       9.971  -4.221 -16.995  1.00  0.00
ATOM     87  C   GLY A  22       9.011  -3.379 -16.164  1.00  0.00
ATOM     88  O   GLY A  22       8.435  -2.409 -16.656  1.00  0.00
ATOM     89  N   GLY A  23       8.915  -3.604 -14.957  1.00  0.00
ATOM     90  CA  GLY A  23       8.031  -2.878 -14.053  1.00  0.00
ATOM     91  C   GLY A  23       8.747  -1.695 -13.413  1.00  0.00
ATOM     92  O   GLY A  23       9.943  -1.762 -13.128  1.00  0.00
ATOM     93  N   GLY A  24       7.990  -0.679 -13.141  1.00  0.00
ATOM     94  CA  GLY A  24       8.572   0.460 -12.441  1.00  0.00
ATOM     95  C   GLY A  24       8.860   0.121 -10.984  1.00  0.00
ATOM     96  O   GLY A  24       8.111  -0.621 -10.349  1.00  0.00
ATOM     97  N   GLY A  25       9.768   0.849 -10.439  1.00  0.00
ATOM     98  CA  GLY A  25      10.112   0.629  -9.039  1.00  0.00
ATOM     99  C   GLY A  25       8.920   0.898  -8.130  1.00  0.00
ATOM    100  O   GLY A  25       8.693   0.177  -7.158  1.00  0.00
ATOM    101  N   GLY A  26       8.154   1.983  -8.485  1.00  0.00
ATOM    102  CA  GLY A  26       7.004   2.364  -7.674  1.00  0.00
ATOM    103  C   GLY A  26       6.008   1.217  -7.556  1.00  0.00
ATOM    104  O   GLY A  26       5.460   0.966  -6.483  1.00  0.00
ATOM    105  N   GLY A  27       5.796   0.505  -8.608  1.00  0.00
ATOM    106  CA  GLY A  27       4.881  -0.630  -8.613  1.00  0.00
ATOM    107  C   GLY A  27       5.365  -1.732  -7.680  1.00  0.00
ATOM    108  O   GLY A  27       4.575  -2.335  -6.952  1.00  0.00
ATOM    109  N   GLY A  28       6.677  -2.022  -7.762  1.00  0.00
ATOM    110  CA  GLY A  28       7.245  -3.035  -6.882  1.00  0.00
ATOM    111  C   GLY A  28       7.131  -2.621  -5.420  1.00  0.00
ATOM    112  O   GLY A  28       6.790  -3.433  -4.560  1.00  0.00
ATOM    113  N   GLY A  29       7.397  -1.358  -5.170  1.00  0.00
ATOM    114  CA  GLY A  29       7.317  -0.833  -3.813  1.00  0.00
ATOM    115  C   GLY A  29       5.908  -0.971  -3.250  1.00  0.00
ATOM    116  O   GLY A  29       5.726  -1.337  -2.089  1.00  0.00
ATOM    117  N   GLY A  30       4.916  -0.622  -4.093  1.00  0.00
ATOM    118  CA  GLY A  30       3.522  -0.724  -3.678  1.00  0.00
ATOM    119  C   GLY A  30       3.159  -2.160  -3.320  1.00  0.00
ATOM    120  O   GLY A  30       2.465  -2.407  -2.334  1.00  0.00
ATOM    121  N   GLY A  31       3.663  -3.091  -4.145  1.00  0.00
ATOM    122  CA  GLY A  31       3.383  -4.504  -3.918  1.00  0.00
ATOM    123  C   GLY A  31       3.961  -4.973  -2.589  1.00  0.00
ATOM    124  O   GLY A  31       3.310  -5.704  -1.842  1.00  0.00
ATOM    125  N   GLY A  32       5.177  -4.532  -2.309  1.00  0.00
ATOM    126  CA  GLY A  32       5.846  -4.927  -1.076  1.00  0.00
ATOM    127  C   GLY A  32       5.147  -4.339   0.143  1.00  0.00
ATOM    128  O   GLY A  32       4.960  -5.019   1.152  1.00  0.00
ATOM    129  N   GLY A  33       4.772  -3.053   0.016  1.00  0.00
ATOM    130  CA  GLY A  33       4.103  -2.363   1.112  1.00  0.00
ATOM    131  C   GLY A  33       2.748  -2.991   1.412  1.00  0.00
ATOM    132  O   GLY A  33       2.382  -3.177   2.573  1.00  0.00
ATOM    133  N   GLY A  34       2.029  -3.299   0.342  1.00  0.00
ATOM    134  CA  GLY A  34       0.714  -3.908   0.502  1.00  0.00
ATOM    135  C   GLY A  34       0.812  -5.252   1.211  1.00  0.00
ATOM    136  O   GLY A  34       0.014  -5.557   2.098  1.00  0.00
ATOM    137  N   GLY A  35       1.759  -6.059   0.728  1.00  0.00
ATOM    138  CA  GLY A  35       1.942  -7.391   1.290  1.00  0.00
ATOM    139  C   GLY A  35       2.343  -7.320   2.758  1.00  0.00
ATOM    140  O   GLY A  35       1.849  -8.088   3.584  1.00  0.00
ATOM    141  N   GLY A  36       3.177  -6.401   3.081  1.00  0.00
ATOM    142  CA  GLY A  36       3.619  -6.224   4.459  1.00  0.00
ATOM    143  C   GLY A  36       2.470  -5.778   5.354  1.00  0.00
ATOM    144  O   GLY A  36       2.332  -6.247   6.483  1.00  0.00
ATOM    145  N   GLY A  37       1.595  -4.962   4.784  1.00  0.00
ATOM    146  CA  GLY A  37       0.434  -4.497   5.533  1.00  0.00
ATOM    147  C   GLY A  37      -0.521  -5.644   5.837  1.00  0.00
ATOM    148  O   GLY A  37      -1.050  -5.748   6.944  1.00  0.00
ATOM    149  N   GLY A  38      -0.781  -6.443   4.797  1.00  0.00
ATOM    150  CA  GLY A  38      -1.686  -7.576   4.946  1.00  0.00
ATOM    151  C   GLY A  38      -1.128  -8.603   5.922  1.00  0.00
ATOM    152  O   GLY A  38      -1.862  -9.162   6.737  1.00  0.00
ATOM    153  N   GLY A  39       0.162  -8.863   5.804  1.00  0.00
ATOM    154  CA  GLY A  39       0.805  -9.816   6.702  1.00  0.00
ATOM    155  C   GLY A  39       0.716  -9.353   8.151  1.00  0.00
ATOM    156  O   GLY A  39       0.463 -10.152   9.053  1.00  0.00
ATOM    157  N   GLY A  40       0.892  -8.053   8.357  1.00  0.00
ATOM    158  CA  GLY A  40       0.840  -7.502   9.706  1.00  0.00
ATOM    159  C   GLY A  40      -0.585  -7.499  10.245  1.00  0.00
ATOM    160  O   GLY A  40      -0.815  -7.789  11.419  1.00  0.00
ATOM    161  N   GLY A  41      -1.525  -7.383   9.428  1.00  0.00
ATOM    162  CA  GLY A  41      -2.933  -7.403   9.805  1.00  0.00
ATOM    163  C   GLY A  41      -3.401  -8.821  10.109  1.00  0.00
ATOM    164  O   GLY A  41      -4.200  -9.039  11.020  1.00  0.00
ATOM    165  N   GLY A  42      -2.694  -9.730   9.489  1.00  0.00
ATOM    166  CA  GLY A  42      -2.898 -11.143   9.786  1.00  0.00
ATOM    167  C   GLY A  42      -4.228 -11.636   9.229  1.00  0.00
ATOM    168  O   GLY A  42      -4.499 -12.837   9.215  1.00  0.00
ATOM    169  N   GLY A  43      -4.741 -10.977   8.275  1.00  0.00
ATOM    170  CA  GLY A  43      -6.008 -11.358   7.661  1.00  0.00
ATOM    171  C   GLY A  43      -5.806 -11.821   6.224  1.00  0.00
ATOM    172  O   GLY A  43      -6.750 -12.255   5.564  1.00  0.00
ATOM    173  N   GLY A  44      -5.523 -12.993   6.034  1.00  0.00
ATOM    174  CA  GLY A  44      -5.297 -13.553   4.707  1.00  0.00
ATOM    175  C   GLY A  44      -6.245 -14.712   4.430  1.00  0.00
ATOM    176  O   GLY A  44      -6.577 -15.484   5.329  1.00  0.00
ATOM    177  N   GLY A  45      -6.782 -14.731   3.258  1.00  0.00
ATOM    178  CA  GLY A  45      -7.668 -15.826   2.884  1.00  0.00
ATOM    179  C   GLY A  45      -6.886 -17.112   2.648  1.00  0.00
ATOM    180  O   GLY A  45      -5.771 -17.085   2.129  1.00  0.00
ATOM    181  N   GLY A  46      -7.650 -18.204   2.655  1.00  0.00
ATOM    182  CA  GLY A  46      -7.005 -19.491   2.426  1.00  0.00
ATOM    183  C   GLY A  46      -6.425 -19.574   1.020  1.00  0.00
ATOM    184  O   GLY A  46      -5.335 -20.110   0.818  1.00  0.00
ATOM    185  N   GLY A  47      -7.180 -19.014   0.044  1.00  0.00
ATOM    186  CA  GLY A  47      -6.732 -19.032  -1.343  1.00  0.00
ATOM    187  C   GLY A  47      -5.410 -18.292  -1.504  1.00  0.00
ATOM    188  O   GLY A  47      -4.521 -18.740  -2.228  1.00  0.00
ATOM    189  N   GLY A  48      -5.307 -17.134  -0.887  1.00  0.00
ATOM    190  CA  GLY A  48      -4.089 -16.336  -0.959  1.00  0.00
ATOM    191  C   GLY A  48      -2.925 -17.047  -0.281  1.00  0.00
ATOM    192  O   GLY A  48      -1.795 -17.013  -0.768  1.00  0.00
ATOM    193  N   GLY A  49      -3.230 -17.714   0.810  1.00  0.00
ATOM    194  CA  GLY A  49      -2.207 -18.476   1.516  1.00  0.00
ATOM    195  C   GLY A  49      -1.676 -19.615   0.656  1.00  0.00
ATOM    196  O   GLY A  49      -0.474 -19.879   0.631  1.00  0.00
ATOM    197  N   GLY A  50      -2.630 -20.306  -0.042  1.00  0.00
ATOM    198  CA  GLY A  50      -2.243 -21.405  -0.919  1.00  0.00
ATOM    199  C   GLY A  50      -1.341 -20.919  -2.046  1.00  0.00
ATOM    200  O   GLY A  50      -0.353 -21.569  -2.387  1.00  0.00
ATOM    201  N   GLY A  51      -1.675 -19.780  -2.626  1.00  0.00
ATOM    202  CA  GLY A  51      -0.874 -19.208  -3.702  1.00  0.00
ATOM    203  C   GLY A  51       0.497 -18.775  -3.198  1.00  0.00
ATOM    204  O   GLY A  51       1.507 -18.971  -3.873  1.00  0.00
ATOM    205  N   GLY A  52       0.522 -18.179  -2.003  1.00  0.00
ATOM    206  CA  GLY A  52       1.785 -17.779  -1.395  1.00  0.00
ATOM    207  C   GLY A  52       2.701 -18.978  -1.187  1.00  0.00
ATOM    208  O   GLY A  52       3.907 -18.897  -1.416  1.00  0.00
ATOM    209  N   GLY A  53       2.050 -20.085  -0.746  1.00  0.00
ATOM    210  CA  GLY A  53       2.809 -21.313  -0.543  1.00  0.00
ATOM    211  C   GLY A  53       3.432 -21.797  -1.846  1.00  0.00
ATOM    212  O   GLY A  53       4.578 -22.245  -1.868  1.00  0.00
ATOM    213  N   GLY A  54       2.661 -21.698  -2.930  1.00  0.00
ATOM    214  CA  GLY A  54       3.201 -22.056  -4.236  1.00  0.00
ATOM    215  C   GLY A  54       4.368 -21.154  -4.617  1.00  0.00
ATOM    216  O   GLY A  54       5.375 -21.618  -5.151  1.00  0.00
ATOM    217  N   GLY A  55       4.269 -19.906  -4.279  1.00  0.00
ATOM    218  CA  GLY A  55       5.342 -18.958  -4.557  1.00  0.00
ATOM    219  C   GLY A  55       6.547 -19.212  -3.660  1.00  0.00
ATOM    220  O   GLY A  55       7.692 -19.063  -4.086  1.00  0.00
ATOM    221  N   GLY A  56       6.305 -19.793  -2.553  1.00  0.00
ATOM    222  CA  GLY A  56       7.358 -20.096  -1.592  1.00  0.00
ATOM    223  C   GLY A  56       8.326 -21.135  -2.143  1.00  0.00
ATOM    224  O   GLY A  56       9.515 -21.121  -1.825  1.00  0.00
ATOM    225  N   GLY A  57       7.884 -21.824  -3.161  1.00  0.00
ATOM    226  CA  GLY A  57       8.770 -22.767  -3.833  1.00  0.00
ATOM    227  C   GLY A  57      10.077 -22.100  -4.240  1.00  0.00
ATOM    228  O   GLY A  57      11.152 -22.685  -4.105  1.00  0.00
ATOM    229  N   GLY A  58       9.962 -20.803  -4.638  1.00  0.00
ATOM    230  CA  GLY A  58      11.154 -20.040  -4.988  1.00  0.00
ATOM    231  C   GLY A  58      12.069 -19.864  -3.782  1.00  0.00
ATOM    232  O   GLY A  58      13.290 -19.959  -3.899  1.00  0.00
ATOM    233  N   GLY A  59      11.468 -19.659  -2.662  1.00  0.00
ATOM    234  CA  GLY A  59      12.216 -19.507  -1.420  1.00  0.00
ATOM    235  C   GLY A  59      12.976 -20.782  -1.076  1.00  0.00
ATOM    236  O   GLY A  59      14.129 -20.732  -0.649  1.00  0.00
ATOM    237  N   GLY A  60      12.263 -21.905  -1.232  1.00  0.00
ATOM    238  CA  GLY A  60      12.870 -23.200  -0.948  1.00  0.00
ATOM    239  C   GLY A  60      14.043 -23.475  -1.880  1.00  0.00
ATOM    240  O   GLY A  60      15.082 -23.979  -1.454  1.00  0.00
ATOM    241  N   GLY A  61      13.917 -23.072  -3.124  1.00  0.00
ATOM    242  CA  GLY A  61      14.996 -23.239  -4.091  1.00  0.00
ATOM    243  C   GLY A  61      16.219 -22.422  -3.697  1.00  0.00
ATOM    244  O   GLY A  61      17.351 -22.896  -3.792  1.00  0.00
ATOM    245  N   GLY A  62      15.967 -21.159  -3.287  1.00  0.00
ATOM    246  CA  GLY A  62      17.063 -20.304  -2.847  1.00  0.00
ATOM    247  C   GLY A  62      17.726 -20.860  -1.593  1.00  0.00
ATOM    248  O   GLY A  62      18.950 -20.834  -1.463  1.00  0.00
ATOM    249  N   GLY A  63      16.920 -21.394  -0.718  1.00  0.00
ATOM    250  CA  GLY A  63      17.433 -21.985   0.513  1.00  0.00
ATOM    251  C   GLY A  63      18.325 -23.184   0.218  1.00  0.00
ATOM    252  O   GLY A  63      19.373 -23.357   0.839  1.00  0.00
ATOM    253  N   GLY A  64      17.888 -24.014  -0.753  1.00  0.00
ATOM    254  CA  GLY A  64      18.676 -25.172  -1.159  1.00  0.00
ATOM    255  C   GLY A  64      20.026 -24.749  -1.723  1.00  0.00
ATOM    256  O   GLY A  64      21.055 -25.351  -1.416  1.00  0.00
ATOM    257  N   GLY A  65      19.996 -23.715  -2.562  1.00  0.00
ATOM    258  CA  GLY A  65      21.222 -23.209  -3.169  1.00  0.00
ATOM    259  C   GLY A  65      22.186 -22.688  -2.111  1.00  0.00
ATOM    260  O   GLY A  65      23.391 -22.928  -2.184  1.00  0.00
ATOM    261  N   GLY A  66      21.644 -21.975  -1.143  1.00  0.00
ATOM    262  CA  GLY A  66      22.459 -21.428  -0.065  1.00  0.00
ATOM    263  C   GLY A  66      23.066 -22.538   0.784  1.00  0.00
ATOM    264  O   GLY A  66      24.233 -22.469   1.171  1.00  0.00
ATOM    265  N   GLY A  67      22.244 -23.546   1.080  1.00  0.00
ATOM    266  CA  GLY A  67      22.723 -24.676   1.867  1.00  0.00
ATOM    267  C   GLY A  67      23.833 -25.423   1.138  1.00  0.00
ATOM    268  O   GLY A  67      24.828 -25.822   1.744  1.00  0.00
ATOM    269  N   GLY A  68      23.713 -25.543  -0.165  1.00  0.00
ATOM    270  CA  GLY A  68      24.746 -26.187  -0.968  1.00  0.00
ATOM    271  C   GLY A  68      26.048 -25.398  -0.925  1.00  0.00
ATOM    272  O   GLY A  68      27.130 -25.974  -0.809  1.00  0.00
ATOM    273  N   GLY A  69      25.921 -24.065  -0.986  1.00  0.00
ATOM    274  CA  GLY A  69      27.098 -23.207  -0.924  1.00  0.00
ATOM    275  C   GLY A  69      27.766 -23.286   0.442  1.00  0.00
ATOM    276  O   GLY A  69      28.992 -23.324   0.543  1.00  0.00
ATOM    277  N   GLY A  70      26.943 -23.273   1.471  1.00  0.00
ATOM    278  CA  GLY A  70      27.452 -23.383   2.833  1.00  0.00
ATOM    279  C   GLY A  70      28.238 -24.674   3.025  1.00  0.00
ATOM    280  O   GLY A  70      29.289 -24.682   3.667  1.00  0.00
ATOM    281  N   GLY A  71      27.659 -25.775   2.513  1.00  0.00
ATOM    282  CA  GLY A  71      28.325 -27.069   2.607  1.00  0.00
ATOM    283  C   GLY A  71      29.646 -27.064   1.848  1.00  0.00
ATOM    284  O   GLY A  71      30.648 -27.600   2.322  1.00  0.00
ATOM    285  N   GLY A  72      29.657 -26.410   0.699  1.00  0.00
ATOM    286  CA  GLY A  72      30.871 -26.300  -0.100  1.00  0.00
ATOM    287  C   GLY A  72      31.952 -25.527   0.644  1.00  0.00
ATOM    288  O   GLY A  72      33.128 -25.889   0.602  1.00  0.00
ATOM    289  N   GLY A  73      31.534 -24.452   1.318  1.00  0.00
ATOM    290  CA  GLY A  73      32.485 -23.656   2.084  1.00  0.00
ATOM    291  C   GLY A  73      32.997 -24.425   3.296  1.00  0.00
ATOM    292  O   GLY A  73      34.166 -24.315   3.664  1.00  0.00
ATOM    293  N   GLY A  74      32.193 -25.257   3.844  1.00  0.00
ATOM    294  CA  GLY A  74      32.581 -26.076   4.986  1.00  0.00
ATOM    295  C   GLY A  74      33.567 -27.162   4.576  1.00  0.00
ATOM    296  O   GLY A  74      34.478 -27.503   5.330  1.00  0.00
ATOM    297  N   GLY A  75      33.488 -27.641   3.403  1.00  0.00
ATOM    298  CA  GLY A  75      34.414 -28.648   2.900  1.00  0.00
ATOM    299  C   GLY A  75      35.815 -28.072   2.732  1.00  0.00
ATOM    300  O   GLY A  75      36.801 -28.686   3.139  1.00  0.00
ATOM    301  N   VAL B  76       1.204  -2.618  11.482  1.00  1.00
ATOM    302  CA  VAL B  76       2.160  -1.668  10.926  1.00  1.00
ATOM    303  C   VAL B  76       1.449  -0.490  10.273  1.00  1.00
ATOM    304  O   VAL B  76       0.462  -0.667   9.558  1.00  1.00
ATOM    305  N   SER B  77       1.864   0.708  10.567  1.00  1.00
ATOM    306  CA  SER B  77       1.317   1.914   9.957  1.00  1.00
ATOM    307  C   SER B  77       2.335   2.577   9.038  1.00  1.00
ATOM    308  O   SER B  77       3.532   2.583   9.324  1.00  1.00
ATOM    309  N   PHE B  78       1.852   3.352   8.098  1.00  1.00
ATOM    310  CA  PHE B  78       2.697   3.995   7.099  1.00  1.00
ATOM    311  C   PHE B  78       2.271   5.438   6.864  1.00  1.00
ATOM    312  O   PHE B  78       1.079   5.748   6.841  1.00  1.00
ATOM    313  N   GLU B  79       3.238   6.305   6.637  1.00  1.00
ATOM    314  CA  GLU B  79       2.996   7.661   6.158  1.00  1.00
ATOM    315  C   GLU B  79       3.251   7.769   4.660  1.00  1.00
ATOM    316  O   GLU B  79       4.247   7.255   4.151  1.00  1.00
ATOM    317  N   LEU B  80       2.298   8.226   3.949  1.00  1.00
ATOM    318  CA  LEU B  80       2.377   8.342   2.498  1.00  1.00
ATOM    319  C   LEU B  80       2.670   9.777   2.074  1.00  1.00
ATOM    320  O   LEU B  80       1.997  10.712   2.507  1.00  1.00
ATOM    321  N   PHE B  81       3.766   9.966   1.362  1.00  1.00
ATOM    322  CA  PHE B  81       4.186  11.298   0.945  1.00  1.00
ATOM    323  C   PHE B  81       3.410  11.763  -0.280  1.00  1.00
ATOM    324  O   PHE B  81       3.756  11.424  -1.412  1.00  1.00
ATOM    325  N   ALA B  82       2.140  12.032  -0.070  1.00  1.00
ATOM    326  CA  ALA B  82       1.250  12.461  -1.142  1.00  1.00
ATOM    327  C   ALA B  82       1.633  13.842  -1.657  1.00  1.00
ATOM    328  O   ALA B  82       1.548  14.115  -2.854  1.00  1.00
ATOM    329  N   ASP B  83       2.421  14.552  -0.783  1.00  1.00
ATOM    330  CA  ASP B  83       2.966  15.869  -1.089  1.00  1.00
ATOM    331  C   ASP B  83       4.106  15.774  -2.095  1.00  1.00
ATOM    332  O   ASP B  83       4.249  16.629  -2.968  1.00  1.00
ATOM    333  N   LYS B  84       4.769  14.700  -2.212  1.00  1.00
ATOM    334  CA  LYS B  84       5.854  14.452  -3.153  1.00  1.00
ATOM    335  C   LYS B  84       5.396  13.560  -4.300  1.00  1.00
ATOM    336  O   LYS B  84       5.756  13.785  -5.456  1.00  1.00
ATOM    337  N   VAL B  85       4.662  12.519  -4.002  1.00  1.00
ATOM    338  CA  VAL B  85       4.178  11.573  -5.000  1.00  1.00
ATOM    339  C   VAL B  85       2.700  11.265  -4.797  1.00  1.00
ATOM    340  O   VAL B  85       2.225  10.189  -5.158  1.00  1.00
ATOM    341  N   PRO B  86       1.839  12.117  -5.254  1.00  1.00
ATOM    342  CA  PRO B  86       0.415  12.053  -4.951  1.00  1.00
ATOM    343  C   PRO B  86      -0.242  10.863  -5.638  1.00  1.00
ATOM    344  O   PRO B  86      -1.079  10.178  -5.051  1.00  1.00
ATOM    345  N   LYS B  87       0.089  10.626  -6.912  1.00  1.00
ATOM    346  CA  LYS B  87      -0.493   9.544  -7.698  1.00  1.00
ATOM    347  C   LYS B  87      -0.089   8.183  -7.146  1.00  1.00
ATOM    348  O   LYS B  87      -0.899   7.257  -7.098  1.00  1.00
ATOM    349  N   THR B  88       1.127   8.024  -6.725  1.00  1.00
ATOM    350  CA  THR B  88       1.631   6.780  -6.157  1.00  1.00
ATOM    351  C   THR B  88       1.073   6.547  -4.758  1.00  1.00
ATOM    352  O   THR B  88       0.752   5.418  -4.388  1.00  1.00
ATOM    353  N   ALA B  89       1.081   7.600  -3.925  1.00  1.00
ATOM    354  CA  ALA B  89       0.509   7.531  -2.586  1.00  1.00
ATOM    355  C   ALA B  89      -0.976   7.195  -2.638  1.00  1.00
ATOM    356  O   ALA B  89      -1.471   6.399  -1.841  1.00  1.00
ATOM    357  N   GLU B  90      -1.686   7.786  -3.555  1.00  1.00
ATOM    358  CA  GLU B  90      -3.113   7.555  -3.748  1.00  1.00
ATOM    359  C   GLU B  90      -3.393   6.100  -4.101  1.00  1.00
ATOM    360  O   GLU B  90      -4.360   5.509  -3.621  1.00  1.00
ATOM    361  N   ASN B  91      -2.592   5.524  -5.023  1.00  1.00
ATOM    362  CA  ASN B  91      -2.722   4.128  -5.422  1.00  1.00
ATOM    363  C   ASN B  91      -2.661   3.201  -4.214  1.00  1.00
ATOM    364  O   ASN B  91      -3.428   2.244  -4.114  1.00  1.00
ATOM    365  N   PHE B  92      -1.621   3.399  -3.396  1.00  1.00
ATOM    366  CA  PHE B  92      -1.405   2.579  -2.210  1.00  1.00
ATOM    367  C   PHE B  92      -2.515   2.785  -1.187  1.00  1.00
ATOM    368  O   PHE B  92      -2.993   1.830  -0.575  1.00  1.00
ATOM    369  N   ARG B  93      -2.907   4.000  -0.970  1.00  1.00
ATOM    370  CA  ARG B  93      -3.942   4.335   0.000  1.00  1.00
ATOM    371  C   ARG B  93      -5.263   3.662  -0.348  1.00  1.00
ATOM    372  O   ARG B  93      -5.951   3.132   0.525  1.00  1.00
ATOM    373  N   ALA B  94      -5.753   3.858  -1.554  1.00  1.00
ATOM    374  CA  ALA B  94      -7.020   3.300  -2.010  1.00  1.00
ATOM    375  C   ALA B  94      -7.004   1.778  -1.953  1.00  1.00
ATOM    376  O   ALA B  94      -7.991   1.151  -1.567  1.00  1.00
ATOM    377  N   LEU B  95      -5.919   1.179  -2.271  1.00  1.00
ATOM    378  CA  LEU B  95      -5.756  -0.269  -2.206  1.00  1.00
ATOM    379  C   LEU B  95      -5.773  -0.761  -0.762  1.00  1.00
ATOM    380  O   LEU B  95      -6.331  -1.817  -0.463  1.00  1.00
ATOM    381  N   SER B  96      -5.335   0.046   0.157  1.00  1.00
ATOM    382  CA  SER B  96      -5.321  -0.279   1.578  1.00  1.00
ATOM    383  C   SER B  96      -6.719  -0.191   2.177  1.00  1.00
ATOM    384  O   SER B  96      -7.098  -1.008   3.016  1.00  1.00
ATOM    385  N   THR B  97      -7.518   0.686   1.726  1.00  1.00
ATOM    386  CA  THR B  97      -8.875   0.897   2.216  1.00  1.00
ATOM    387  C   THR B  97      -9.872   0.013   1.476  1.00  1.00
ATOM    388  O   THR B  97     -10.837  -0.476   2.062  1.00  1.00
ATOM    389  N   GLY B  98      -9.543  -0.419   0.274  1.00  1.00
ATOM    390  CA  GLY B  98     -10.410  -1.391  -0.381  1.00  1.00
ATOM    391  C   GLY B  98     -11.657  -0.724  -0.948  1.00  1.00
ATOM    392  O   GLY B  98     -12.466  -1.365  -1.618  1.00  1.00
ATOM    393  N   GLU B  99     -11.578   0.569  -1.153  1.00  1.00
ATOM    394  CA  GLU B  99     -12.660   1.422  -1.631  1.00  1.00
ATOM    395  C   GLU B  99     -12.947   1.172  -3.106  1.00  1.00
ATOM    396  O   GLU B  99     -14.095   1.243  -3.546  1.00  1.00
ATOM    397  N   LYS B 100     -12.209   0.530  -3.789  1.00  1.00
ATOM    398  CA  LYS B 100     -12.375   0.115  -5.177  1.00  1.00
ATOM    399  C   LYS B 100     -12.891  -1.316  -5.266  1.00  1.00
ATOM    400  O   LYS B 100     -13.442  -1.725  -6.288  1.00  1.00
ATOM    401  N   GLY B 101     -13.227  -1.957  -4.248  1.00  1.00
ATOM    402  CA  GLY B 101     -13.821  -3.288  -4.251  1.00  1.00
ATOM    403  C   GLY B 101     -12.748  -4.369  -4.228  1.00  1.00
ATOM    404  O   GLY B 101     -13.020  -5.521  -3.889  1.00  1.00
ATOM    405  N   PHE B 102     -11.540  -3.993  -4.403  1.00  1.00
ATOM    406  CA  PHE B 102     -10.370  -4.862  -4.348  1.00  1.00
ATOM    407  C   PHE B 102      -9.169  -4.133  -3.760  1.00  1.00
ATOM    408  O   PHE B 102      -9.010  -2.927  -3.949  1.00  1.00
ATOM    409  N   GLY B 103      -8.222  -5.032  -3.103  1.00  1.00
ATOM    410  CA  GLY B 103      -7.017  -4.363  -2.628  1.00  1.00
ATOM    411  C   GLY B 103      -6.101  -5.334  -1.895  1.00  1.00
ATOM    412  O   GLY B 103      -6.448  -6.498  -1.693  1.00  1.00
ATOM    413  N   TYR B 104      -5.461  -4.991  -0.935  1.00  1.00
ATOM    414  CA  TYR B 104      -4.391  -5.637  -0.185  1.00  1.00
ATOM    415  C   TYR B 104      -4.950  -6.521   0.923  1.00  1.00
ATOM    416  O   TYR B 104      -4.369  -7.553   1.259  1.00  1.00
ATOM    417  N   LYS B 105      -6.072  -6.233   1.423  1.00  1.00
ATOM    418  CA  LYS B 105      -6.647  -7.016   2.510  1.00  1.00
ATOM    419  C   LYS B 105      -6.914  -8.451   2.074  1.00  1.00
ATOM    420  O   LYS B 105      -7.594  -8.690   1.076  1.00  1.00
ATOM    421  N   GLY B 106      -6.218  -9.340   2.950  1.00  1.00
ATOM    422  CA  GLY B 106      -6.330 -10.764   2.659  1.00  1.00
ATOM    423  C   GLY B 106      -5.147 -11.252   1.834  1.00  1.00
ATOM    424  O   GLY B 106      -4.920 -12.456   1.708  1.00  1.00
ATOM    425  N   SER B 107      -4.320 -10.327   1.307  1.00  1.00
ATOM    426  CA  SER B 107      -3.123 -10.708   0.567  1.00  1.00
ATOM    427  C   SER B 107      -2.006 -11.138   1.510  1.00  1.00
ATOM    428  O   SER B 107      -1.884 -10.620   2.620  1.00  1.00
ATOM    429  N   CYS B 108      -0.911 -11.673   0.928  1.00  1.00
ATOM    430  CA  CYS B 108       0.199 -12.204   1.710  1.00  1.00
ATOM    431  C   CYS B 108       1.530 -11.640   1.230  1.00  1.00
ATOM    432  O   CYS B 108       1.694 -11.327   0.051  1.00  1.00
ATOM    433  N   PHE B 109       2.488 -11.560   2.086  1.00  1.00
ATOM    434  CA  PHE B 109       3.860 -11.301   1.669  1.00  1.00
ATOM    435  C   PHE B 109       4.510 -12.555   1.100  1.00  1.00
ATOM    436  O   PHE B 109       4.632 -13.569   1.787  1.00  1.00
ATOM    437  N   HIS B 110       4.664 -12.600  -0.182  1.00  1.00
ATOM    438  CA  HIS B 110       5.104 -13.796  -0.891  1.00  1.00
ATOM    439  C   HIS B 110       6.622 -13.840  -1.008  1.00  1.00
ATOM    440  O   HIS B 110       7.219 -14.915  -1.053  1.00  1.00
ATOM    441  N   ARG B 111       7.319 -12.836  -0.689  1.00  1.00
ATOM    442  CA  ARG B 111       8.758 -12.698  -0.880  1.00  1.00
ATOM    443  C   ARG B 111       9.385 -11.870   0.235  1.00  1.00
ATOM    444  O   ARG B 111       8.962 -10.743   0.497  1.00  1.00
ATOM    445  N   ILE B 112      10.129 -12.483   1.058  1.00  1.00
ATOM    446  CA  ILE B 112      10.766 -11.861   2.212  1.00  1.00
ATOM    447  C   ILE B 112      12.230 -12.270   2.319  1.00  1.00
ATOM    448  O   ILE B 112      12.558 -13.456   2.271  1.00  1.00
ATOM    449  N   ILE B 113      13.104 -11.329   2.198  1.00  1.00
ATOM    450  CA  ILE B 113      14.546 -11.540   2.241  1.00  1.00
ATOM    451  C   ILE B 113      15.165 -10.866   3.459  1.00  1.00
ATOM    452  O   ILE B 113      14.987  -9.667   3.674  1.00  1.00
ATOM    453  N   PRO B 114      15.711 -11.634   4.349  1.00  1.00
ATOM    454  CA  PRO B 114      16.275 -11.084   5.576  1.00  1.00
ATOM    455  C   PRO B 114      17.450 -10.162   5.277  1.00  1.00
ATOM    456  O   PRO B 114      18.355 -10.519   4.523  1.00  1.00
ATOM    457  N   GLY B 115      17.395  -8.953   5.899  1.00  1.00
ATOM    458  CA  GLY B 115      18.547  -8.078   5.716  1.00  1.00
ATOM    459  C   GLY B 115      18.384  -7.204   4.479  1.00  1.00
ATOM    460  O   GLY B 115      19.049  -6.178   4.340  1.00  1.00
ATOM    461  N   PHE B 116      17.500  -7.645   3.574  1.00  1.00
ATOM    462  CA  PHE B 116      17.147  -6.824   2.422  1.00  1.00
ATOM    463  C   PHE B 116      15.839  -6.080   2.656  1.00  1.00
ATOM    464  O   PHE B 116      15.792  -4.851   2.592  1.00  1.00

"""

def run_proteinmpnn(api_key, input_pdb, ca_only, use_soluble_model, num_seq_per_target, sampling_temp):
    url = "https://health.api.nvidia.com/v1/biology/ipd/proteinmpnn/predict"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "input_pdb": input_pdb,
        "ca_only": ca_only,
        "use_soluble_model": use_soluble_model,
        "num_seq_per_target": num_seq_per_target,
        "sampling_temp": sampling_temp
    }

    response = requests.post(url=url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    return response

def save_output(response, output_file="output.fasta"):
    try:
        response_data = json.loads(response.text)
        if "mfasta" not in response_data:
            raise KeyError("Response does not contain 'mfasta' key")
        print(response, f"Saving to {output_file}:\n", response.text[:200], "...")
        Path(output_file).write_text(response_data["mfasta"])
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse response JSON: {str(e)}")
    except KeyError as e:
        raise Exception(f"Invalid response format: {str(e)}")

def main():
    # Parameters explanation from structure analysis:

    
    api_key = get_api_key()
    input_pdb = get_pdb_content()
    ca_only = False
    use_soluble_model = False
    num_seq_per_target = 1
    sampling_temp = [0.1]

    try:
        response = run_proteinmpnn(api_key, input_pdb, ca_only, use_soluble_model, num_seq_per_target, sampling_temp)
        save_output(response)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()