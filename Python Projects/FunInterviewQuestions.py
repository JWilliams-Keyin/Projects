

def fizz_bizz():
   '''
   To solve the FizzBuzz problem with the additional "Bizz" condition for
   numbers divisible by 8
   '''
   # loop shows from 1 to 100 inclusive
   for i in range(1, 101): 
       
   # if number is divisible by both 5 and 8. If true, print "FizzBizz"    

       if i % 5 == 0 and i % 8 == 0 :  
           
           print("FizzBizz") 

#if the number is divisible by 5. If true, print "Fizz"
       elif i % 5 == 0: 
           
           print("Fizz")

# if the number is divisible by 8. If true, print "Bizz"
       elif i % 8 == 0: 
           print("Bizz")
       else:
           
 # If none of the above conditions are true, print the number itself          
         print(i) 

fizz_bizz()

