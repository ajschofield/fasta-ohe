import numpy as np

sequence = 'ACGTACGTACGTACGT'

mapping = {
    'A': [1, 0, 0, 0],
    'C': [0, 1, 0, 0],
    'G': [0, 0, 1, 0],
    'T': [0, 0, 0, 1]
}

def encode(sequence, mapping=mapping):
    return np.array([mapping[base] for base in sequence])

print(encode(sequence))