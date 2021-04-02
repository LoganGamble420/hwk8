import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#1
def psi(r,a=1,b=1,c=1):
    term1 = a * np.exp(-b*r)
    term2 = -c/r**6
    return term1 + term2

range1 = np.arange(.5,5.1,.1)
psi_ans=[]

for r in range1:
    answer = psi(range1)
    psi_ans.append(answer)


#res = minimize(psi,range1, method  = 'nelder-mead')

print(range1)
print(psi_ans)

plt.plot(range1,psi_ans)
plt.yscale('log')
plt.show()


def f(x,y):
    a1=-(x-1)**2 - (2*(y-3)**2)
    a2=-2*(x-4)**2 - (y-1)**2
    return (5*np.exp(a1)) + (3*np.exp(a2))

xr = np.arange(0,5,.1)
yr = xr

ans = minimize(f,xr,yr, method = 'nelder-mead')

