#Authored by Melissa Wall and Jacob Dorman

from AreaModule import Area
import sys
import os
import pickle
import random
import textwrap

#Globals
#A reference to the current area
area = None
#An area map that will hold references to areas
areaMap = {}
#Whether the player is in a building or not
inBuilding = False

#Formats the message to fit our style
def format(message):
	return "|*| " + "\n|*| ".join(textwrap.wrap(message))


def feastMiniGame():
	global inBuilding
	global areaMap
	global hint
	print format(
'''Your hunger is insatiable as you enter the Hall of Feasts and stand in the lobby. The gatekeepers lie between you and this corridor of delicacies. You approach the gatekeeper and ask if you may be allowed inside. "Certainly," she says. "...provided that you can answer my three riddles."''')
	riddles = {
"fire":
'''I am always hungry, I must always be fed. 
The finger I lick will soon turn red.''',
"egg":
'''A box without hinges, key or lid, Yet golden treasure inside is hid.''',
"fish":
'''Alive without breath,
As cold as death;
Never thirsty, ever drinking,
All in mail never clinking.''',
"corn":
'''Throw out my outer.
Keep my inner.
Eat my outer.
Throw out my inner.''',
"onion":
'''You use a knife to slice my head and weep beside me when I am dead.''',
"potato":
'''What has eyes but never looks?''',
"pear":
'''What fruit resembles two?''',
"toast":
'''You eat me, you drink me; describe me, who can;
I'm sometimes to a woman, and sometimes to a man.''',
"jelly bean":
'''Like all beans, I am small and round; but unlike others,
I dont grow in the ground.''',
"blueberry":
'''What do you call a sad cranberry?'''
	}
	alreadyAsked = []
	for x in range(3):
		print ""
		answer = random.choice(riddles.keys())
		while answer in alreadyAsked:
			answer = random.choice(riddles.keys())
		alreadyAsked.append(answer)
		question = riddles[answer]
		print question
		guess = raw_input("What is your answer? ").lower()
		while guess != answer:
			print "Wrong! Try again."
			guess = raw_input("What is your answer? ").lower()
	print "|*| " + "\n|*| ".join(textwrap.wrap("The gatekeeper moves aside to grant you passage. You pile your plate high and go back for seconds, thirds, and fourths. Finally, filled with meats, desserts, and self-loathing, you make your way to the exit."))
	inBuilding = False
	thisArea = areaMap["Hall of Feasts"]
	del thisArea.miniGame
	thisArea.inside_desc = "You have already found what you were looking for here. There is no need to go back for seconds."
	areaMap["Hall of Knowledge"].miniGame = wisdomMiniGame
	print format("Now that your hunger is sated, you should seek the Opal of Wisdom. It is rumored to be hidden deep in the Hall of Knowledge, which stands ominously at the northern peak of the realm.")

def wisdomMiniGame():
	global areaMap
	global inBuilding
	print format('''You enter the Hall of Knowledge. Long corridors extend as far as the eye can see, flanked by shelves of books on either side. Each row of shelves carries a label with a number; there must be at least a thousand (1000). You can feel that the Opal of Wisdom is here, beckoning to you. You can sense its force upon you changing, as you move throughout the shelves. Maybe you can narrow down its location.
''')
	answer = random.randrange(1000) + 1
	print ""
	guess = int(raw_input("Where would you like to start? "))
	while int(guess) != int(answer):
		if int(guess) < int(answer):
			print "You feel like the force upon you is lessening. Maybe try going to a higher-numbered shelf."
		else:
			print "You feel like the force upon you is lessening. Maybe try going to a lower-numbered shelf."
		guess = raw_input("Next guess? ")
	print format("You approach the shelf numbered " + str(answer) + ". Your gaze is immediately drawn to an old-looking book. You pick it up and open it, and find that the insides have been hollowed out to make a secret compartment. Inside lies the Opal of Wisdom. You pick it up and feel confidence and enlightenment surging through you. You put it in your pocket and make your way out of the Hall of Knowledge.")
	thisArea = areaMap["Hall of Knowledge"]
	del thisArea.miniGame
	thisArea.inside_desc =  "You have already found what you were looking for here."
	inBuilding = False
	areaMap["Red Castle"].miniGame = prologMiniGame
	print ""
	print format("You have accomplished this task, but your worth has not yet been proven. Seek the Wise Master in his quarters in the Red Castle. There you will be tested. Your reward, should you pass, will be the Scroll of Prolog, a most arcane and powerful language.")

def prologMiniGame():
	global areaMap
	global inBuilding
	print format('''You enter the Red Castle and make your way up the stairs. The Wise Master is waiting for you in his office. You tell him that you seek the Scroll of Prolog. "I see," he says. "I will give the scroll to you, but first you will have to earn it. If you can answer enough of my questions correctly, I will bestow the scroll upon you."''')
	print ""
	questions = {
'''In almost all logic languages, axioms are written in a standard form known as a Horn clause.''':True,
'''A Horn clause consists of a head and a body.''':False,
'''A Prolog compiler runs in the context of a database of clauses.''':False,
'''An atom can look like an identifier beginning with an uppercase letter.''':False,
'''A variable looks like an identifier beginning with an uppercase letter.''':True,
'''The scope of every variable is limited to the clause in which it appears.''':True,
'''There are declarations in Prolog.''':False,
'''The clauses in a Prolog database can be classified as facts or rules, each of which ends with a period.''':True,
'''Backward chaining is starting with existing clauses and working to derive the goal.''':False,
'''Backward chaining is starting with the goal and working backwards, attempting to "unresolve" it into a set of preexisting clauses.''':True,
'''The process of returning to previous goals is known as backtracking.''':True,
'''There is never a guaranteed winning strategy in the game of Tic-Tac-Toe''':True
	}
	numAsked = 0
	numCorrect = 0
	numWrong=  0
	numQuestions = len(questions)
	while numAsked < 5 and len(questions) != 0:
		#Continue to ask questions that haven't been asked
		question = random.choice(questions.keys())
		print format(question)
		print ""
		guess = raw_input("What is your answer? ").lower()
		if guess != "true" and guess != "false":
			print format("Please state your answer in a true/false format, thanks. <3")
			print ""
			continue
		if guess == "true":
			guess = True
		else:
			guess = False
		if guess == questions[question]:
			numCorrect += 1
			print format('''"Correct!", the Wise Master exclaims.''')
		else:
			numWrong += 1
			print format("The Wise Master shakes his head at you.")
		numAsked += 1
		#Remove question from the dictionary
		del questions[question]
	if numCorrect  < numWrong + 2:
		print format("This is getting awkward...Lets uhhh, skip this...")
		print format("The Wise Master, DEPRESSED by your LACK of knowledge, hands you the Scroll of Prolog. You exit the Red Castle and look to the west.")
	else:
		print format("The Wise Master, impressed with your knowledge, hands you the Scroll of Prolog. You exit the Red Castle and look to the west.")
	thisArea = areaMap["Red Castle"]
	del thisArea.miniGame
	thisArea.inside_desc =  "You have already found what you were looking for here."
	inBuilding = False
	areaMap["Twin Castle"].miniGame = endGame
	print format("Now you are truly ready to face the final challenge. Make your way to the Twin Castle to complete your quest.")

def endGame():
	print format("You enter the castle and approach the room where you face the final assessment. You sit down and are handed a small stack of papers. The contents of the Scroll of Prolog are fresh in your mind, and the Opal of Wisdom glows warm in your pocket. You ready your writing utensils. You work your way through the stack at an impressive rate, confidently putting down answers as quickly as you can write. Truly, you are the OPaL Master.....")
	print "\n\n\n"
	print str.center('''THE END''', 80)
	raw_input("")
	sys.exit(0)
	

def displayAreaDescription():
	global area
	global inBuilding
	print ""
	print area.name
	if inBuilding and hasattr(area, "miniGame"):
		area.miniGame()
	#If in a building, print inside description and command to leave
	elif inBuilding:
		#print "|*| " + "\n|*| ".join(textwrap.wrap(area.inside_desc))
		print format(area.inside_desc)
		print ["exit"]
	#If outside, display the long description and any area exits
	else:
		print format(area.long_desc)
		exits = []
		if area.inside_desc != None:
			exits.append("enter")
		for exit in area.exits:
			if (area.exits[exit] != None):
				exits.append(exit)
		print exits

def parseCommand():
	global area
	global inBuilding
	global hint
	#Take the next command to parse
	command = raw_input("What do you do? ")
	#Look at appropriate description
	if command == "look":
		displayAreaDescription()
	#Look to another area
	elif command[:4] == "look" and command[5:] in area.exits:
                if area.exits[command[5:]] != None:
			#Get the name of the next area
			nextArea = area.exits[command[5:]]
			nextArea = areaMap[nextArea]
			print format(nextArea.short_desc)
                else:
                        print "There's nothing in that direction."
	#Display contents of inventory
	elif command == "inv" or command == "inventory":
		displayInventory()
	elif inBuilding and command == "exit":
		inBuilding = False
		displayAreaDescription()
	#Attempt to go in the passed direction
	elif not inBuilding and command in area.exits:
                #Verify there is an exit in that direction
                if area.exits[command] != None:
                        #Get the name of the next area
                        nextArea = area.exits[command]
                        #Set the current area to the reference to the next area
                        area = areaMap[nextArea]
                        displayAreaDescription()
                else:
                        print "There's nothing in that direction."
	#Attempt to enter
	elif command == "enter":
		if area.inside_desc != None:
			#Enter building
			inBuilding = True
			displayAreaDescription()
		else:
			#Attempted to enter where there was no entrance
			print "You attempt to enter nothing.  You succeed?"
	#Attempt to exit
	elif command == "exit":
		if inBuilding:
			#Leave current building
			inBuilding = False
			displayAreaDiscription()
		else:
			#Attempted to exit while not in building
			print "You're already outside."
	else:
		print "I don't understand you."
	
def initAreas():
	global area
	global areaMap
	#Unpickle each area and add them to the dictionary
	subdir = "areas"
	files = os.listdir(subdir)
	for file in files:
		#print "Loading in " + os.path.join(subdir, file)
		nextArea = pickle.load(open(os.path.join(subdir, file)))
		areaMap[nextArea.name] = nextArea
	#Get starting area
	area = areaMap.get("Sku Hill")
	areaMap["Hall of Feasts"].miniGame = feastMiniGame

if __name__ == "__main__":
	#Load in area info
	initAreas()
	#Print initial quest information
	print """   ____  ____  ___    __       ____  __  ___________________
  / __ \/ __ \/   |  / /      / __ \/ / / / ____/ ___/_  __/
 / / / / /_/ / /| | / /      / / / / / / / __/  \__ \ / /   
/ /_/ / ____/ ___ |/ /___   / /_/ / /_/ / /___ ___/ // /    
\____/_/   /_/  |_/_____/   \___\_\____/_____//____//_/     
                                                            """
	print format("""Good morning, Apprentice. This is a day of great importance to you. You must summon all of your strength and wisdom, for today you face a great  challenge. You will prove that you are ready to end your apprenticeship and move on to become a Master. To be victorious, you must be strong of body and mind, and use all of the resources at your disposal. """)
	#Display initial area information
	print ""
	displayAreaDescription()
	#While the game is still going
	while True:
		parseCommand()
