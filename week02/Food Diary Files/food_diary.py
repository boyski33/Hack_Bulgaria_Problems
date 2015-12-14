import datetime
import json


def read_json():
	with open('food.json', 'r') as rfile:
		data = json.load(rfile)

		return data


def write_json(date, meal):

	temp = read_json() #get the json file

	if date in temp: #check if the current date is in the dict
		temp[date].append(meal)
	else: 
		lst = [] #create a list and add the meal to it
		lst.append(meal)
		temp[date] = lst #temp[date].append(meal) throws an exception! 

	with open('food.json', 'w') as wfile:
		json.dump(temp, wfile)


def add_meal(meal):
	now = datetime.datetime.now()
	now = "{}.{}.{}".format(now.day, now.month, now.year)

	write_json(now, meal)

def list_meals(date):
	data = read_json()
	if date in data: #prevent exceptions
		return '\n'.join(data[date])
	return "No entries for that date"


def main():
	
	command = ''

	while command != 'exit':
		text = input("Enter	a command > ").split() #creates a list of strings
		command = text[0]

		if command == 'meal':
			add_meal(text[1])
			print('OK Saved')
		elif command == 'list':
			print(list_meals(text[1]))



if __name__ == '__main__':
	main()
