
### CPP compiler wrapper
CXX=mpicxx

### Optimization flags
FFLAGS=-O3

#######################################################################

all: broadcast.exec allreduce.exec scatter.exec monte_carlo_mpi.exec

#######################################################################

broadcast.exec: broadcast.cpp
	$(CXX) $(FFLAGS) broadcast.cpp -o broadcast.exec

allreduce.exec: allreduce.cpp
	$(CXX) $(FFLAGS) allreduce.cpp -o allreduce.exec

scatter.exec: scatter.cpp
	$(CXX) $(FFLAGS) scatter.cpp -o scatter.exec

monte_carlo_mpi.exec: monte_carlo_mpi.cpp
	$(CXX) $(FFLAGS) monte_carlo_mpi.cpp -o monte_carlo_mpi.exec

#######################################################################

clean :
	rm -f *.exec

#######################################################################	
