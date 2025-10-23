# a⁻¹ ≡ a^(m-2) (mod m)

# use fast exponentiation (binary exponentiation)
from counting.binomial_coefficients import exp


def mod_inv_1(a, m):  # O(log m)
    return exp(a, m - 2, m)


# pythonic (not recommended)
import math


def mod_inv_2(a, m):  # O(log m)
    return math.pow(a, m - 2, m)
