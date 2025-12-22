print("power calculator")
base=(float(input("(enter ur base number:")))
exponent=(int(input("enter ur exponent:")))
if exponent==0:
    results=1
    print("Results:",results)
elif exponent>0:
    result=base**exponent
    print("Results:",result)
else:
    result=1/(base**abs(exponent))
    print("Results:",result)