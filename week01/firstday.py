#problem 1
def sum_of_digits(n):
	n = abs(n)
	digit_sum = 0

	while n != 0:
		digit_sum += n % 10
		n //= 10
		print(n)

	return digit_sum

#problem 2
def to_digits(n):
	digits = []

	while n > 0:
		digits.append(n % 10)
		n //=10

	return digits[::-1] #returns the list reversed

#problem 3
def to_number(digits):
	number = ""

	for i in range(len(digits)):
		number += str(digits[i])

	return int(number)

#problem 4
def fact_digits(n):
	sum_fact = 0

	while n > 0:
		sum_fact += factorial(n % 10)

		n //= 10

	return sum_fact

def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num - 1)

#problem 5
def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fibonacci(n):
	fib_list = []

	for i in range(1, n+1):
		fib_list.append(fib(i))

	return fib_list

#problem 6
def fib_number(n):
	fib_string = ""

	a, b = 1, 1

	for i in range(n+1):
		fib_string += str(a)
		a, b = b, (a + b)

	return fib_string

#problem 7
def palindrome(obj):
	obj_reversed = str(obj)[::-1]

	return str(obj) == obj_reversed

#problem 8
def count_vowels(s):
	count = 0
	vowels = "aeiouy"

	for i in range(len(s)):
		if s[i] in vowels:
			count += 1

	return count

#problem 9
def count_consonants(s):
	count = 0
	consonants = "bcdfghjklmnpqrstvwxz"

	for i in range(len(s)):
		if s[i].lower() in consonants:
			count += 1

	return count

#problem 10
def char_histogram(some_string):
	histogram = {}

	for i in range(len(some_string)):
		if some_string[i] not in histogram:
			histogram[some_string[i]] = 1
		else:
			histogram[some_string[i]] += 1

	return histogram
