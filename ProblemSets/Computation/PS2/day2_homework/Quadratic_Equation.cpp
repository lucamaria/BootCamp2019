#include <iostream>
#include <math.h>

using namespace std;

void quadratic(int a, int b, int c, double& x1,double& x2)
{
  x1 = (-b+sqrt(b*b-4*a*c))/(2*a);
  x2 = (-b-sqrt(b*b-4*a*c))/(2*a);
}


int main()
{
  int a,b,c;
  double x1,x2;

  cout << "Enter parameters a,b and c" << endl;
  cout << "\n Parameter a: ";
  cin >> a;
  cout << "\n Parameter b: ";
  cin >> b;
  cout << "\n Parameter c: ";
  cin >> c;

  quadratic(a,b,c,x1,x2);

  cout << "The solution to the quadratic equation is"  << x1 << " and " << x2<< endl;

  return 0;
}
