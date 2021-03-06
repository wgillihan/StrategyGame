## Team 4 Strategy Game Simple ###
#      William Gillihan          #
#      Christopher Dixon         #
#      Wendy Gray                #
#      Brian Begun               #
#                                #
#      ver 12.18.15              #
#      11_26_2015                #
##################################

#StrategyGame-simple.py
#Main File
#Theme: Star Wars
#
#Object of the game:
#Travel from planet to planet
#Look for the secret plans to the Death Star

# #Put all imports here please
import random

# Star Wars game function
def starWars():
  plansRoom = random.randint(2, 8)  
  gameState = [false, plansRoom]
  printNow("\n\n\n\n\n--------------- STAR WARS ---------------")
  printNow("---------- The Python Adventures ----------")
  help()
  naboo(gameState)

# exit function
def exit():
  printNow("Loser, The Force was not with you!!!")
  return

  # help function
def help():
  printNow("\nA long time ago in a Galaxy far, far away...\n")
  printNow("It is a time of great unrest as the evil Galactic Empire")
  printNow("continues to conquer, ensalve and ravage the free planets of")
  printNow("the galaxy. However, small bands of rebels have banded together") 
  printNow("to fight the tyranny of the Empire and seek to restore the freedom and") 
  printNow("justice known under the Old Republic. Unbeknownst to all, on the planet")
  printNow("Naboo, a lone rebel seeks to obtain and deliver plans of a new, terrible") 
  printNow("weapon created to crush the last vestiges of hope in the galaxy...")
  printNow("Welcome to the Star Wars Galaxy.  You will be able to explore eight worlds in this galaxy.")  
  printNow("On each world, you may jump to other select worlds by typing in one of the choices given.")
  printNow("You need to pick up the plans to the Death Star to stop the Empire.\n")
  printNow("Type \"help\" at any time to redisplay this introduction.")
  printNow("Type \"exit\" to quit the game at any time.\n")

#############################################
# room one (Naboo) function #################
#############################################
def naboo(gameState):
  check = true
  ################### Introduction ####################
  rmDesc = "------------ Naboo Spaceport -----------\n"
  rmDesc += "You have arrived at the Naboo Spaceport.\n"
  rmDesc += "Naboo is a small pastoral world located\n"
  rmDesc += "near the border of the Outer Rim Territories.\n"
  rmDesc += "It is inhabited by two societies - an indigenous\n"
  rmDesc += "species of intelligent amphibians called the Gungans, and\n"
  rmDesc += "a group of peaceful humans who are referred to as the Naboo.\n" 
  rmDesc += "Destination choices are: \n Coruscant, Tatooine, Alderaan, or EXIT to quit.\n"
  printNow (rmDesc)
  ############## this scenario is unlikely since Naboo is the entrance/exit planet (added for possible future change) #############
  if(gameState[0]== false and gameState[1] == 1):# found plan room
    fndPlns = "\nHowever, before you take off, Valenthyne Farfalla\n"
    fndPlns += "catches up to tell you that the Bothans have succeeded in\n"
    fndPlns += "bribing a high-ranking Imperial officer into allowing them\n"
    fndPlns += "to infiltrate a slicer droid into the Coruscant computer network\n"
    fndPlns += "and have located and copied the plans of the Death Star layout.\n"
    fndPlns += "He has just arrived at Naboo to give you the plans personally.\n"
    fndPlns += "He asks you to take them to use in your mission to rescue Princess Leia.\n\n"
    printNow(fndPlns)
    pPln = "Type \"Pickup Plans\" to pick up the plans from the Jedi Master\n"
    pPln += "Type \"HELP\" for game info.\n"
    pPln += "or just Type \"EXIT\" to quit.\n"
    picPln = requestString(pPln)
    picPln = picPln.lower()
    if picPln == "help": # for game info
      help()
      picPln = requestString(pPln)
      picPln = picPln.lower()      
    if picPln == "pickup plans": # pickup plans
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
    elif picPln == "exit": # to exit
      exit()
      check = false
    else:
      printNow("\nYou have failed to pickup the plans.\nReturn later and try again.\n")
###################################################### Destination Choice Loop #################################################	  
  # destination choice loop
  while check == true:
    dstChc = "What is your destination choice?\n"
    dstChc += "Type \"Coruscant\" to jump to Coruscant\n"
    dstChc += "Type \"Tatooine\" to jump to Tatooine\n"
    dstChc += "Type \"Alderaan\" to jump to Alderaan\n"
    dstChc += "Type \"Help\" for game info.\n"
    dstChc += "or just Type \"EXIT\" to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "coruscant": # for Coruscant
      check = false
      coruscant(gameState)
    elif choice == "tatooine": # for Tatooine
      check = false
      tatooine(gameState)
    elif choice == "alderaan": # for Alderaan
      check = false
      alderaan(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    else:
      printNow("You cannot get to "+ chc +" from here,\ntry Coruscant, Tatooine, Alderaan, or type EXIT to quit.")
      check = true

#################################################
# room two (Coruscant) function #################
#################################################
def coruscant(gameState):
  check = true
  ################### Introduction ####################
  rmDesc = "------------ Coruscant Spaceport -----------\n"
  rmDesc += "You have arrived at the Coruscant Spaceport.\n"
  rmDesc += "Coruscant is the vibrant heart and capital of the galaxy.\n"
  rmDesc += "Coruscant was originally called Notron, also known\n"
  rmDesc += "as Imperial Center or the Queen of the Core.\n"
  rmDesc += "It is a planet located in the Galactic Core.\n"
  rmDesc += "It is generally agreed that Coruscant is\n"
  rmDesc += "the most politically important world in the galaxy.\n" 
  rmDesc += "Destination choices are: \nNaboo, Alderaan, Hoth, Dagobah, or type EXIT to quit.\n"
  printNow(rmDesc)
################################################# found plan room #################################################
  if(gameState[0]== false and gameState[1] == 2):# found plan room
    fndPlns = "\nHowever, before you take off, Valenthyne Farfalla\n"
    fndPlns += "catches up to tell you that the Bothans have succeeded in\n"
    fndPlns += "bribing a high-ranking Imperial officer into allowing them\n"
    fndPlns += "to infiltrate a slicer droid into the Coruscant computer network\n"
    fndPlns += "and have located and copied the plans of the Death Star layout.\n"
    fndPlns += "He asks you to take them to use in your mission to rescue Princess Leia.\n\n"
    printNow(fndPlns)
    pPln = "Type \"Pickup Plans\" to pick up the plans from the Jedi Master\n"
    pPln += "Type \"HELP\" for game info.\n"
    pPln += "or just Type \"EXIT\" to quit.\n"
    picPln = requestString(pPln)
    picPln = picPln.lower()
    if picPln == "help": # for Help
      help()
      picPln = requestString(pPln)
      picPln = picPln.lower()      
    if picPln == "pickup plans":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
    elif picPln == "exit":
      exit()
      check = false
    else:
      printNow("\nYou have failed to pickup the plans.\nReturn later and try again.\n")
###################################################### Destination Choice Loop #################################################
  # destination choice loop
  while check == true:
    dstChc = "What is your destination choice?\n"
    dstChc += "Type \"Naboo\" to jump to Naboo\n"
    dstChc += "Type \"Alderaan\" to jump to Alderaan\n"
    dstChc += "Type \"Hoth\" to jump to Hoth\n"
    dstChc += "Type \"Dagobah\" to jump to Dagobah\n"
    dstChc += "Type \"Help\" for game info.\n"
    dstChc += "or just Type \"EXIT\" to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "naboo": # for Naboo
      check = false
      naboo(gameState)
    elif choice == "alderaan": # for Alderaan
      check = false
      alderaan(gameState)
    elif choice == "hoth": # for Hoth
      check = false
      hoth(gameState)
    elif choice == "dagobah": # for Dagobah
      check = false
      dagobah(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    else:
      printNow("You cannot get to "+ chc +" from here,\ntry Naboo, Alderaan, Hoth, Dagobah, or type EXIT to quit..")
      check = true
#################################################
# room 4 (Alderaan) function
#################################################
def alderaan(gameState):
  check = true
  choiceDescrip = ""
  roomDescrip = "\n--------------- Alderaan Spaceport ---------------\n"
  roomDescrip += "You are at the Spaceport on the lush, \n"
  roomDescrip += "mountainous planet of Alderaan, one of the hubs of the \n"
  roomDescrip += "Rebel Alliance.  You spend some time talking to some rebels\n"
  roomDescrip += "about the best ways to avoid the Empire. Your destination options\n"
  roomDescrip += "are Naboo, Coruscant, Cloud City, and Endor.\n"
  
  cDescrip = "What do you want to do?\n"
  cDescrip += "Type \"Naboo\" to jump to Naboo\n"
  cDescrip += "Type \"Coruscant\" to jump to Coruscant\n"
  cDescrip += "Type \"Cloud City\" to jump to Cloud City\n"
  cDescrip += "Type \"Endor\" to jump to Endor\n"
  
  #if this planet has the plans and you don't already have them, notify
  if gameState[0] == false and gameState[1] == 4:
    roomDescrip += "\nHowever, before you take off, Prince Bail Organa\n"
    roomDescrip += "catches up with you.  He reveals a small disk drive\n"
    roomDescrip += "and tells you that it contains the plans of the \n"
    roomDescrip += "layout of the Death Star.  He begs you to take them\n"
    roomDescrip += "and defeat the Empire.\n"
 
    
    choiceDescrip = "Type \"Pickup Plans\" to take the Plans\n"
  

  choiceDescrip = cDescrip + choiceDescrip + "Type \"Exit\" to exit the game\n"
  choiceDescrip += "Type \"Help\" to display game info\n"
  cDescrip += "Type \"Exit\" to exit the game\n"
  cDescrip += "Type \"Help\" to display game info\n"
  
  printNow(roomDescrip)
  choice = requestString(choiceDescrip)
  
  while check == true:
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad!\n")
      return
      check = false
    else:
      choice = choice.lower()
    if choice == "naboo":
      naboo(gameState)
      check = false
    elif choice == "coruscant":
      coruscant(gameState)
      check = false
    elif choice == "cloud city":
      cloudCity(gameState)
      check = false
    elif choice == "endor":
      endor(gameState)
      check = false
    elif choice == "pickup plans" and gameState[0] == false and gameState[1] == 4: #pickup plans
      gameState[0] = true
      printNow("\nCongratulations!  You've accomplished your mission!\n")
      choice = requestString(cDescrip)
    elif choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad!\n")
      return
      check = false
    elif choice == "help":
      help()
      choice = requestString(choiceDescrip)
    else:
      printNow("\nThe nav computer could not interpret your choice. Please try again.\n")
      choice = requestString(choiceDescrip)
      
#################################################
# room 8 (Endor) function
#################################################
def endor(gameState):
  check = true
  choiceDescrip = ""
  roomDescrip = "\n--------------- Endor Spaceport ---------------\n"
  roomDescrip += "You have arrived at the Spaceport on the forest moon\n"
  roomDescrip += "of Endor. After the Ewoks have refueled the Millenium\n"
  roomDescrip += "Falcon, you're ready to continue your journey.\n"
  roomDescrip += "They tell you that the only planets within range\n"
  roomDescrip += "are Alderaan and Hoth.\n"
  
  cDescrip = "What do you want to do?\n"
  cDescrip += "Type \"Alderaan\" to jump to Alderaan\n"
  cDescrip += "Type \"Hoth\" to jump to Hoth\n"
  
  #if this planet has the plans and you don't already have them, notify
  if gameState[0] == false and gameState[1] == 8:
    roomDescrip += "\nMore importantly, you notice a blue astromech droid\n"
    roomDescrip += "rolling toward you and beeping.  The gold protocol droid\n"
    roomDescrip += "next to him calls for you to wait.  He introduces himself\n"
    roomDescrip += "as C-3PO and informs you that his companion, R2-D2 has\n"
    roomDescrip += "the secret plans for the Death Star.  He offers them to\n"
    roomDescrip += "you to destroy the Empire.\n"
    
    choiceDescrip = "Type \"Pickup Plans\" to take the plans from the droids\n"
  
  choiceDescrip = cDescrip + choiceDescrip + "Type \"Exit\" to exit the game\n"
  choiceDescrip += "Type \"Help\" to display game info\n"
  cDescrip += "Type \"Exit\" to exit the game\n"
  cDescrip += "Type \"Help\" to display game info\n"
  
  printNow(roomDescrip)
  choice = requestString(choiceDescrip)
  
  while check == true:
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad!\n")
      return
      check = false
    else:
      choice = choice.lower()
    if choice == "alderaan":
      alderaan(gameState)
      check = false
    elif choice == "hoth":
      hoth(gameState)
      check = false
    elif choice == "pickup plans" and gameState[0] == false and gameState[1] == 8: #pickup plans
      gameState[0] = true
      printNow("\nCongratulations!  You've accomplished your mission!\n")
      choice = requestString(cDescrip)
    elif choice == "help":
      help()
      choice = requestString(choiceDescrip)
    elif choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad!\n")
      return
      check = false
    else:
      printNow("\nThe nav computer could not interpret your choice. Please try again.\n")
      choice = requestString(choiceDescrip)


#############################################
# room three (Tatooine) function ############
#############################################
#Function to grab input choices and display game play options
#In requestString dialog box
#return user entered input to be used in other functions
#only allow certain user options depending on what part of the planet gameplay
#user is in.
def userChoice(roomState, gameState, currentRoom, dialogDisplay):
  choiceStat = false
  while choiceStat == false:
    userInput = requestString(dialogDisplay)
    if userInput == None:
      printNow("Okay, I guess you want to leave the game...Bye!")
      choiceStat = true
      exit()
    else:
      userInput = userInput.lower()
      if userInput == 'help':
        return('help')
        choiceStat = false
      elif userInput == 'exit':
        printNow("Time to leave.")
        choiceStat = true
        exit()
      elif userInput == 'dagobah' and roomState == 'tatooine':
        printNow("you're off to Dagobah...wooosh!")
        choiceStat = true
        return('dagobah')
      elif userInput == 'cloud city' and roomState == 'tatooine':
        printNow("you're off to Cloud City...woosh!")
        choiceStat = true
        return('cloud city')
      elif userInput == 'naboo' and roomState == 'tatooine':
        printNow("you're off to Naboo...woosh!")
        choiceStat = true
        return('naboo')
      elif userInput == 'cantina' and roomState == 'tatooine':
        printNow("I'm thirsty, let's go check out the cantina.")
        choiceStat = true
        return('cantina')
      elif userInput == 'chat' and roomState == 'cantina':
        choiceStat = true 
        return('chat')  
      elif userInput == 'leave' and roomState == 'cantina':
        printNow("\nYou've left the cantina.")
        choiceStat = true
        return('leave')
      else:
        printNow("The nav computer could not interpret your choice. Please try again.")
        choiceStat = false

#Establish where the user is on current planet and return appropriate dialog        
def whereAmI(gameState, roomState, currentRoom):
  options = ""
  uDialogOptions = ""
  roomDescrip = ""
  action = ""
  uDialogAction = ""
  
  options =  "\n Type \"help\" to re-display this introduction."
  options += "\nType \"exit\" or cancel the dialog box to quit at any time."
  uDialogOptions = options
  
  if roomState == 'tatooine':
    roomDescrip =  "\nYou have arrived at Mos Isley Spaceport on Tatooine.  "  
    roomDescrip += "There are space transports currently available to take you to Dagobah, "
    roomDescrip += "Cloud City or Naboo and a cantina nearby."
    if gameState[0] == true:
      action =  "\nYou have the secret plans, but you might want to check out the Cantina, "
      action += "and see if anyone can help you find the Death Star."
    elif gameState[0] == false:
      action =  "\nSince your mission is to find the secret plans for the Death star, "
      action += "you might want to ask around a little bit and see if anyone can help you."
    action += "\nEnter \"Dagobah\", \"Cloud City\" or \"Naboo\" to move on to another planet or \ntype "
    uDialogAction = "\nEnter \"Dagobah\", \"Cloud City\" or \"Naboo\" to move on to another planet or \ntype "
    action += "\"Cantina\" to go into the bar nearby and talk to some locals"
    uDialogAction += "\"Cantina\" to go into the bar nearby and talk to some locals" 
  elif roomState == 'cantina':
    roomDescrip =  "\nYou've entered the local cantina.  "
    roomDescrip += "Strangely enough, the bar is virtually empty.  "
    roomDescrip += "\nAt the moment, only the barkeep is around cleaning drink glasses "
    roomDescrip += "with a scornful look on his face."
    if gameState[0] == true:
      action = "\nYou might want to ask the barkeep if he knows how to get to the Death Star."
    elif gameState[0] == false:
      action = "\nHe's staring right at you.  Now is your chance to ask him for some help."
    action += "\nEnter \"chat\" to ask the barkeep a question or type \"leave\" to exit the cantina."
    uDialogAction = "\nEnter \"chat\" to ask the barkeep a question or type \"leave\" to exit the cantina."   
  elif roomState == 'chat':
    roomDescrip = "\nYou say jokingly: \"Hey barkeep, you happen see any secret "
    roomDescrip += "Death Star plans around here?\""
    if gameState[0] == true:
      action =  "\nHe replies: \"Moron, you've got them in your hand.\"  "
      action += "You reply with a look of embarrassment on your face: \"Sorry, I mean "
      action += "do you know of a way to get to the Death Star?\""
      action += "\n\"Nope, nothing like that 'round here.  "
      action += "Don\'t ask me stupid questions.  Now leave me alone!\""
    elif gameState[1] == currentRoom and gameState[0] == false:
      action += "\n\"You mean these worthless maps?  "
      action += "Some old guy with a lightsaber traded them for a drink.  "
      action += "I took pity on the old drunk and agreed on the trade.  "
      action += "You can have them if you want.  "
      action += "They're just collecting dust back here.\"  "
      action += "He hands you the plans.  What luck!"
    else:
      action =  "\n\"Nope, nothing like that around here.  "
      action += "You may want to check out one of the nearby systems.  "
      action += "Might have better luck.\"" 
    action += "\nType \"leave\" to exit the bar"
    uDialogAction += "\nType \"leave\" to exit the bar" 
  return(options, roomDescrip, action, gameState, uDialogOptions, uDialogAction)
  
#Function to display chosen dialog 
def dialog(roomState, gameState, currentRoom):

  printNow("\n--------------- Tatooine ---------------")
  
  allDialog =  whereAmI(gameState, roomState, currentRoom)
  
  options = allDialog[0]
  roomDescrip = allDialog[1]
  action = allDialog[2]
  textDisplay =  roomDescrip + action + options
  
  uDialogOptions = allDialog[4]
  uDialogAction = allDialog[5]
  dialogDisplay = uDialogAction + uDialogOptions
  
  printNow(textDisplay)
  return(dialogDisplay)  

#main planet function for tatooine()
#set's current room number as a variable
#set's roomState variable to tatooine to be used later
def tatooine(gameState):

  currentRoom = 3
  roomState = 'tatooine'
 
 #execute dialog depending on user input
 #if another planet is choosen, exit while loop and off to other external function    
  uiDialog = dialog(roomState, gameState, currentRoom)
  userResult = userChoice(roomState, gameState, currentRoom, uiDialog)
  while userResult != 'exit' and userResult != None:
    if userResult == 'help':
      help()
      userResult = userChoice(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'cantina':
      roomState = 'cantina'
      uiDialog = dialog(roomState, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'chat':
      uiDialog = dialog(userResult, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'leave':
      roomState = 'tatooine'
      uiDialog = dialog(roomState, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'chat' and gameState[1] == currentRoom:
      gameState[0] = true
    if userResult == 'dagobah':
      dagobah(gameState)
      userResult = 'exit'
    elif userResult == 'cloud city':
      cloudCity(gameState)
      userResult = 'exit'
    elif userResult == 'naboo':
      naboo(gameState)
      userResult = 'exit'
 
#############################################
# room seven (Cloud City) function ##########
############################################# 
#Function to grab input choices and display game play options
#In requestString dialog box
#return user entered input to be used in other functions
#only allow certain user options depending on what part of the planet gameplay
#user is in.
def userChoice2(roomState, gameState, currentRoom, dialogDisplay):
  choiceStat = false
  while choiceStat == false:
    userInput = requestString(dialogDisplay)
    if userInput == None:
      printNow("Okay, I guess you want to leave the game...Bye!")
      choiceStat = true
      exit()
    else:
      userInput = userInput.lower()
      if userInput == 'help':
        return('help')
        choiceStat = false
      elif userInput == 'exit':
        printNow("Time to leave.")
        choiceStat = true
        exit()
      elif userInput == 'tatooine' and roomState == 'cloudCity':
        printNow("you're off to Tatooine...wooosh!")
        choiceStat = true
        return('tatooine')
      elif userInput == 'alderaan' and roomState == 'cloudCity':
        printNow("you're off to Alderaan...woosh!")
        choiceStat = true
        return('alderaan')
      elif userInput == 'business' and roomState == 'cloudCity':
        printNow("I'm thirsty, let's go check out the business.")
        choiceStat = true
        return('business')
      elif userInput == 'chat' and roomState == 'business':
        choiceStat = true 
        return('chat')  
      elif userInput == 'leave' and roomState == 'business':
        printNow("\nYou've left the business.")
        choiceStat = true
        return('leave')
      else:
        printNow("The nav computer could not interpret your choice. Please try again.")
        choiceStat = false
        
#Establish where the user is on current planet and return appropriate dialog            
def whereAmI2(gameState, roomState, currentRoom):
  options = ""
  uDialogOptions = ""
  roomDescrip = ""
  action = ""
  uDialogAction = ""
  
  options =  "\n Type \"help\" to re-display this introduction."
  options += "\nType \"exit\" or cancel the dialog box to quit at any time."
  uDialogOptions = options
  
  if roomState == 'cloudCity':
    roomDescrip =  "\nYou have arrived at the main space port on Cloud City.  "
    roomDescrip += "There are space transports currently available to take you "
    roomDescrip += "to Tatooine or Alderaan and the business district nearby."
    if gameState[0] == true:
      action =  "\nYou have the secret plans, but you might want to check "
      action += "out the local businesses, and see if anyone can help you "
      action += "find the Death Star."
    elif gameState[0] == false:
      action =  "\nSince your mission is to find the secret plans "
      action += "for the Death star, you might want to ask around "
      action += "a little bit and see if anyone can help you."
    action += "\nEnter \"Tatooine\" or \"Alderaan\" to move on to another planet "
    uDialogAction = "\nEnter \"Tatooine\" or \"Alderaan\" to move on to another planet "
    action += "or type \"Business\" to go into the business center nearby "
    uDialogAction += "or \ntype \"Business\" to go into the business center nearby "
    action += "and talk to some locals."
  elif roomState == 'business':
    roomDescrip =  "\nYou've entered the business district.  "
    roomDescrip += "It's off season, so the marketplace is virtually empty.  "
    roomDescrip += "At the moment, only a local merchant is around selling her wares."
    if gameState[0] == true:
      action =  "\nYou might want to ask the merchant if she knows "
      action += "how to get to the Death Star."
    elif gameState[0] == false:
      action =  "\nShe's trying to ignore you, but since no one else "
      action += "seems to be around, why don\'t you ask her for some help."
    action += "\nEnter \"chat\" to talk to the merchant or type \"leave\" " 
    action += "to go back to the ship."
    uDialogAction = "\nEnter \"chat\" to talk to the merchant or type \"leave\" "
    uDialogAction += "to go back to the ship."    
  elif roomState == 'chat':
    roomDescrip =  "\nYou say jokingly: \"Hi there good lookin\', you "
    roomDescrip += "happen see any secret Death Star plans around here?\"\n"
    if gameState[0] == true:
      action =  "\nShe replies: \"Moron, you've got them in your hand.\"  "
      action += "You reply with a look of embarrassment on your face: \"Sorry, "
      action += "I mean do you know of a way to get to the Death Star?\"\n"
      action += "\n\"Nope, nothing like that 'round here.  Don\'t ask me "
      action += "stupid questions.  Now leave me alone!\""
    elif gameState[1] == currentRoom and gameState[0] == false:
      action += "\n\"You mean these worthless maps?  Some old guy with a "
      action += "lightsaber traded them for a new pair of shoes.  I took pity "
      action += "on the old drunk and agreed on the trade.  I didn't know what "
      action += "to do with them, so I sewed them into this nice blanket.  "
      action += "You can have them if you want.  It\'s not selling anyway.\"  She "
      action += "hands you the plans.  What luck!"
    else:
      action =  "\n\"Nope, nothing like that around here.  You may want to check "
      action += "out one of the nearby systems.  Might have better luck.\""
    action += "\nType \"leave\" to exit the business district" 
    uDialogAction += "\nType \"leave\" to exit the business district" 
  return(options, roomDescrip, action, gameState, uDialogOptions, uDialogAction)
  
#Function to display chosen dialog   
def dialog2(roomState, gameState, currentRoom):

  printNow("\n--------------- Cloud City ---------------")
    
  allDialog =  whereAmI2(gameState, roomState, currentRoom)
  
  options = allDialog[0]
  roomDescrip = allDialog[1]
  action = allDialog[2]
  textDisplay =  roomDescrip + action + options
  
  uDialogOptions = allDialog[4]
  uDialogAction = allDialog[5]
  dialogDisplay = uDialogAction + uDialogOptions
  
  printNow(textDisplay)
  return(dialogDisplay)  
 

#main planet function for cloudCity()
#set's current room number as a variable
#set's roomState variable to cloud city to be used later
def cloudCity(gameState):

  currentRoom = 7
  roomState = 'cloudCity'
  
 
 #execute dialog depending on user input
 #if another planet is choosen, exit while loop and off to other external function   
  uiDialog = dialog2(roomState, gameState, currentRoom)
  userResult = userChoice2(roomState, gameState, currentRoom, uiDialog)
  while userResult != 'exit' and userResult != None:
    if userResult == 'help':
      help()
      userResult = userChoice2(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'business':
      roomState = 'business'
      uiDialog = dialog2(roomState, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'chat':
      uiDialog = dialog2(userResult, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'leave':
      roomState = 'cloudCity'
      uiDialog = dialog2(roomState, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom, uiDialog)
    if userResult == 'chat' and gameState[1] == currentRoom:
      gameState[0] = true  
    if userResult == 'tatooine':
    	tatooine(gameState)
    	userResult = 'exit'
    elif userResult == 'alderaan':
    	alderaan(gameState)
    	userResult = 'exit'
    elif userResult == 'death star':
    	deathStar(gameState)
    	userResult = 'exit'
        

##########HOTH FUNCTION (ROOM 5)#########################

def hoth(gameState): #room 5
  check = true
  roomDesc = "\n--------------- Hoth Spaceport ---------------\n"
  roomDesc += "Hoth is the sixth planet in the hoth system\n"
  roomDesc += "It is a frozen world covered in snow and ice.\n"
  roomDesc += "The wampa and the tauntaun are both native to hoth.\n"
  roomDesc += "A newly deceased tauntaun can be cut open to \n"
  roomDesc += "to make a great temporary refuge from the cold.\n"
  
    
  while check == true:
    option = "What is your choice?\n"
    # if the player doesn't have plans, and this is the planet with the plans, tell the player
    if (gameState[0] == false and # does not have plans 
    gameState[1] == int(5)): #this planet has the plans
       option += "The plans are here!\n"
       option += "Type \"pickup plans\" to get the plans.\n"
       roomDesc += "The plans are here!\n"
       roomDesc += "Type \"pickup plans\" to get the plans.\n"   
  
    option += "Type \"Coruscant\" to jump to Coruscant.\n"
    option += "Type \"Endor\" to jump to Endor.\n"
    option += "Type \"Help\" to re-display this introduction.\n"
    option += "Type \"Exit\" to quit."
    
    printNow(roomDesc)
    
    choice = requestString(option)
    
    if choice == None:
      printNow("Bye Jar Jar")
      return
      check = false
    
    choice = choice.lower()
    
    if choice == "coruscant":
      coruscant(gameState)
      check = false
    elif choice == "endor":
      endor(gameState)
      check = false
    elif (choice == "pickup plans" and
    gameState[0] == false and #player doesn't already have plans
    gameState[1] == int(5)):#this is the plans room
      printNow("You found the plans!")
      gameState[0] = true #hasPlans
      check = false
      hoth(gameState)
    elif choice == "exit":
      printNow("Bye Jar Jar")
      return
      check = false
    elif choice == "help":
      help()   
    else:
      printNow("I don't recognize that statement.")
      
##########DAGOBAH FUNCTION (ROOM 6)#########################

def dagobah(gameState): #room 6
  check = true
  roomDesc = "\n--------------- Dagobah Spaceport ---------------\n"
  roomDesc += "Dagobah is a world of murky swamps,\n"
  roomDesc += "steaming bayous, and petrified forests.\n"
  roomDesc += "The great Jedi Yoda lives near a cave\n"
  roomDesc += "infused with the dark side of the Force\n"
  roomDesc += "which keeps Emperor Palpatine from detecting him.\n"
  

  
  while check == true:
    option = "What is your choice?\n"
    # if the player doesn't have plans, and this is the planet with the plans, tell the player
    if (gameState[0] == false and # does not have plans 
    gameState[1] == int(6)): #this planet has the plans
       option += "The plans are here!\n"
       option += "Type \"pickup plans\" to get the plans.\n"
       roomDesc += "The plans are here!\n"
       roomDesc += "Type \"pickup plans\" to get the plans.\n" 
  
    option += "Type \"Coruscant\" to jump to Coruscant.\n"
    option += "Type \"Tatooine\" to jump to Tatooine.\n"
    option += "Type \"Help\" to re-display this introduction.\n"
    option += "Type \"Exit\" to quit."
    
    printNow(roomDesc)
    
    choice = requestString(option)
    
    if choice == None:
      printNow("Bye Jar Jar")
      return
      check = false
    
    choice = choice.lower()
    
    if choice == "coruscant":
      coruscant(gameState)
      check = false
    elif choice == "tatooine":
      tatooine(gameState)
      check = false
    elif (choice == "pickup plans" and
    gameState[0] == false and #player doesn't already have plans
    gameState[1] == int(6)):#this is the plans room
      printNow("You found the plans!")
      gameState[0] = true #hasPlans
      check = false
      dagobah(gameState)
    elif choice == "exit":
      printNow("Bye Jar Jar")
      return
      check = false
    elif choice == "help":
      help()   
    else:
      printNow("I don't recognize that statement.")
