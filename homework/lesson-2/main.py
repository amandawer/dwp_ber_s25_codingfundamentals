#Variables and basic data types
my_number = 10
my_string = "Hello, Python"
my_float = 3.14

print("Number:", my_number)
print("String:", my_string)
print("Float:", my_float)

#Different data Types
#A
first_name = "Amanda"
last_name = "Wer Estrada"
full_name = first_name + " " + last_name
print("Full name:", full_name)

#B
a = 5
b = 3
add_result = a + b
sub_result = a - b
mult_result = a * b
div_result = a / b
print("addition:", add_result)
print("subtraction:", sub_result)
print("multiplication:", mult_result)
print("division:", div_result)

#Booleans and Comparisons

is_greater = 5 > 3
is_equal = 5 == 3
is_smaller = 5 < 3
print("Is greater:", is_greater)
print("Is equal:", is_equal)
print("Is smaller:", is_smaller)

bool1 = True
bool2 = False
and_result = bool1 and bool2
or_result = bool1 or bool2

print("And:", and_result)
print("Or:", or_result)

#Comparison of pi

pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"

print("Are pi and pi_pi equal?", pi == pi_pi) 
#no, because pi is a number, pi_pi is a string
print("Are pi_pi and pi_pi_pi equal?", pi_pi == pi_pi_pi)
#yes, both are strings

print(type(pi))
print(type(pi_pi))
print(type(pi_pi_pi))

#Type Conversion
my_str = 123
my_int = int(my_str)
my_float_converted = float(my_int)

print("my_str:", my_str)
print("my_int:", my_int)
print("my_float_converted:", my_float_converted)

#Challenge

celsius = 37
fahrenheit = (celsius * 9/5) + 35
print("celsius to fahrenheit:", celsius, "=", fahrenheit)