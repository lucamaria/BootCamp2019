#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	double iter = 10000;
	double x,y;
	int i;
	int count=0;
	double z;
	double pi;

	for (i=0; i<iter; ++i)
	{
		x = (double)random()/RAND_MAX;
		y = (double)random()/RAND_MAX;
		z = sqrt((x*x)+(y*y));
		if (z<=1)
		{
			++count;
		}
	}
	pi = ((double)count/(double)iter)*4.0;
	std::cout << "The approximation is: " << pi << std::endl;
	return 0;
}
