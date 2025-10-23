# a⁻¹ ≡ a^(m-2) (mod m)

# use fast exponentiation (binary exponentiation)
from combinatorics.binomial_coefficients import exp


def mod_inv_1(a, m):
    return exp(a, m - 2, m)


# pythonic (not recommended)
import math


def mod_inv_2(a, m):
    return math.pow(a, m - 2, m)
