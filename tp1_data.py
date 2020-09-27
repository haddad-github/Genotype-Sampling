#!/usr/bin/env python
"""Module to read TP1's data from a Pickle."""


import pickle


samples = None
phenotypes = None
genotypes = None


with open("./data.pickle", "rb") as f:
    samples = pickle.load(f)
    phenotypes = pickle.load(f)
    genotypes = pickle.load(f)
