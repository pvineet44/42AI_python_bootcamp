import random
import sys

def generator(text, sep, option=None):
	"""Option is optional, sep is a seperator which will be used 
	to split text"""

	if (option != None and option != "shuffle" and option != \
		"unique" and option != "ordered" ):
		print("ERROR")
		sys.exit(0)
	split_text = text.split(sep)
	if option is "shuffle":
		random.shuffle(split_text)
	if option is "unique":
		split_text = set(split_text)
	if option is "ordered":
		split_text.sort(reverse = True)
	for split in split_text:
		yield(split)


text ="Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
	print(word)
