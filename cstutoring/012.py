"""
Given the following functions:

f(x) = 50x^3 - 46x^2 + 25x - 14
g(x) = 49x^3 + 45x^2 - 20x^3 + 195x - 4

What are the first 5 digits of f(105) * g(105)?
"""

def f(x):
    return 50*(x**3) - 46*(x**2) + 25*x -14

def g(x):
    return 49*(x**3) + 45*(x**2) - 20*(x**3) +195*x - 4

print str(f(105) * g(105))[:5]