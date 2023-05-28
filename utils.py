"""Utilities for running the paper selection process.

Simply change paths for the input and output files for each stage of the paper selection process,
then run on the command line (after cd'ing to this directory) with the following command:

python -m part-2-paper-selection
"""

# Steps:
# Stage 1: For each paper in all papers, input 0 or 1 for each category in Exclusion Stage 1.
# Stage 2: For each paper for which all criteria are 0 in Stage 1, input 0 or 1 for each category in Exclusion Stage 2.
# Duplicates: Mark duplicates in the table after identifying relationships.
# For each paper that passes Stage 2 AND is not a duplicate, enter criteria for each dimension table.