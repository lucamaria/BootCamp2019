class ComplexNumber:
    def __init__(self, real, imag=0.00):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.real-self.imag*1j

    def __str__(self):
        if self.imag >= 0:
            string=str("("+str(self.real)+"+"+str(self.imag)+"j)")
        else:
            string=str("("+str(self.real)+"-"+str(self.imag)+"j)")
        return string

    def __abs__(self):
        return sqrt(self.real**2+self.imag**2)

    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real-other.real, self.imag-other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real - self.imag*other.imag,
                             self.imag*other.real+self.real*other.imag)

    def __truediv__(self, other):
        sr, si, otr, oi = self.real, self.imag, other.real, other.imag
        r=float(otr**2+oi**2)
        return ComplexNumber((sr*otr+si*oi)/r,(si*otr-sr*oi)/r)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
