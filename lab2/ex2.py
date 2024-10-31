from math import prod, factorial

a, b, h = 0.1, 0.5, 0.05
d = 0.001
m = 20

def series_function(x, m, d):
    sum_result = 1
    term = x
    n = 1

    while abs(term) > d:
        term = (prod([m - (i - 1) for i in range(1, n + 1)]) / factorial(n)) * (x ** n)
        sum_result += term
        n += 1

    return sum_result

print("x\tf(x)")
while a <= b:
    fx = series_function(a, m, d)
    print(f"{a:.2f}\t{fx:.2f}")
    a += h
