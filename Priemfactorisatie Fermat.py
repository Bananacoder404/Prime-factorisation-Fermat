import time, numpy
delers = []
while True:
    n=int(input("Het getal dat u wilt factoriseren: "))
    start=time.time()
    if n%2==0:
        delers.append(2)
        delers.append(int(n/2))
    
    else:
        x=numpy.ceil(numpy.sqrt(n))
        while True:
            y=numpy.sqrt(numpy.power(x, 2)-n)
            yf=int(y)
            if (yf*yf==numpy.power(x, 2)-n):
                delers.append(int(x+y))
                delers.append(int(x-y))
                break
            else:
                x=x+1
                
    end=time.time()
    timer=end-start
    print("Delers: " + str(delers))
    print("Tijd: " + str(timer) + " seconden")
    delers.clear()
    
