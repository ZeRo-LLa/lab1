import math

a,b,h = 0.4, 0.8, 0.02
print("x\tf(x)")
while a <= b:
    if a < 0.5:
        fx = abs(math.log(a)) ** 7
    elif 0.5 <= a <= 0.7:
        fx = 1 / math.tan(a + a ** 3)
    elif a > 0.7:
        fx = math.log(math.sin(a), 5)
    print(f"{a:.2f}\t{fx:.6f}")
    a += h
