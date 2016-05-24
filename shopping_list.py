shopping_list = ["cereal", "milk"]

def add_item(item):
	if item.lower() not in shopping_list:
		shopping_list.append(item.lower())
		print sorted_list(shopping_list)
	else: print "This item is already on the list!"

def sorted_list(shopping_list):
	shopping_list.sort()
	return shopping_list

def remove_item(item):
	if item.lower() in shopping_list:
		shopping_list.remove(item.lower())
		print sorted_list(shopping_list)
	else: print "This item is not on the list!"
	
def menu():
	global menu_choice
	menu_choice = raw_input("What would you like to do? 0 - Main Menu, 1 - Show Current List, 2 - Add an Item to List ")
	return menu_choice

def parsed_string(item_string):
	new_items = item_string.split(",")
	for item in new_items:
		if item.lower() not in shopping_list:
			shopping_list.append(item.lower())
			print sorted_list(shopping_list)
		else: print "This item is already on the list!"

def main():
	while(True):
		print "Type exit to exit"
		menu()
		if menu_choice == "exit":
			break
		elif menu_choice == 0:
			None
		elif menu_choice == 1:
			print shopping_list
		elif menu_choice == 2:
			input_answer = raw_input("What do you want to add? ")
			if "," in input_answer:
				parsed_string(input_answer)
			else: add_item(input_answer)
		else:
			print "Sorry, I don't understand."

if __name__ == '__main__':
	main()
