import math
import cmath

class Spectral_Analyzer:
    """    class Spectral_Analyzer
    The class Spectral_Analyzer obtain the information of a cfd scheme from a respective instance 
    of class Scheme, and use this to compute modified wavenumber at a wavenumber.
    """

    nodes = 1001
    interval = 2.0 * math.pi
    index = range(0,nodes)
    dx = interval / (nodes - 1)
    x = [0.0] * nodes
    u = [0.0] * nodes
    f = [0.0] * nodes

    def __init__(self, scheme):
        self.scheme = scheme
        for i in Spectral_Analyzer.index:
            Spectral_Analyzer.x[i] = Spectral_Analyzer.dx * Spectral_Analyzer.index[i]
        return

    def Get_Modified(self, wavenumber):
        dft_sum = complex(0.0)

        if self.scheme.index[0] < 0:
            f_start = 0 - self.scheme.index[0]
        else:
            f_start = 0

        if self.scheme.index[-1] > 0:
            f_end = Spectral_Analyzer.nodes - self.scheme.index[-1]
        else:
            f_end = 0

        for j in Spectral_Analyzer.index:
            Spectral_Analyzer.u[j] = cmath.exp(complex(0.0,1.0) * (wavenumber * Spectral_Analyzer.x[j]))

        for j in range(f_start, f_end):
            Spectral_Analyzer.f[j] = self.scheme.Eval(Spectral_Analyzer.u, j)

        for j in range(f_start + 1, f_end):
            dft_sum = dft_sum + (Spectral_Analyzer.f[j] - Spectral_Analyzer.f[j - 1]) * cmath.exp(complex(0.0,1.0) * (- wavenumber * Spectral_Analyzer.x[j]))

        return dft_sum / (f_end - f_start - 1)