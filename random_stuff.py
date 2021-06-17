'''
TODO: 	print div (\n ot ------)
		code cleanup
'''
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
		exit()

# number sort functionality
def numbersort():
	final_user_input_1 = user_input_type("Enter the first number: ", int)
	final_user_input_2 = user_input_type("Enter the first number: ", int)
	final_user_input_3 = user_input_type("Enter the first number: ", int)

	# create list
	num_list = [final_user_input_1, final_user_input_2, final_user_input_3]

	# sort into descending order
	num_list.sort(reverse=True)

	# print first number in list
	print(num_list[0])

# calculator functionality
def calculator():
	print("WIP")

while 1:
	# this program has multiple functions
	num_functions = 3
	functions = ["numbersort", "calculator", "exit"]

	temp = user_input_type("Enter the desired function\n\t1. %s\n\t2. %s\n\t3. %s\nFunction: "
							%(functions[0], functions[1], functions[2]), int)
	# Arrays start at 0
	temp = temp - 1


	# check validity of user selection
	'''
	# use i=0 for consistency, subtract 1 from num_functions to adjust for that
	i = 0
	while i <= (num_functions - 1):
		if temp == i:
			break
		i = i + 1
	else:
		print("Please enter a valid choice")
		exit()
	'''

	# valaidity check v2
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

