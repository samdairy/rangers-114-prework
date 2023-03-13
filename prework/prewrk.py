#question 1
#writ a foction  to print "hello_USERNAME!" USERNAME is the input of the function . the first lin of the code has been definedas below.

def hello_name(user_name):
    print("hello," + user_name()+ "!")


#question 2
#writ a python functino ,first_odds that print the odd numbers from 1-100 and returns nothing

number = 1
while number < 101:
   if number% 2 == 1:
      print(number)
      number += 1
   else:
      number += 1
         




#question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
   max_number = max(a_list)
   return max_number

test =  max_num_in_list in list([4,5,20,8,10])
print(test)








#question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def  is_leap_year(a_year):
    if a_year % 4 == 0:  
      if a_year % 100 == 0: 
         if a_year % 400 == 0:
          return True
            

# question 5            
#Write a function to check to see if all numbers in list are consecutive numbers. For example, 
# [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
   test=a_list[0]
   for i in a_list:
      if i == test:
         test = test+1
      else:
         return False
   return True
