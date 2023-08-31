import math
import latexify

@latexify.with_latex
def solve (a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*(a))
solve

@latexify.with_latex
def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x
sinc
# by clcoding.com