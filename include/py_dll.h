#ifndef _PY_DLL_H_
#define _PY_DLL_H_

#ifdef _PY_DLL_IMPLEMENTION_
#define _DLL_FUNCTION_ATTRIBUTE_ extern "C" __declspec(dllexport)
#else
#define _DLL_FUNCTION_ATTRIBUTE_ extern "C" __declspec(dllimport)
#endif

/* scheme enumerator */

#define LINEAR 0
#define GVC 1

/* scheme dispersion mode */
#define FAST_MODE 0
#define SLOW_MODE 1

typedef struct _Py_Scheme_Char{
	double *kr;
	double *ki;
	double *alpha;
	int size;
} Py_Scheme_Char;

typedef struct _Py_Linear_Scheme{
	double *coefficient;
	int left_end;
	int right_end;
} Py_Linear_Scheme;

_DLL_FUNCTION_ATTRIBUTE_ void Spectral_Analysis(Py_Scheme_Char *s_char, Py_Linear_Scheme *l_scheme, int s_enum);
_DLL_FUNCTION_ATTRIBUTE_ double Max_Alpha(Py_Scheme_Char *s_char, double tol);
_DLL_FUNCTION_ATTRIBUTE_ int Dispersion_Mode(Py_Scheme_Char *s_char);

#endif