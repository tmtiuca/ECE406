#!/usr/bin/env python3
"""
ECE 406:  File for Exercise 1 of Assignment #3
"""
import numpy.fft as np
import math

def evaluate(poly, base):
    result = 0
    i = 0
    for coeff in poly:
        result += coeff * math.pow(base, i)
        i += 1

    return int(math.fabs(result))

def convert_bin(coeff):
    c = []
    for i in range(0, len(coeff) - 1):
        if coeff[i] > 1:
            coeff[i] -= 2
            coeff[i+1] += 1

        c.append(int(coeff[i].real))

    if coeff[-1] > 1:
        coeff[-1] -= 2
        coeff.append(1)
        c.append(int(coeff[-2].real))

    c.append(int(coeff[-1].real))

    return c

def main():
    """
    Exercise 1:  Using the FFT to multiply two binary numbers.
    You just need to fill in parts (v) and (vi)
    """
    # The binary numbers and their product
    a_bin = 0b110000001100
    b_bin = 0b100011110000
    c_bin = a_bin * b_bin
    print('The product of a and b is', c_bin)


    # (i) The coefficients of the polynomials A and B
    Acoeff = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    Bcoeff = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1]


    # (ii) the value representations of A and B
    Aval = np.fft(Acoeff, 32)
    Bval = np.fft(Bcoeff, 32)


    # (iii) The value representation of C
    Cval = []
    for i in range(len(Aval)):
        Cval.append(Aval[i] * Bval[i])

    print(Cval)
    # (iv) The coefficients of the polynomial C
    Ccoeff = np.ifft(Cval)
    # we'll get rid of the imaginary parts, which are just numerical errors
    for i, c in enumerate(Ccoeff):
        Ccoeff[i] = int(round(c.real))


    # (v) calculate the product by evaluating the polynomial at 2, i.e., C(2)
    C_2 = evaluate(Ccoeff, 2)
    print('Product in decimal: ', C_2)

    # (vi) write code to calculate the binary digits of c directly from the coefficients of C, Ccoeff.
    c = convert_bin(Ccoeff)

    print(c)

if __name__ == '__main__':
    main()
