#Resolve the equation from the associated open issue
# Test Data
# Sample input: 1 <-> Expected output: y = 0.6000000000000001
# Sample input: 10 <-> Expected output: y = 0.09901951266867294
# Sample input: 100 <-> Expected output: y = 0.009999000199950014
# Sample input: -5 <-> Expected output: y = -0.19258202567760344

def ecuacion(x):
     y=1/(x+1/(x+(1/(x+1/x))))
     return(y)
print (f"x=1, y={ecuacion(1)}")
print (f"x=10, y={ecuacion(10)}")
print (f"x=100, y={ecuacion(100)}")
print (f"x=-5, y={ecuacion(-5)}")
