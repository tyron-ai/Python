#Program to check if a set of six numbers is a pair of geographical/GPS coordinates or not, assuming the degrees/minutes/seconds form:
#40º20'21" N 79º58'36" W
#The six numbers represent, in sequence: latitude degrees, latitude minutes, latitude seconds, longitude degrees, longitude minutes and longitude seconds. 
#Program must uses negative number to represent degrees in the southern and western hemispheres.

number1 = eval (input ("Enter first number:\n"))
number2 = eval (input ("Enter second number:\n"))
number3 = eval (input ("Enter third number:\n"))
number4 = eval (input ("Enter fourth number:\n"))
number5 = eval (input ("Enter fifth number:\n"))
number6 = eval (input ("Enter sixth number:\n"))

if (number1 >= -90) and (number1 <= 90) and (number2 >= 0) and (number2 <= 59) and (number3 >= 0) and (number3 <=59) and (number4 >= -180) and (number4 <= 180) and (number5 >= 0) and (number5 <= 59) and (number6 >= 0) and (number6 <=59):
   print ("WOW! Looks like geographic coordinates!")
else:
   print ("Hmmm ... looks like 6 random numbers.")

   