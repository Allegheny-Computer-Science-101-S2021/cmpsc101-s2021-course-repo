class patient:
    def __init__(self, inp, outp):
        self.inp = inp
        self.outp = outp
    def __str__(self):
        return str(self.inp) + " " + str(self.outp)
    def __add__(self, addend):
        inp = self.inp + addend.inp
        outp = self.outp + addend.outp
        return patient(inp,outp)
day1 = patient(20,30)
day2 = patient(10,20)
print(day1,day2)
print(day1+day2)