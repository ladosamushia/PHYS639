// warmupHW.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

double f1(double N, double t) {
	double a = 5;
	double b = 6;
	return (a*N) - (b*(N*N));
}
double f2(double N) {
	double t =  3;
	return -N/t;
}

//different differential equations to solve with euler method
int main()
{
	//output file
	ofstream out;
	out.open("warmup2star.txt");
	double N0 = 10;
	double xi = 0;
	double xf = 100;
	double s = 10000;
	double nlast = N0;
	double ss = (xf - xi) / s;
	double pos = xi;
	//time step stuff
	out << pos << "\t" << N0 << endl;
	//output
	while (pos < xf) {
		pos += ss;
		//change to next time
		double now = nlast + (ss*f1(nlast, pos));
		//euler stuff
		nlast = now;
		out << pos << "\t" << now << endl;
		//output
	}

    return 0;
}