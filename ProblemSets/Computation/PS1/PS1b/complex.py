class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __str__(self):
        if self.imag >=0:
            return Complex(self.real, self.imag)
