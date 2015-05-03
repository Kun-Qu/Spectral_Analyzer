#ifndef _SPECTRAL_ANALYZER_SCHEME_INFO_H_
#define _SPECTRAL_ANALYZER_SCHEME_INFO_H_

typedef enum {
	linear = 0,
	gvc = 1,
	weno = 2
} Scheme_Enum;

typedef struct _Scheme_Info{
	int left_end;
	int right_end;
} Scheme_Info;

/* the character of a cfd scheme */
typedef struct _Scheme_Char {
	double *kr;              //real part of modified wavenumber
	double *ki;              //imaginery part of modified wavenumber
	double *alpha;           //alpha = wavenumber * dx
	int size;                //size of array
} Scheme_Char;

#endif