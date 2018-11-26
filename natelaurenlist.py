import random
import pickle

optiona = "\nAdd to the list"
optionb = "\nHere's the list, what did you end up doing?\n"
optionc = "\nLet's get you a date.\n\n"
option0 = "EXIT"
fileObject = open('Date List', 'rb')
natelaurenlist = pickle.load(fileObject)

def mainmenu():
	while(True):
		initialprompt = input("\nWelcome to the ultimate list maker! Please select one of the following options.\n A: Add more to this awesome list.\n B: Check something off this awesome list.\n C: Random date activity please.\n Press 0 to exit\n So what do you want to do?\n" )


#when user selects A, it allows for the user to add an item to the list and then subsequently prints the list for them to view
		if initialprompt == "A" or initialprompt == "a" or initialprompt == " a" or initialprompt == " A" :
				newdate = str(input("add a date: "))
				natelaurenlist.append(newdate)
				print("\n".join(natelaurenlist))
				File_Name = "Date List"
				fileObject = open(File_Name, 'wb')
				pickle.dump(natelaurenlist, fileObject)
				fileObject.close()
				fileObject = open(File_Name, 'rb')
	
	
#when user selects B, they should be able to pop any item off the list into the completed section and then add any details they would like
		elif initialprompt == "B" or initialprompt == "b" or initialprompt == " B" or initialprompt == " b":
			input((optionb) + ("\n".join(natelaurenlist)))
	
	#Need to figure this part out, potentially would want to pop the item off the date list into a completed list for reference
		
	
#When user selects C, they get a random date activity from the list. 	
		elif initialprompt == "C" or initialprompt == "c" or initialprompt == " C" or initialprompt == " c":
			print(optionc + random.choice(natelaurenlist))
			
		elif initialprompt == "0" or initialprompt == " 0":
			print("Have a nice day!")
			quit()
	
	
		else:
			print("fuck you kyle")
mainmenu()
