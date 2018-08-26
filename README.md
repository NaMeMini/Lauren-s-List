# Lauren-s-List
A random date generator for myself and Lauren

import random

optiona = "\nAdd to the list"
optionb = "\nNoiceeee. Here's the list, what did you end up doing?\n"
optionc = "\nWay to not have a sweet idea nerd. I'll get you one."
natelaurenlist = ["Cat cafe", "tilt(pinball)", "do a puzzle", "go to WI and buy fireworks", "do origami", "cook dinner", "cook breakfast", "cook dinner", "cook dessert", "rob a place w/your van", "push up contest!", "pie eating contest", "trvia night!", "go to a libraryu and read in silence", "go to the library and read in noise", "go to the archery/gun range", "ice cream and scallops", "go to the casino and gamble", "play road trip games", "look at crazy stuff on the interenet", "puddle jump", "go rock climbing", "find something that neither of us have done and do that", "thrift shop", "draw together", "mad libs", "hiking", "try eating insanely spicy peppers", "cross country skiing", "learn to surf", "go to the zoo", "statue mountain island", "go for a run", "MOA and poeple watch", "walk and food and walk", "Hmong village", "get crazy haircuts/dye hair", "wine and paint", "winery/brewery", "play Oregon trail", "game night!", "see how many random buildings we can walk into", "dinner and show", "buy our respective families gifts", "vinegar and baking soda volcano", "plant a tree", "make to do lists together", "remodel my bathroom"]

initialprompt = input("Welcome to the ultimate list maker! Please select one of the following options.\n A: Add more to this awesome list.\n B: Check something off this awesome list.\n C: Random date activity please.\n So what do you want to do?\n" )
if initialprompt == "A" or initialprompt == "a" or initialprompt == " a" or initialprompt == " A" :
	print(optiona)
elif initialprompt == "B" or initialprompt == "b" or initialprompt == " B" or initialprompt == " b":
	print((optionb) + ("\n".join(natelaurenlist)))
elif initialprompt == "C" or initialprompt == "c" or initialprompt == " C" or initialprompt == " c":
	print(random.choice(natelaurenlist))
else:
	print("please just enter a letter.")
	

#import random
#natelaurenlist = ["Cat cafe", "tilt(pinball)", "do a puzzle", "go to WI and buy fireworks", "do origami", "cook dinner", "cook breakfast", "cook dinner", "cook dessert", "rob a place w/your van", "push up contest!", "pie eating contest", "trvia night!", "go to a libraryu and read in silence", "go to the library and read in noise", "go to the archery/gun range", "ice cream and scallops", "go to the casino and gamble", "play road trip games", "look at crazy stuff on the interenet", "puddle jump", "go rock climbing", "find something that neither of us have done and do that", "thrift shop", "draw together", "mad libs", "hiking", "try eating insanely spicy peppers", "cross country skiing", "learn to surf", "go to the zoo", "statue mountain island", "go for a run", "MOA and poeple watch", "walk and food and walk", "Hmong village", "get crazy haircuts/dye hair", "wine and paint", "winery/brewery", "play Oregon trail", "game night!", "see how many random buildings we can walk into", "dinner and show", "buy our respective families gifts", "vinegar and baking soda volcano", "plant a tree", "make to do lists together", "remodel my bathroom"]
#random.choice(natelaurenlist)


