class Scheme:
    """    class Scheme 
    The class Scheme record all information in a certain cfd scheme, and implement respective 
    computing process.
    For example, two-order central scheme Du(i) = (u(i + 1) - u(i - 1)) / (2 * dx) can be rewrited as 
    the conservative scheme Du(i) = (F(i + 1/2) - F(i - 1/2)) / dx, with F(i + 1/2) = 0.5 *(u(i) + u(i + 1)). 
    In this case, index = [0, 1] and coefficient = [0.5, 0.5].
    """
    def __init__(self, index, coefficient):
        self.index = index
        self.coefficient = coefficient
        return

    def Eval(self, u, j):
        partial = complex(0.0)
        for dj in self.index:
            partial = partial + u[j + dj] * self.coefficient[dj]
        return partial