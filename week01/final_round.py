#problem 1
def count_words(arr):
	occurence_dict = {}
	
	for i in range(len(arr)):
		if arr[i] not in occurence_dict:
			occurence_dict[arr[i]] = 1
		else:
			occurence_dict[arr[i]] += 1
	
	return occurence_dict
	
#problem 2
def nan_expand(times):
	
	if times == 0:
		return ''
	elif times == 1:
		return 'Not a NaN'
	else:
		return 'Not a ' + nan_expand(times - 1)

#problem 3 (not complete)
def iterations_of_nan_expand(expanded):
	return expanded.count("Not")

#problem 4
def group(int_list):	

	group_list = []
	current_list = []
	
	for i in range(len(int_list)):
		if int_list[i] not in current_list:

			if len(current_list) != 0:
				group_list.append(current_list[:])

			del current_list[:]
			current_list.append(int_list[i])
		else:
			current_list.append(int_list[i])	
	
	group_list.append(current_list)

	return group_list
	
#problem 5
def max_consecutive(items):
	m = 0
	curr_count = 1
	
	for i in range(len(items) - 1):
		if items[i] == items[i + 1]:
			curr_count += 1
			if curr_count > m:
				m = curr_count
		else:
			curr_count = 1

	return m

#problem 6
def gas_stations(distance, tank_size, stations):

	stations.append(distance)
	current_position = 0
	used_stations = []

	for i in range(len(stations)-1):

		if stations[i+1] > tank_size + current_position:
			used_stations.append(stations[i])
			current_position = stations[i]

	return used_stations


#problem 7
def sum_of_numbers(st):

	current_num = "0"
	sum = 0

	for i in range(len(st)):
		if st[i] >= '0' and st[i] <= '9':
			current_num += st[i]
		else:
			sum += int(current_num)
			current_num = "0"

	sum += int(current_num)		

	return sum

#problem8 (SMS problem)
def numbers_to_message(pressed_sequence):

	curr = 0

	for i in range(len(pressed_sequence)):
		while pressed_sequence[i] != -1:
			

