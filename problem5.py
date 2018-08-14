import numpy
import time

t0 = time.time()


ints = numpy.array(range(1,21))
primes = [2,3,5,7,11,13,17,19] # under 20
facts = []
for p in primes:
    counter = 0
    nums = ints
    while any(nums % p == 0):
        nums = nums / float(p)
        counter += 1
    facts.append(counter)

facts = numpy.array(facts)
mults = primes**facts
ans = 1
for m in mults:
    ans = m * ans

t1 =time.time()
perf = t1 - t0
print ("Problem 5\nAnswer:",ans, "runtime:", perf, "seconds")

"""Problem 5
Answer: 232792560 runtime: 0.00505399703979 seconds"""



##2520 is the smallest number that can be divided by each
##of the numbers from 1 to 10 without any remainder.
##What is the smallest positive number that is evenly
##divisible by all of the numbers from 1 to 20?
