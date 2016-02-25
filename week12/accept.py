def accepts(*args):
	def get_accepts(func):
		def check_type(*given_args):
			for i in range(len(args)):
				if args[i] != type(given_args[i]):
					raise TypeError("Argument {} of {} in not {}".format(i+1, func.__name__, args[i].__name__))
			return func(*given_args)
		return check_type
	return get_accepts
