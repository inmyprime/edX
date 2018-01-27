def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    L_reverse = L[::-1]
    def poly(x):
        return sum([L_reverse[i] * x**i for i in range(len(L))])
    return poly

print(general_poly([1, 2, 3, 4])(100))
