def encrypt(key):
	#key %= 26
	def accepter(func):
		def decorated():
			input_str = func()
			result = ""
			for i in range(len(input_str)):
				if not input_str[i].isalpha(): # ingore punctuation
					result += input_str[i]
					continue
				if ord(input_str[i]) + key > ord('z'): # "loop" back if over 'z'
					result += chr(ord(input_str[i]) - (26 - key))
				else:
					result += chr(ord(input_str[i]) + key)
			return result
		return decorated
	return accepter


@encrypt(2)
def get_low():
	return "Get get get low"

print(get_low())
