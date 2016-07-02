def decode():
	decryptor = ""
	number = 0
	answer = raw_input('Gimme your code!\n')
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

print 'your message must be %s' % (decode())