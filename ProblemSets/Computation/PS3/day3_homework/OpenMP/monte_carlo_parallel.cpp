#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>


double start = omp_get_wtime( );
int main()
{
	int iter = 10000;
	double x,y;
	int i;
	int count=0;
	double z;
	double pi;
	unsigned int seed;
	double time;
	#pragma omp parallel private(x,y,z) reduction(+:count)
	{
		unsigned int seed = 123+10*omp_get_thread_num();

		#pragma omp for
		for (i=0; i<iter; ++i)
		{
			x = (double)rand_r(&seed)/RAND_MAX;
			y = (double)rand_r(&seed)/RAND_MAX;
			z = sqrt((x*x)+(y*y));
			if (z<=1)
			{
				++count;
			}
		}
	}
	pi = ((double)count/(double)iter)*4.0;

	std::cout << "The approximation is: " << pi << std::endl;
	double end = omp_get_wtime();// end the timer
	double dif = end - start; // stores the difference in dif
	std::cout << "The computation time for N=10000 is: " << dif << std::endl;
	return 0;
}
