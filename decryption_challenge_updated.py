#decryption function
def decode():
	#I want the letter characters saved in a string
	decryptor = ""
	number = 0
	answer = raw_input('Gimme your code!\n')
	'''for loop goes through each character in answer and decides if it is a letter, number, or symbol.
	 If letter save it in decryptor.'''
	for letter in answer:
		number = number - 1
		if letter.isdigit():
			number = int(letter)
		elif number == -1 and letter.isalpha() == True:
			decryptor += decryptor.join(letter).strip()	
		elif not letter.isalnum():
			print 'Please use only letters and numbers.'
			return decode()
	return decryptor

print 'Is your message %s?' % (decode())


