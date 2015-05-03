#ifndef _SPECTRAL_ANALYZER_H_
#define _SPECTRAL_ANALYZER_H_

#include <complex>
#include "scheme.hpp"

using namespace std;

/* type operation */
typedef Scheme_Base < complex<double> > C_Scheme_Base;

class Spectral_Analyzer {
public:
	Spectral_Analyzer(C_Scheme_Base *_scheme, Scheme_Enum _scheme_type);
	~Spectral_Analyzer();
public:
	/* get modified wavenumber */
	complex<double> Modified_WN(double wavenumber);
	void Solve(Scheme_Char &scheme_char);
private:
	C_Scheme_Base *scheme;               //scheme instance
	Scheme_Enum scheme_type;
	complex<double> *u;         //function value
	complex<double> *f;         //sepcial variable
};

#endif