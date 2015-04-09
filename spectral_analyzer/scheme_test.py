from spectral_analyzer.spectral_analyzer import Spectral_Analyzer

class Scheme_Test:
    """    class Scheme_Test
    The class Scheme_Test use class Spectral_Analyzer to perform analysis on a cfd scheme.
    The output of the method Write(self, filename) can be recognized by Tecplot.
    """

    k_interval = 5
    k_n = int(Spectral_Analyzer.nodes / (2 * k_interval) + 1)
    k = range(0, k_n * k_interval, k_interval)
    mk = [complex(0.0)] * k_n

    def __init__(self, scheme):
        self.analyzer = Spectral_Analyzer(scheme)
        return

    def Solve(self):
        for i in range(0, Scheme_Test.k_n):
            Scheme_Test.mk[i] = self.analyzer.Get_Modified(Scheme_Test.k[i])
        return

    def Write(self,filename):
        f = open(filename,'w')
        f.write('VARIABLES = "alpha", "kr", "ki"\n')
        f.write('ZONE I=')
        f.write(str(Scheme_Test.k_n))
        f.write(', DATAPACKING=BLOCK\n')
        for i in range(0,Scheme_Test.k_n):
            f.write(str(Scheme_Test.k[i] * Spectral_Analyzer.dx))
            f.write('\t')
        f.write('\n')
        for i in range(0,Scheme_Test.k_n):
            f.write(str(Scheme_Test.mk[i].real))
            f.write('\t')
        f.write('\n')
        for i in range(0,Scheme_Test.k_n):
            f.write(str(Scheme_Test.mk[i].imag))
            f.write('\t')
        f.write('\n')
        f.close()