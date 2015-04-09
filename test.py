from spectral_analyzer.scheme import Scheme
from spectral_analyzer.spectral_analyzer import Spectral_Analyzer
from spectral_analyzer.scheme_test import Scheme_Test

def main():
    central_scheme =Scheme([0, 1], [0.5, 0.5])
    scheme_test = Scheme_Test(central_scheme)
    scheme_test.Solve()
    scheme_test.Write('output.dat')

if __name__ == '__main__':
    main()