# TFBind
Predict whether the transcription factor protein sequence binds to the DNA gene sequence

# Dependencies

TFBind works under Python 3.11.4

The required dependencies for TFBind are as follows：

python==3.11.4

torch==2.0.1

numpy

pandas==2.1.1

scikit-learn

# Input
TFBind Two files are required for input, one is the amino acid protein sequence of the transcription factor, and the other is the DNA nucleotide sequence. The protein sequence does not exceed 1451bp, and the DNA sequence does not exceed 150bp.

# Output
The output is 1 and 0. 1 represents the potential combination possibility in model calculation, and 0 represents the potential non-combination possibility.

# Cite
Liu et al., 2025. Deep Neural Network-Mining of Rice Drought-Responsive TF-TAG Modules by a Combinatorial Analysis of ATAC-Seq and RNA-Seq. First published: 31 March 2025 https://doi.org/10.1111/pce.15489.


