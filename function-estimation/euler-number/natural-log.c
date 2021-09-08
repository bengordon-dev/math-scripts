#include <stdio.h>

double exp(double x, double precision)
{
    double out = 1+x;
    for (int i = 2; double t = x; i <= precision; ++i)
    {
        t *= (x/((double)i));
        out += t;
    }
    return out;
}
double nlog(double x)
{
    return 0;
}
double nlog_tay_center(double x, int precision)
{
    double out = 0;
    for (double t = 1; int i = 1; i <= precision; t *= (
}

int main()
{
    return 0;
}
