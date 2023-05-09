import matplotlib.pyplot as plt
import numpy as np

def SieveOfEratosthenesModified(n,ln=2):
    #modified version of geeksforgeeks implementation
    prime = [True for i in range(n + 1)]
    numOfPrimesPer1k = []
    primeArr = []
    numOfPrimes=0
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(ln, n + 1):
        if prime[p]:
            numOfPrimes+=1
            primeArr.append(p)
        if p%1000==0:
            numOfPrimesPer1k.append(numOfPrimes)
            numOfPrimes = 0
    return primeArr, numOfPrimesPer1k
def twinPrimeFinder(primes):
    numOfTwinPrimesPer1k = []
    numOfTwinPrimes = 0
    val = 1
    for prime in primes:
        if prime + 2 in primes:
            numOfTwinPrimes+=1
        if prime >= 1000*val:
            numOfTwinPrimesPer1k.append(numOfTwinPrimes)
            numOfTwinPrimes = 0
            val+=1
    return numOfTwinPrimesPer1k

if __name__ == '__main__':
    x = 1000500
    primeArray = SieveOfEratosthenesModified(x)
    primePer1k = primeArray[1]
    primeArray = primeArray[0]
    twinPrimePer1k = twinPrimeFinder(primeArray)
    #initialize y axis
    kCount = []
    for i in range(len(primePer1k)):
        kCount.append(i+1)
    #initialize x axis for both primes and twin rpiems
    xValsPrime = np.array(primePer1k)
    xValsTwin = np.array(twinPrimePer1k)
    #plot 1 - twin primes
    plt.subplot(1, 2, 1)
    plt.scatter(xValsTwin, kCount,marker=".", color='red')
    plt.ylabel("Range from (y*10^3-1000) to y*10^3")
    plt.xlabel("Number of twin primes per 1000")
    #plot 2 - primes
    plt.subplot(1, 2, 2)
    plt.scatter(xValsPrime, kCount, marker=".")
    plt.xlabel("Number of primes per 1000")
    plt.show()