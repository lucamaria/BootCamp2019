#######################################################################

all: 	normalize_vec.exec normalize_vec_parallel.exec dot_prod.exec dot_prod_parallel.exec monte_carlo_parallel.exec

#######################################################################

normalize_vec.exec: normalize_vec.cpp
	g++ normalize_vec.cpp -fopenmp -o normalize_vec.exec

normalize_vec_parallel.exec: normalize_vec_parallel.cpp
	g++ normalize_vec_parallel.cpp -fopenmp -o normalize_vec_parallel.exec

dot_prod.exec: dot_prod.cpp
	g++ dot_prod.cpp -fopenmp -o dot_prod.exec

dot_prod_parallel.exec: dot_prod_parallel.cpp
	g++ dot_prod_parallel.cpp -fopenmp -o dot_prod_parallel.exec

monte_carlo_parallel.exec: monte_carlo_parallel.cpp
	g++ monte_carlo_parallel.cpp -fopenmp -o monte_carlo_parallel.exec
#######################################################################

clean :
	rm -f *.exec
