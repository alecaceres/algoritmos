from cmath import e, tau, log, exp, isclose
import numpy

def FFT(a, w):
    if isclose(w, 1, rel_tol = 1e-03): # ya que difílmente se llega al valor teórico de 1
        return a
    n = len(a)
    s1 = FFT(a[0::2], w**2) # elementos impares
    s2 = FFT(a[1::2], w**2) # elementos pares
    r = numpy.zeros(n, dtype = complex)
    waux = 1
    for j in range(0,n//2):
        r[j] = s1[j] + waux*s2[j]
        r[j+n//2] = s1[j] - waux*s2[j]
        waux *= w
    return r

a = input("\nIngrese la entrada:\n")
a = a.split()
a = [complex(x) for x in a]
a = numpy.array(a)
n = len(a)
w = exp(1j*tau/n)
print("\nLa FFT es: ", FFT(a, w), "\n")
