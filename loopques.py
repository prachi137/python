#counting positive numbers
numbers = [1,2,-3,7,-5,8]
positive_num_count = 0

for num in numbers:
   if num>0:
    positive_num_count+=1
print('final count', positive_num_count)
----------------------------------------------------------------------------------------------------------------------------------------------------
#sum of even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
for num in numbers:
  if num%2==0:
   even_count+=num
  print('final result', even_count)
----------------------------------------------------------------------------------------------------------------------------------------------------------
#multiplication table print
numbers = int(input("give the number:"))
for i in range(1,11):
  if i==5:
    continue
  print('numbers','x','i',"=", numbers*i)
------- --- -----------------------------------------------------------------------------------------------------------------------------------------------
#reverse a string
char = 'python'
reverse_char =''
for i in char:
  rverse_char = char+reverse_char
print(reverse_char)
------------------------------------------------------------------------------------------------------------------------------
#factorial calculator
number = 10
factorial =1
while number>1:
  factorial = factorial*number
  number-=1
  print(factorial)
  -----------------------------------------------------------------------------------------------------------------------
  #prime number cheacker
number = 29
is_prime = True
for i in range(2,number):
  if number%i==0:
    is_prime =False
    break
    print(is_prime)
 -------------------------------------------------------------------------------------------------------------------------------
#exponetial backoff
import time
wait_time = 1
max_retrives = 5
attempts = 0
while attempts<max_retrives:
  print('attempt', 'attempt+1', 'wait_time')
  time.sleep(wait_time)
  wait_time*=2
  attempts+=1
    
