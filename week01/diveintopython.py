#problem 1
def is_balanced(num):
	list_digits = []
	left = 0
	right = 0
	
	for i in range(len(str(num))):
		list_digits.append(num % 10)
		num /= 10
		
	print (list_digits)
		
	for i in range(len(list_digits) / 2):
		left += list_digits[i]
		print ('left = %s' %left)
		
	for i in range(len(list_digits)-1, (len(list_digits)/2 - 1) + len(list_digits)%2,-1): 
		right += list_digits[i]
		print ('right = %s' %right)
		
	if left == right:
		return True
	else:
		return False

#problem 2.1
def is_increasing(seq):
	increasing = True
	
	for i in range(len(seq)-1):
		if seq[i] >= seq[i+1]:
			increasing = False
			
	return increasing
	
#problem 2.2
def is_decreasing(seq):
	decreasing = True
	
	for i in range(len(seq)-1):
		if seq[i] <= seq[i+1]:
			decreasing = False
			
	return decreasing
	
#problem 3
def get_largest_palindrome(n):
	largest_palindrome = 1
	
	for i in range(n):
		if is_palindrome(i) and i > largest_palindrome:
			largest_palindrome = i
	
	return largest_palindrome
	
def is_palindrome(n):
	num_string = str(n)
	p = True
	
	for i in range(len(num_string)/2):
		if num_string[i] != num_string[len(num_string)-(i + 1)]:
			p = False
	
	return p
	
#problem 4
def prime_numbers(n):
	num_list = []
	prime_list = []

	for i in range(2, n+1):
		num_list.append(i)





	print(num_list)
	
	
	
	
#problem 5
def is_anagram(a, b):
	a = a.lower()
	b = b.lower()
	a_map = {}
	b_map = {}
		
	for i in range(len(a)):
		if a[i] not in a_map:
			a_map[a[i]] = 1
		else:
			a_map[a[i]] += 1

	for i in range(len(b)):
		if b[i] not in b_map:
			b_map[b[i]] = 1
		else:
			b_map[b[i]] += 1

	return a_map == b_map		

#problem 6		

#problem 7

	
	
print(is_anagram('LettEr', 'TEETRL'))

