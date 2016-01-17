import copy

#problem 1
def is_number_balanced(num):
	list_digits = []
	left = 0
	right = 0
	
	for i in range(len(str(num))):
		list_digits.append(num % 10)
		num /= 10
		
	print (list_digits)
		
	for i in range(len(list_digits) / 2):
		left += list_digits[i]
		#print 'left = %s' %left
		
	for i in range(len(list_digits)-1, (len(list_digits)/2 - 1) + len(list_digits)%2,-1): 
		right += list_digits[i]
		#print 'right = %s' %right
		
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
	
	for i in range(len(num_string)//2):
		if num_string[i] != num_string[len(num_string)-(i + 1)]:
			p = False
	
	return p
	
#problem 4
def prime_numbers(n):

	numbers = [0 for x in range(n)] #list of zeros 

	i = 2

	while i < n:
		if numbers[i] == 0:
			print(i)
			j = i*i
			while j < n:
				numbers[j] = 1 #change all the numbers on positions divisible by the current number to 1 
				j += i

		i += 1	
	
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
def birthday_ranges(birthdays, ranges):
	
	result = [0] * len(ranges) #list initialized with zeros

	for i in range(len(ranges)):
		for j in range(len(birthdays)):
			if birthdays[j] >= ranges[i][0] and birthdays[j] <= ranges[i][1]:
				result[i] += 1

	return result


#problem 7
def sum_matrix(m):
	m_sum = 0

	for i in m:
		for j in i:
			m_sum += j

	return m_sum

#problem 8

NEIGHBORS = [
(-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
(-1, 0), (1, 0),  # Get to 8 and 7
(-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


#problem 9
def is_transversal(transversal, family):

	family_flags = [0 for x in range(len(family))]

	for element in transversal:
		for i in range(len(family)):
			for el in family[i]:
				if element == el:
					family_flags[i] = 1
					break

	for flag in family_flags:
		if flag == 0:
			return False


	return True
