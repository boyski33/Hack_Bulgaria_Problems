class Fraction:

	def __init__(self, numerator, denominator):
		self._numerator = numerator
		self._denominator = denominator

	def __str__(self):
		return "{} / {}".format(int(self._numerator), int(self._denominator))

	def __float__(self):
		return float("{:.2f}".format(self._numerator / self._denominator))

	def __repr__(self):
		return self.__str__()

	def __neg__(self):
		"""Helps with __sub__"""

		return Fraction(-self._numerator, self._denominator)

	def simplify(self):
		"""So that 8/12 becomes 2/3"""

		gcf = Fraction.GCF(self._numerator, self._denominator)

		self._numerator /= gcf
		self._denominator /= gcf

		#return self.__str__()

	def GCF(a, b): 
		"""Euclidian algorithm"""

		a, b = max(abs(a), abs(b)), min(abs(a), abs(b)) #in case we have negative fractions

		r = a % b

		while r > 0:
			a = b
			b = r
			r = a % b

		return b

	def LCM(a, b):
		"""Least Common Multiple
		for help with __add__ and __sub__"""

		return (a * b) / Fraction.GCF(a, b)

	def __eq__(self, other):
		"""Maybe not the best way to do it, but that way it
		considers 1/3 and -1/-3 as the same number."""

		return self.__float__() == other.__float__()

	def __add__(self, other):
		"""Check if denominators are same to make it more simple.
		If different, find the LCM of the denominators and then multiply the 
		numerator by the LCM divided by its respective denominator. Then use the 
		LCM as the new denominator and the sum of self._numerator and
		other._numerator as the new numerator"""

		if self._denominator == other._denominator:
			num = self._numerator + other._numerator
			denom = self._denominator

			result = Fraction(num, denom)
			result.simplify()

			return result.__str__()

		else:
			lcm = Fraction.LCM(self._denominator, other._denominator)

			s_num = self._numerator * (lcm / self._denominator)
			o_num = other._numerator * (lcm / other._denominator)

			result = Fraction((s_num + o_num), lcm)
			result.simplify()

			return result.__str__()

	def __sub__(self, other):
		
		return self.__add__(-other)

	def __mul__(self, other):	

		num = self._numerator * other._numerator
		denom = self._denominator * other._denominator

		result = Fraction(num, denom)

		result.simplify()

		return result.__str__()


def main():
	pass






if __name__ == "__main__":
	main()

