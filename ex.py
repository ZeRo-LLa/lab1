from math import tan,cos 
x,y =2.134,0.129

res = (x*y +(x**2)*(y**2))/tan((x**5)*(y**5)) - cos(x*y) + x*((x**5)**1/6) + 173.11*x
print(res)