#ifndef _PY_DLL_IMPLEMENTION_
#define _PY_DLL_IMPLEMENTION_

#include <math.h>
#include "py_dll.h"
#include "spectral_analyzer.h"

static inline void Struct_Convert(Scheme_Char &scheme_char, Py_Scheme_Char *s_char) {
	scheme_char.alpha = s_char->alpha;
	scheme_char.kr = s_char->kr;
	scheme_char.ki = s_char->ki;
	scheme_char.size = s_char->size;
}

void Spectral_Analysis(Py_Scheme_Char *s_char, Py_Linear_Scheme *l_scheme, int s_enum) {
	Scheme_Char scheme_char;

	Struct_Convert(scheme_char, s_char);

	if (LINEAR == s_enum)
	{
		Linear_Scheme<complex<double>> scheme(l_scheme[0].left_end, l_scheme[0].right_end, l_scheme[0].coefficient);
		Spectral_Analyzer analyzer(&scheme, (Scheme_Enum)s_enum);
		analyzer.Solve(scheme_char);
	}
	else if (GVC == s_enum)
	{

	}
	else
	{

	}
}

double Max_Alpha(Py_Scheme_Char *s_char, double tol) {
	double max_alpha = 0.0;

	for (int i = 1; i < s_char->size; i++)
	{
		if ((abs(s_char->kr[i]) < tol) && (abs(s_char->ki[i] / s_char->alpha[i] - 1.0) < tol))
		{
			max_alpha = s_char->alpha[i];
		}
		else
		{
			break;
		}
	}

	return max_alpha;
}

int Dispersion_Mode(Py_Scheme_Char *s_char) {
	int dispersion_mode = 0;
	double max_alpha = 0.0;
	double integral = 0.0;

	max_alpha = Max_Alpha(s_char, 0.05);

	for (int i = 1; s_char->alpha[i] <= max_alpha; i++)
	{
		integral = integral + (s_char->ki[i] / s_char->alpha[i] - 1.0);
	}

	if (integral < 0.0)
	{
		return SLOW_MODE;
	}
	else
	{
		return FAST_MODE;
	}
}

#endif