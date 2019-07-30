#include <stdio.h>
#include <mpi.h>


int main (int argc, char *argv[])
{
    int rank, input, result;


    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    MPI_Comm_size(MPI_COMM_WORLD, &input);

    /* Compute sum of all ranks. */
    input=rank+1;

    MPI_Reduce(&input, &result, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    printf ("Rank %i:\tSum = %i\n", rank, input);

    MPI_Finalize();
    return 0;
}
