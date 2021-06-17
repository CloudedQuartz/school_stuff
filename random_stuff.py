
# simple (hopefully exception free) input function
'''
user_input_type(str, type):
	Take input with input_text then convert to input_type.
	if input does not match type, catch exception and
	return None.
	Returns "None" if -
	1. input_text (first argument) is not str
	2. usr_inp doesnt match out_type
'''
def user_input_type(input_text, out_type):
	# Check input text type
	if type(input_text) != str:
		return

	# assign to user_inp
	usr_inp = input(input_text)

	# try to convert to out_type, if exception return None.
	try:
		return out_type(usr_inp) 
	except:
		print("Please enter with proper type (%s)" %out_type)
		return
		

# maximum value finder
def numbermax():
	print("Maximum value finder")
	num_1 = user_input_type("Enter the first number: ", int)
	num_2 = user_input_type("Enter the second number: ", int)
	num_3 = user_input_type("Enter the third number: ", int)

	# user_input_type can be None
	if num_1 == None or num_2 == None or num_3 == None:
		print("Invalid value")
		return

	# create list
	num_list = [num_1, num_2, num_3]

	# sort into descending order
	num_list.sort(reverse=True)

	# print first number in list as it is highest
	print(num_list[0])

# calculator
def calculator():
	print("Calculator")
	# convert to string for concat
	num_1 = str(user_input_type("Enter the first number: ", float))
	num_2 = str(user_input_type("Enter the second number: ", float))
	operator = user_input_type("Enter the operator: ", str)

	# user_input_type can be None
	if num_1 == None or num_2 == None or operator == None:
		print("Invalid value")
		return

	# allowed operators
	# this is used to prevent security issues in eval()
	valid_operators = ["+", "-", "*", "/", "//", "**", "%"]
	if operator in valid_operators:
		calc = num_1 + operator + num_2
		print("The result is %d" %eval(calc))
	else:
		print("Please enter a valid operator")

while 1:
	# this program has multiple functions
	num_functions = 3
	functions = ["numbermax", "calculator", "exit"]

	temp = user_input_type("Enter the desired function\n\t1. %s\n\t2. %s\n\t3. %s\nFunction: "
							%(functions[0], functions[1], functions[2]), int)

	# user_input_type returns none in 2 conditions
	if temp == None:
		continue
	
	# Arrays start at 0
	temp = temp - 1


	# check validity of user selection
	try:
		# eval is safe to use as user there are few set possibilities only
		eval(functions[temp])()
	# special systemexit case is necessary as exit() causes exception.
	# raise the exception in this case.
	except SystemExit:
		raise
	except:
		print("Please enter a valid choice")
		continue

