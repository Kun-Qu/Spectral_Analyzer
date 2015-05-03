from ctypes import *

dll = cdll.LoadLibrary('lib/x64/spectral_analyzer.dll')

class C_Scheme_Char(Structure):
    _fields_ = [("kr", POINTER(c_double)),
                ("ki", POINTER(c_double)),
                ("alpha", POINTER(c_double)),
                ("size", c_int)]

class C_Linear_Scheme(Structure):
    _fields_ = [("coefficient", POINTER(c_double)),
                ("left_end", c_int),
                ("right_end", c_int)]

class Linear_Scheme:
    ''' linear interpolation @ j - 1/2 node '''
    scheme_enum = 0

    def __init__(self, coeff, left, right):
        self.coeff = coeff
        self.left = left
        self.right = right

class Scheme_Char:
    ''' scheme character '''
    def __init__(self,c_scheme_char):
        self.kr = [0.0] * c_scheme_char.size
        self.ki = [0.0] * c_scheme_char.size
        self.alpha = [0.0] * c_scheme_char.size
        self.size = c_scheme_char.size

        for i in range(0, self.size):
            self.kr[i] = c_scheme_char.kr[i]
            self.ki[i] = c_scheme_char.ki[i]
            self.alpha[i] = c_scheme_char.alpha[i]

def Spectral_Analysis(scheme, nodes = 101):
    ''' return modified wavenumber - alpha relation of the scheme in C_Scheme_Char type. '''

    spectral_analysis = dll.Spectral_Analysis
    nodes_array = c_double * nodes
    scheme_array = c_double * (scheme.right - scheme.left + 1)

    pi = 3.141592653589793;
    kr = nodes_array()
    ki = nodes_array()
    alpha = nodes_array()
    coefficient = scheme_array()

    for i in range(0, nodes):
        alpha[i] = 0.5 * pi * (i / (nodes - 1))

    c_scheme_char = C_Scheme_Char(cast(kr, POINTER(c_double)), 
                              cast(ki, POINTER(c_double)), 
                              cast(alpha, POINTER(c_double)),
                              c_int(nodes))

    if 0 == scheme.scheme_enum:
        for i in range(0, scheme.right - scheme.left + 1):
            coefficient[i] = scheme.coeff[i]
        linear_scheme = C_Linear_Scheme(cast(coefficient, POINTER(c_double)), 
                                      c_int(scheme.left), 
                                      c_int(scheme.right))
        spectral_analysis(pointer(c_scheme_char), pointer(linear_scheme), c_int(0))
        return c_scheme_char
    else:
        return -1

def Max_Alpha(c_scheme_char, tol = 0.05):
    ''' return max alpha value satisfied with tolerance tol. '''
    max_alpha = dll.Max_Alpha
    max_alpha.restype = c_double
    return max_alpha(pointer(c_scheme_char), c_double(tol))

def Dispersion_Mode(c_scheme_char):
    ''' return 0 if the scheme is fast mode, return 1 if slow mode. '''
    dispersion_mode = dll.Dispersion_Mode
    return dispersion_mode(pointer(c_scheme_char))

def Write_Scheme_Char(filename, c_scheme_char):
    f = open(filename,'w')
    f.write('VARIABLES = "alpha", "kr", "ki"\n')
    f.write('ZONE I=')
    f.write(str(c_scheme_char.size))
    f.write(', DATAPACKING=BLOCK\n')
    for i in range(0, c_scheme_char.size):
        f.write(str(c_scheme_char.alpha[i]))
        f.write('\t')
    for i in range(0, c_scheme_char.size):
        f.write(str(c_scheme_char.kr[i]))
        f.write('\t')
    for i in range(0, c_scheme_char.size):
        f.write(str(c_scheme_char.ki[i]))
        f.write('\t')
    f.close()