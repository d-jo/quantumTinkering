#!/bin/python/

from pyquil.quil import Program
import pyquil.api as api
from pyquil.gates import *
import numpy as np

# converts binary to decimal
def b2d(binaryListList):
    num = 0
    pos = 0
    for internalList in binaryListList:
        for a in reversed(internalList):
            num += (a * (2 ** pos))
            pos += 1
    return num

# collapses a quantum state of log2(n) qbits
def throw_nside_die(n):
    # API connection
    qvm = api.QVMConnection()
    p = Program()
    # figure how many bits we need
    b = int(np.ceil(np.log2(n)))
    # for each bit, put it in superposition 
    # 1/sqrt(2)|0> + 1/sqrt(2)|1>
    for x in range(0, b):
        p.inst(H(x))
    for x in range(0, b):
        # collapse each superposition
        p.measure(x, x)
    # run the program
    return (qvm.run(p ,range(0, b)))


# run tests
print("count\tsides\tresult")
for i in range(1, 20):
    sides = 10
    binary = throw_nside_die(sides)
    print(i, '\t', sides, '\t', (b2d(binary) % sides) + 1)
