#ifndef _SPECTRAL_ANALYZER_SCHEME_H_
#define _SPECTRAL_ANALYZER_SCHEME_H_

#include "scheme_info.h"

template<typename T>
class Scheme_Base {
public:
	Scheme_Base(int left, int right);
	~Scheme_Base() { }
public:
	inline Scheme_Info Get_Info(void);
	virtual T Eval(T *u) = 0;
protected:
	Scheme_Info scheme_info;
};

template<typename T>
class Linear_Scheme : public Scheme_Base < T > {
public:
	Linear_Scheme(int left, int right, double *coeff);
	~Linear_Scheme();
public:
	T Eval(T *u);
private:
	double *coefficient;
};

#endif