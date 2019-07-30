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

	for(int i=0; i<numtasks; ++i)
	{
		double x = (double)random()/RAND_MAX;
		double y = (double)random()/RAND_MAX;
		double z = sqrt((x*x)+(y*y));
		if (z<=1)
		{
			++count;
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
	}
	MPI_Finalize();
	return 0;
}
