'''
Created on Jul 2, 2018

@author: adil
'''
#Overlapping subproblems property 

# Function to calculate nth Fibonacci number
#Memorization

def fib(n, lookup):
 
    # Base case
    if n == 0 or n == 1 :
        lookup[n] = n
 
    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup) 
 
    # return the value corresponding to that value of n
    return lookup[n]
# end of function
 
# Driver program to test the above function
def main():
    n = 101
    # Declaration of lookup table
    # Handles till n = 100 
    lookup = [None]*(1001)
    print "Fibonacci Number is ", fib(n, lookup)
 
if __name__=="__main__":
    main()