
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
