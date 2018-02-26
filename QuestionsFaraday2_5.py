#!/bin/python

# Questions 2 - 5
import operator as ops ## Problem 5
import re ## Problem 2

### Problem 2
def convert(val=''):
	## Error handling, if user tries to enter invalid arguments
	try:
		if re.match("^\d+?\.\d+?$", val) is not None: # Regex to check if the string really is a float
			return float(val)
		elif val.isdigit(): #If the argument is purely numbers (e.g. a Integer)
			return int(val)
		else:
			return str(val) #Otherwise return a string value (Mixture of numbers, periods, and letters)
	except:
		print "Argument provided is invalid - please enter a string as argument"

### Problem 4
### Just check the first two numbers to see if they satisfy the minimum requirement
### Can just return the third, since we know for sure it is  smaller than the first two. 
def minOfThree(num1, num2, num3):
	if num1 < num2 and num1 < num3:
		return num1
	elif num2 < num1 and num2 < num3:
		return num2
	else:
		return num3


### Problem 5
def apply_operation(left_operand, right_operand, operator):
	if operator == '+':
		return left_operand + right_operand
	elif operator == '-':
		return left_operand - right_operand
	elif operator == '*':
		return left_operand * right_operand
	elif operator == '/':
		return left_operand / right_operand

### One method - using a lookup table
def apply_operation_reformed(left_operand, right_operand, operator):
	op = { '+': ops.add, '-': ops.sub, '*':ops.mul, '/':ops.div }
	return op[operator](left_operand, right_operand)

### SIDE NOTE:
### Eval is usually unsafe, but would make this easier, but we want to be safe
### Eval option -> return eval(str(left_operand) + operator + str(right_operand))

### Similar to apply_operation_reformed(), but uses python lambdas to do the operation
def apply_operation_reformed2(left_operand, right_operand, operator):
	ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}
	return ops[operator](left_operand, right_operand)

# This code is easy to scale and reuse, since there is no need to write if statements for
# additional cases. Just add a entry to the dictionary and that's all. 	



if __name__ == "__main__":

	### Problem 2 Test Cases
	# print type(convert(1))
	# print type(convert('1.0'))
	# print type(convert('test'))
	# print type(convert('1.2testStr'))
	# print type(convert('1.2t23...2tttt'))
	# print type(convert('1.234523'))
	# print type(convert('1.'))
	# print type(convert('123523'))

	### Problem 3
	# Memory is not utilized efficiently when declaring variables only for printing
	# Just have the output format the list directly, efficiently used and less heap space
	output1 = ('{a[1]} the {a[0]} is {a[2]} years old'.format(a=abc))

	### Problem 4 Test Cases
	# print minOfThree(55,322,55)


	### Problem 5 Test Cases
	# print apply_operation(2,3,'+')
	# print apply_operation_reformed(2,3, '+')
	# print apply_operation_reformed2(2,3,'*')