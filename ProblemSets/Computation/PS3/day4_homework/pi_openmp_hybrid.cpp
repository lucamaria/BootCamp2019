/* Note: I use the monte_carlo_mpi.cpp file as a baseline because to my understanding
it is easier to transform it this way into hybrid
*/

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <mpi.h>


int main(int argc, char **argv)
{
	int iter = 4000000;
	int p, myid, tag, proc, pi_sum, ierr, pi;
	int master=0;
	MPI_Comm comm;
	MPI_Status status;

	comm = MPI_COMM_WORLD;
	ierr = MPI_Init(&argc,&argv);
	MPI_Comm_rank(comm, &myid);
	MPI_Comm_size(comm, &p);
	int numtasks=iter/p;
	int count=0;
  double x,y,z;

  #pragma omp parallel private(x,y,z) reduction(+:count)
  {
    unsigned int seed = 123+10*omp_get_thread_num();

		#pragma omp for
  	for(int i=0; i<numtasks; ++i)
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
	MPI_Send(&count, 1, MPI_INT, master, tag, comm);
	if(myid == master)
	{
		pi_sum = 0.0;
		for (proc=0 ; proc< p; proc++)
		{
			MPI_Recv(&count, 1, MPI_INT, proc, tag, comm, & status);     /* status reports source, tag */
			pi_sum += count;
		}
		std::cout << "The approximation is: " << pi_sum*4.0/iter << std::endl;
    std::cout << "Experimenting with processes & threads directly done in the terminal "<< std::endl;
	}
	MPI_Finalize();
	return 0;
}
