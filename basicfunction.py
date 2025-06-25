def square_num(num):
   print(num**2)

square_num(6)
--------------------------------------------------------------------------------------------------------------------------
def square_of_num(num):
    return num**2

square_of_num(23)
--------------------------------------------------------------------------------------------------------------------------
#function with multiple parameter
def multiple(a,b):
  return a*b
multiple(23,34)
--------------------------------------------------------------------------------------------------------------------------
# polymorphism in function
def sum(p1,p2):
  return p1*p2
print(sum("prachi", 2))
--------------------------------------------------------------------------------------------------------------------------
#function return multiple values
#circle area and circumpherence
import math
def circle_stats(radius):
  area = math.pi*radius**2
  circumpherence=2*math.pi*radius
  return area,circumpherence
circle_stats(5)
--------------------------------------------------------------------------------------------------------------------------
#default parameter value
def greet(username):
  return "hello", username, "!"
print(greet('prachi'))


def greet(username='misti'):
  return "hello", username, "!"
print(greet())  
-----------------------------------------------------------------------------------------------------------------------------
#lambda function
cube = lambda x: x**3
cube(5)


def cube(num):
  return num**3
cube(9)
---------------------------------------------------------------------------------------------------------------------------
#function with *args
def sum_num(*args):
  return sum(args) # Use the built-in sum function to sum the arguments
print(sum_num(1,2,3,4))
--------------------------------------------------------------------------------------------------------------------------
#function with **kwargs
def print_kwargs(name,power):
 
    print(name='prachi', power=3)
------------------------------------------------------------------------------------------------------------------------------
#generator function with yeild
def even_generator(limit):
   for i in range (2, limit+1, 2):
     yield i
even_generator(10)
-----------------------------------------------------------------------------------------------------------------------------
#recursive function
def factorial(n):
  return 9*8*7*6*5*4*3*2*1

def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
