#days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
#today = None

#def prompt_user():
#	global today
#	today = raw_input("What day is it today?")
#	return today

#def display_tomorrow(item):
#	global today
#	for i in range(len(days_of_week)):
#		print "Tomorrow is", days_of_week[(days_of_week.index(today)) + 1]

#prompt_user()
#display_tomorrow(today)

days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def prompt_user():
	return raw_input("What day is it today? ")

def display_tomorrow(today):
	tomorrow = (days_of_week.index(today) + 1) % len(days_of_week)
#	if tomorrow > 6:
#		tomorrow == 0
	print "Tomorrow is", days_of_week[tomorrow]

def main():
	my_today = prompt_user()
	display_tomorrow(my_today)

#	display_tomorrow(prompt_user())

if __name__ == '__main__':
	main()