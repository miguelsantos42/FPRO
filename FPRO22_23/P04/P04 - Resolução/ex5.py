def deriv(f):
    def df(x):
        h = 0.001
        derivate = (f(x+h) - f(x))/h
        return round(derivate,3)
    return df

def f(x):
    return x*x + 2*x + 2
print(deriv(f)(3))