#ifndef _SPECTRAL_ANALYZER_SCHEME_HPP_
#define _SPECTRAL_ANALYZER_SCHEME_HPP_

#include "scheme.h"

template<typename T>
Scheme_Base<T>::Scheme_Base(int left, int right) {
	scheme_info.left_end = left;
	scheme_info.right_end = right;
}

template<typename T>
Scheme_Info Scheme_Base<T>::Get_Info(void) {
	return scheme_info;
}

template<typename T>
Linear_Scheme<T>::Linear_Scheme(int left, int right, double *coeff) : Scheme_Base<T>(left, right) {
	coefficient = new double[right - left + 1];
	for (int i = 0; i < right - left + 1; i++)
	{
		coefficient[i] = coeff[i];
	}
}

template<typename T>
Linear_Scheme<T>::~Linear_Scheme() {
	delete[] coefficient;
	coefficient = 0;
}

template<typename T>
T Linear_Scheme<T>::Eval(T *u) {
	T eval = T(0.0);
	for (int i = scheme_info.left_end; i < scheme_info.right_end + 1; i++)
	{
		eval = eval + u[i] * coefficient[i - scheme_info.left_end];
	}
	return eval;
}

#endif