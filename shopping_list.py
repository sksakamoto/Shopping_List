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
		else:
			add_item(raw_input("What do you want to add? "))
#	add_item("kale")
#	remove_item("kale")

if __name__ == '__main__':
	main()
