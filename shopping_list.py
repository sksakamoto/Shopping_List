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

def main():
	add_item("kale")
	remove_item("kale")

if __name__ == '__main__':
	main()