from spectral_analyzer import *

#    test section

#    1st order upwind scheme

ls_1 = Linear_Scheme([1.0], -1, -1)
print(ls_1)
c_scheme_char_1 = Spectral_Analysis(ls_1)
alpha_1 = Max_Alpha(c_scheme_char_1)
mode_1 = Dispersion_Mode(c_scheme_char_1)
py_scheme_char_1 = Scheme_Char(c_scheme_char_1)
Write_Scheme_Char('upwind_1.dat', c_scheme_char_1)

#    2nd order central scheme

ls_2 = Linear_Scheme([0.5, 0.5], -1, 0)
print(ls_2)
c_scheme_char_2 = Spectral_Analysis(ls_2)
alpha_2 = Max_Alpha(c_scheme_char_2)
mode_2 = Dispersion_Mode(c_scheme_char_2)
py_scheme_char_2 = Scheme_Char(c_scheme_char_2)
Write_Scheme_Char('central_2.dat', c_scheme_char_2)