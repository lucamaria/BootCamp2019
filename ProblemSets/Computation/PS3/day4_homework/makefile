### CPP compiler wrapper
CXX=mpicxx

### Optimization flags
FFLAGS=-O3 -fopenmp

#######################################################################

all: pi_openmp_hybrid.exec

#######################################################################

pi_openmp_hybrid.exec: pi_openmp_hybrid.cpp
	$(CXX) $(FFLAGS) pi_openmp_hybrid.cpp -o pi_openmp_hybrid.exec


#######################################################################

clean :
	rm -f *.exec

#######################################################################
