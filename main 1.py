1.1 the calculate the factorial of a given number

...
1! = 1 * 1
2! = 2 * 1! --->2 * 1
3! = 3 * 2! --->3 * 2 * 1
.
.
  10!




def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n* fact _rec(n-1)
    
number=2
res=fact_rec(number)

print (*"the factorial of {} is {}.". format (number,res))
