from sympy import Symbol,sin,cos,simplify
import math
x=Symbol('x')
a=math.sqrt(2)
print(a)

expr=sin(x)/cos(x)
print(simplify(expr))

from sympy import Symbol,solve

y=Symbol('y')
sol=solve(x**2-x)#equal:x**2-x=0
print(sol)

from sympy import *
print(expand((x+1)**2))
z=Rational(1,2)
print(z)

print(simplify(sin(x)**2 + cos(x)**2))
alpha_mu = symbols('alpha_mu')
print(simplify(2*sin(alpha_mu)*cos(alpha_mu)))

x_1 = symbols('x_1')
print(expand((x_1 + 1)**2))

#factor (因式分解)
print(factor(x**3 - x**2 + x - 1))

#collect (合并同类项)

expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
print(collect(expr, x))

#cancel (有理分式化简)
print(cancel((x**2 + 2*x + 1)/(x**2 + x)))

l1=limit(1/x,x,oo)
print(l1)

#plot(x*x)
print(integrate(exp(-x), (x, 0, oo)))

print(integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))

print(limit(sin(x)/x, x, 0))

print(limit(1/x, x, 0, '+'))

expr = sin(x)
print(expr.series(x, 0, 4))

#求解一元二次方程:
Eq(x**2 - x, 0)#x**2-x=0
print(solveset(Eq(x**2 - x, 0), x, domain = S.Reals))