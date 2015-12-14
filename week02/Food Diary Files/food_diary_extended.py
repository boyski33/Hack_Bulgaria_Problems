import datetime
import json


def read_json(filename):
	with open(filename, 'r') as rfile:
		data = json.load(rfile)

		return data


def write_json(date, meal):

	temp = read_json('food.json') #get the json file

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
	data = read_json('food.json')
	if date in data: #prevent exceptions
		return '\n'.join(data[date])
	return "No entries for that date"


def main():
	
	command = ''

	calories_dict = {}
	calories_dict = read_json('calories.json')

	while command != 'exit':
		text = input("Enter	a command > ").split() #creates a list of strings
		command = text[0]

		if command == 'meal':
			meal = text[1]
			add_meal(meal)
			print('OK Saved')

			amount = 0

			text = input("How much have you eaten? > ")
			if text.endswith('kg'):
				amount = int(text[:-2])*1000
			elif text.endswith('g'):
				amount = int(text[:-1])

			meal_cals = 0
			meal_cals = calories_dict[meal]
			meal_cals = meal_cals * amount/100
			
			print(amount)
			print(meal_cals)


		elif command == 'list':
			print(list_meals(meal))

		
			

				



				


if __name__ == '__main__':
	main()
