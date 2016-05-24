
#add_item(str(raw_input("What do you want to add to the list? ")))
#remove_item("MILK")

"""def add_item(item):
	if item not in shopping_list:
		shopping_list.extend(item)
		print sorted_list(shopping_list)
	else: print "This item is already on the list!"

def sorted_list(shopping_list):
	return sorted(shopping_list)

add_item(["cereal", "chocolate"])"""



shopping_list = ["cereal", "milk"]

def add_item(item):
	if item.lower() not in shopping_list:
		shopping_list.append(item.lower())
		print sorted_list(shopping_list)
	else: print "This item is already on the list!"

def sorted_list(shopping_list):
	#return sorted(shopping_list)
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

	#my_list = ["apple", "cheese", "bacon"]

#def sorted_list(my_list):
#	print sorted(my_list)

#sorted_list(my_list)

#shopping_list = ["bread", "apple"]

#def add_item(item):
#	if item.lower() not in shopping_list:
#		shopping_list.append(item)
#		print sorted_list(shopping_list)
#	else: print "This item is already in your cart!"

#def sorted_list(shopping_list):
#	return sorted(shopping_list)
	


	#print sorted_list

#def main():
#	add_item("apple")

#if __name__ == "__main__":
#main()

add_item("bread")

shopping_list = ["bread", "apple"]

def add_item(item):
	if item.lower() not in shopping_list:
		shopping_list.append(item)
	else: print "This item is already in your cart!"
	return shopping_list

def sorted_list(shopping_list):
	shopping_list.sort()
	return shopping_list
	


	#print sorted_list

#def main():
#	add_item("apple")

#if __name__ == "__main__":
#main()

add_item("banana")
sorted_list(shopping_list)
print shopping_list
