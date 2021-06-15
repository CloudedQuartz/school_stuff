
'''
user_input_eval(str, type):
	Take input with input_text then use eval. if input is not
	a defined type, return as string
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
		print("Please enter with proper type")
		return

final_user_input = user_input_type("Input a test number (int): ", int)
if final_user_input != None:
	if final_user_input % 2 == 0:
		print("Number %d is even" %final_user_input)
	else:
		print("Number %d is odd" %final_user_input)

