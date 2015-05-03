#include "spectral_analyzer.h"

/* type operation */

typedef Linear_Scheme < std::complex<double> > C_Linear_Scheme;

/* parameter definition */

#define WINDOW_SIZE (2.0 * 3.141592653589793)
#define NODES_IN_WINDOW 1001
#define SPACIAL_STEP (WINDOW_SIZE / (NODES_IN_WINDOW - 1))
#define WAVE_NUMBER ((NODES_IN_WINDOW - 1) / 2)

/* macro function */

#define Min(a, b) ((a) < (b) ? (a) : (b))
#define Max(a, b) ((a) > (b) ? (a) : (b))

Spectral_Analyzer::Spectral_Analyzer(C_Scheme_Base *_scheme, Scheme_Enum _scheme_type) : scheme_type(_scheme_type) {
	u = new complex<double>[NODES_IN_WINDOW];
	f = new complex<double>[NODES_IN_WINDOW];

	if (Scheme_Enum::linear == _scheme_type)
	{
		scheme = _scheme;
	}
	else
	{

	}
}


Spectral_Analyzer::~Spectral_Analyzer() {
	delete[] u;
	delete[] f;
}


complex<double> Spectral_Analyzer::Modified_WN(double wavenumber) {

	const complex<double> i(0.0, 1.0);
	complex<double> dft_sum(0.0, 0.0);
	complex<double> mul = exp(i * (wavenumber * SPACIAL_STEP));
	Scheme_Info scheme_info = scheme->Get_Info();
	int f_start = Max(-scheme_info.left_end, 0);
	int f_end = NODES_IN_WINDOW + Min(- scheme_info.right_end, 0);

	u[0] = 1.0;
	for (int j = 1; j < NODES_IN_WINDOW; j++)
	{
		u[j] = u[j - 1] * mul;
	}

	for (int j = f_start; j < f_end; j++)
	{
		f[j] = scheme->Eval(&u[j]);
	}

	for (int j = f_start + 1; j < f_end; j++)
	{
		dft_sum += (f[j] - f[j - 1]) / u[j - 1];
	}

	return dft_sum * (1.0 / (f_end - f_start - 1));
}

void Spectral_Analyzer::Solve(Scheme_Char &scheme_char) {
	complex<double> temp;
	for (int i = 0; i < scheme_char.size; i++)
	{
		temp = Modified_WN(scheme_char.alpha[i] / SPACIAL_STEP);
		scheme_char.kr[i] = temp.real();
		scheme_char.ki[i] = temp.imag();
	}
}