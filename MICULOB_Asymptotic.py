import math
import matplotlib.pyplot as plt
import time

n = int(input("Enter a number: "))
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []

start_time = time.time()
def logarithmic(n):
    print(math.log(n))
    x1.append(math.log(n))

logarithmic(n)

end_time = time.time()
runTime1 = end_time - start_time
print("Execution time:", runTime1)


start_time = time.time()
def linearithmic(n):
    print(n*math.log(n))
    x2.append(n*math.log(n))

linearithmic(n)

end_time = time.time()
runTime2 = end_time - start_time
print("Execution time:", runTime2)


start_time = time.time()
def linear(n):
    print(n)
    x3.append(n)

linear(n)

end_time = time.time()
runTime3 = end_time - start_time
print("Execution time:", runTime3)


start_time = time.time()
def quadratic(n):
    print(n**2)
    x4.append(n**2)

quadratic(n)

end_time = time.time()
runTime4 = end_time - start_time
print("Execution time:", runTime4)


start_time = time.time()
def polynomial(n):
    print(n**4)
    x5.append(n**4)

polynomial(n)

end_time = time.time()
runTime5 = end_time - start_time
print("Execution time:", runTime5)


start_time = time.time()
def exponential(n):
    print(2**n)
    x6.append(2**n)

exponential(n)

end_time = time.time()
runTime6 = end_time - start_time
print("Execution time:", runTime6)



plt.plot([x1, x2, x3, x4,x5,x6], [runTime1, runTime2, runTime3, runTime4,runTime5,runTime6])



plt.xlabel('Value')
plt.ylabel('Runtime')
plt.title('Graph')

plt.show()
