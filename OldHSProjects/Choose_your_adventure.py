# This is an adventure game with multiple branching paths #

print('WARNING: DO NOT PRESS ENTER UNTIL A NUMBER IS TYPED. DO NOT INPUT ANY NUMBERS THAT ARE NOT PROMPTED, AS THE GAME WILL CRASH')

######## Imported Functions ########
import time
from random import randint
####################################

######## Variables Definitions ########
path = int(0) # Gives the user the path that they input #
hunt = False # Triggers after first choice in hunting path, transitions to the rest of the path #
deer = int(0) # Another variable similar to the hunt variable #
hit = int(0) # Tracks if the user hits the deer #
store = False # Triggers after first choice in grocery store path, transitions to the rest of the path #
go_home = False # Triggers at the end of each path to transition to the ending #
hungry = int(0) # Variable that tracks if the user ate food in the store path #
arrows = int(3) # Set to 3 and decreases depending on what you decide to do in the hunting path #
success = int(0) # Variable that tracks if the player's hunt was successful or not #
visited = int(0) # Variable that tracks if the player has visited a department1 in the store path #
bag = int(0) # Variable that tracks if the player collected the bag in the store path #
knife = int(0) # Variable that tracks if the layer collected the knife in the store path #
department1 = int(0) # Variable that sets the first department1 that the player goes to #
department2 = int(0) # Variable that sets the second department1 the player wants to do to #
clothes = int(0) # Variables that tracks if the player went to the clothing store #
floral = int(0) # Variable that tracks if the player went to the floral department1 #
outcome = int(0) # Determines what will be said to the player at the end of the game #
plan1 = int(0)
plan2 = int(0)
plan3 = int(0)
plan4 = int(0)
# The plan variables track which way the player can end the game #
retry = int(0) # Variable that restarts the game #
start = int(input('Type 1 to start the game ')) # Variable that starts the game #
#######################################

######## Beginning Loop ########

# This loop starts the game once the user presses 1 #
# It also contains the code for choosing a path #

if start == int(1):
  print('It is a very distant future')
  time.sleep(2)
  print('The world has been thrown into chaos and society has fallen')
  time.sleep(2)
  print('You are a lone wanderer, trying to survive in this cruel world')
  time.sleep(3)
  print('You are extremely hungry, but you ran out of food the night before')
  time.sleep(3)
  print('You figure that it is time to get up and find something to eat')
  time.sleep(3)
  print('You have a handmade bow with 3 arrows and a machete')
  time.sleep(3)
  print('Behind your shelter is a vast forest')
  time.sleep(3)
  print('There is an abandoned grocery store a few miles away, but most of the food is inedible')
  time.sleep(3)
  print('Where will you get your food?')
  time.sleep(2)
  print('Go hunting in the forest (1)')
  print('Scavenge at the abandoned grocery store (2)')
  path = int(input('Type the number of the path that you want to take '))
################################

######## First Choices Loop ########

# This loop contains all of the first choices for each path #

if path == int(1):
  print('You exit your shelter, bow in hand, to go hunting')
  time.sleep(3)
  print('It took a long time, but you finally found a deer, grazing in an open part of the forest')
  time.sleep(3)
  print('It would be risky, but you could take a shot at it')
  time.sleep(3)
  print('One shot might not kill it though, so you may have to use multiple arrows')
  time.sleep(3)
  print('What will you do?')
  time.sleep(2)
  print('Shoot it in the leg, then go in for the kill (1)')
  print('Go for the neck (2)')
  deer = int(input('Type the number of what you want to do '))
  hunt = True
elif path == int(2):
  print('Even though it has been abandoned and likely picked clean, you hold out hope for the grocery store')
  time.sleep(4)
  print('After a long walk, you finally arrive')
  time.sleep(3)
  print('All of the windows are broken and thick green foliage has started growing on the walls')
  time.sleep(3)
  print('Thankfully, there seems to be nobody around, so you casually walk into the grocery store')
  time.sleep(3)
  print('You look around and see that there are three places to go: the aisles to your left, the clothing shop to your right, and a floral department next to the front door')
  time.sleep(6)
  print('Where will you go?')
  time.sleep(2)
  print('The aisles (1)')
  print('The clothing store (2)')
  print('The floral department1 (3)')
  department1 = int(input('Type the number of the place you want to go to '))
  store = True
####################################

######## Hunting Loop ########

# This loop contains the code for the hunting path and stores the values of the variables affected by it towards the end. This will affect the final part of the game. #

if hunt == True:
  if deer == int(1):
    arrows = int(1)
    print('You hit the deer in the leg!')
    time.sleep(2)
    print('It starts to limp away, so you take another shot and it collapses')
    time.sleep(3)
    print('You approach the deer and finally kill it with your machete')
    time.sleep(3)
    print('After butchering it for a while, you head home with some fresh meat and deer pelt')
    time.sleep(4)
    go_home = True
    success = int(1)
  elif deer == int(2):
    arrows = 2
    print('You hold your breath as your heart races at the tought of potentially missing your shot')
    time.sleep(4)
    print('You draw your bow, pull back, and...')
    time.sleep(3)
    print('Fire!')
    hit = randint(1, 2)
    time.sleep(2)
    if hit == int(1):
      print('Yes! You hit the deer in the neck!')
      time.sleep(2)
      print('You see it fall over and have a sigh of relief')
      time.sleep(3)
      print('The shot you hit killed the deer instantly')
      time.sleep(3)
      print('After butchering it for a while, you head home with some fresh meat and deer pelt')
      time.sleep(4)
      go_home = True 
      success = int(1)
    elif hit == int(2):
      print('No! You missed the deer!')
      time.sleep(2)
      print('It runs away into the forest')
      time.sleep(2)
      print('Feeling defeated, you decide to make your way back home to think of a new plan')
      time.sleep(3)
      go_home = True
      success = int(2)
##############################

######## Grocery Store Loop ########

# This loop contains all of the code for the grocery store path and the values of the variables affected by it in the end #

if store == True:
  if department1 == int(2):
    print('Since nobody else is here, you think that you may as well look around a bit')
    time.sleep(3)
    print('You enter the clothing store and find what looks to be the remains of an old camp')
    time.sleep(3)
    print('After searching around for a bit, you find a big reusable bag!')
    clothes = 1
    bag = int(1)
    time.sleep(3)
  elif department1 == int(3):
    print('Since nobody else is here, you think you may as well look around a bit')
    time.sleep(3)
    print('Before you enter the department, you observe from the counter')
    time.sleep(3)
    print('There are many dead plants lying around in what looks to be old flower arrangements')
    time.sleep(3)
    print('Then, you notice a small plaque on the wall. It reads:')
    time.sleep(3)
    print('"Community Votes 2020 Platinum Winner, Best Florists and Flower Shops"')
    time.sleep(3)
    print('Huh. Whoever ran this floral department must have done a really good job')
    time.sleep(3)
    print('When you search the drawers behind the counter, you manage to find an unusually sharp knife!')
    floral = int(1)
    knife = int(1)
    time.sleep(4)
  
  if clothes == int(1):
    print('Where will you go now?')
    time.sleep(3)
    print('The aisles (1)')
    print('The floral department (3)')
    department2 = int(input('Type the number of the place you want to go to '))
  elif floral == int(1):
    print('Where will you go now?')
    time.sleep(3)
    print('The aisles (1)')
    print('The clothing store (2)')
    department2 = int(input('Type the number of the place you want to go to '))

  if department2 == int(2):
    print('You enter the clothing store and find what looks to be the remains of an old camp')
    time.sleep(3)
    print('After searching around for a bit, you find a big reusable bag!')
    bag = int(1)
    visited = int(1)
    time.sleep(3)
  elif department2 == int(3):
    print('Before you enter the department, you observe from the counter')
    time.sleep(3)
    print('There are many dead plants lying around in what looks to be old flower arrangements')
    time.sleep(3)
    print('Then, you notice a small plaque on the wall. It reads:')
    time.sleep(3)
    print('"Community Votes 2020 Platinum Winner, Best Florists and Flower Shops"')
    time.sleep(3)
    print('Huh. Whoever ran this floral department must have done a really good job')
    time.sleep(3)
    print('When you search the drawers behind the counter, you manage to find an unusually sharp knife!')
    knife = int(1)
    visited = int(1)
    time.sleep(4)

  if visited == int(1):
    print('Now that you have searched the other two departments, you decide to search the aisles')
    department1 = int(1)
    time.sleep(4)

  if department1 == int(1):
    print('The first aisle is labelled "Cleaning Supplies", so nothing useful there')
    time.sleep(3)
    print('The next two aisles are also useless, but the aisle after that has some cans left on the shelves!')
    time.sleep(3)
    print('There are 5 cans of fruit, 6 cans of veggies, and 3 cans of tuna')
    time.sleep(3)
    print('Seems like whoever lived here left before they could gather the rest of the food')
    time.sleep(3)
  elif department2 == int(1):
    print('The first aisle is labelled "Cleaning Supplies", so nothing useful there')
    time.sleep(3)
    print('The next two aisles are also useless, but the aisle after that has some cans left on the shelves!')
    time.sleep(3)
    print('There are 5 cans of fruit, 6 cans of veggies, and 3 cans of tuna')
    time.sleep(3)
    print('Seems like whoever lived here left before they could gather the rest of the food')
    time.sleep(3)

  if knife == int(1):
    print('Since you grabbed the knife earlier, you try to open a can of fruit')
    time.sleep(3)
    print('The knife was so sharp that you could stab a hole in the can and peel off the top!')
    time.sleep(4)
    print('You quickly eat the contents of the can')
    time.sleep(2)
    hungry = int(1)
    print('You are no longer starving!')
    time.sleep(3)
  else:
    print('If only you had something to open one of these cans, you are so hungry that you would crack one open right now')
    time.sleep(4)

  if bag == int(1):
    print('Since you got the bag at the old camp, you are able to take all of the cans!')
    time.sleep(3)
    print('This could definetly keep you fed for a few days at least')
    time.sleep(3)
  else:
    print("You don't have any bags with you, so you are only able to take two of each can")
    time.sleep(3)

  print('You head home')

  if bag == int(1):
    print('carrying all of the cans you found')
    time.sleep(4)
  elif knife == int(1):
    print('feeling energized')
    time.sleep(4)
  
  if bag == int(0):
    print('with 6 cans of food')
    time.sleep(4)
  go_home = True
####################################

######## Ending Loops ########

# This section contains the code for the end of the game, which is switched up depending on which path you take #

if go_home == True:
  print('Wow, it really has been a long day')
  time.sleep(3)
 
  if success == int(1):
    print('Trudging through the forest, you feel yourself getting even hungrier as you think about cooking the deer')
    time.sleep(4)
  elif success == int(2):
    print('Trudging through the forest, you dwell on how you will get food now that your hunting attempt has failed') 
    time.sleep(4)

  print('As you near your shelter, you notice people standing guard outside!')
  time.sleep(3)
  print('You quickly dart behind a nearby bush on a hill to observe')
  time.sleep(3)

  if success == int(1):
    print('You quietly lay down your deer meat and pelt in the bush for safe keeping')
    time.sleep(3)
  elif bag == int(1):
    print('You quietly lay down your bag of cans in the bush for safe keeping')
    time.sleep(3)
  elif bag == int(0):
    print('You take all of the cans out of your pockets and lay them in the bush for later')
    time.sleep(3)

  print('You carefully peer through the leaves and see that there are three bandits standing guard outside your shelter')
  time.sleep(4)
  print('It seems these bandits are not very discrete, as you can hear loud footsteps and banging from your shelter')
  time.sleep(4)
  print("You can't make out what they are saying, but you can hear the voices of two people inside")
  time.sleep(3)
  print('You take inventory of what you have at the moment to deal with this situation')
  time.sleep(3)
  print('You have...')
  time.sleep(2)
  
  if arrows == int(2):
    print('two arrows for your bow,')
    time.sleep(2)
  elif arrows == int(1):
    print('one arrow for your bow,')
    time.sleep(2)
  elif knife == int(1):
    print('the knife from the store,')
    time.sleep(2)
  elif hungry == int(1):
    print('energy from the can of fruit, ')
    time.sleep(2)

  print('your machete,')
  time.sleep(2)
  print('and the knowledge of your shelter')
  time.sleep(2)
  print('What will you do?')
  time.sleep(3)

  if arrows == int(2):
    print('Pick off two guards with your bow, then get the last one with your machete (1)')
    outcome = int(1)
  elif arrows == int(1):
    print('Pick off one guard with your bow, then get the last two with your machete (1)')
    outcome = int(2)
  elif hungry == int(1):
    print('Swiftly run in and get them all with your knife (1)')
    outcome = int(3)
  else:
    outcome =int(4)
  
  print('Try with just your machete (2)')
  print('Give up and find another shelter (3)')

  if outcome == int(1):
    plan1 = int(input('Type the number of the way you want to deal with the situation '))
  elif outcome == int(2):
    plan2 = int(input('Type the number of the way you want to deal with the situation '))
  elif outcome == int(3):
    plan3 = int(input('Type the number of the way you want to deal with the situation '))
  elif outcome == int(4):
    plan4 = int(input('Type the number of the way you want to deal with the situation '))

  # Ending 1 #
  if plan1 == int(1):
    print('You wait until all of the guards are split up, then quickly shoot two of them, killing them instantly')
    time.sleep(4)
    print('You then sneak up to the last guard and pick him off with your machete')
    time.sleep(3)
    print('You wait until you think the coast is clear to go inside')
    time.sleep(3)
    print('As you sneak into the shelter, you can hear the two bandits in the other room, as if they are clueing up their raid')
    time.sleep(4)
    print('Quickly, you charge into the room and tackle one of the bandits, slashing them with your machete')
    time.sleep(3)
    print('Before you can get up, the other bandit takes out his knife and lands three quick slashes on your back')
    time.sleep(4)
    print('Though you are in pain, you swing the machete at the bandit and manage to finally kill him')
    time.sleep(3)
    print('It took some effort, but you managed to defend your shelter!')
    time.sleep(3)
    print('(Marksman Ending)')
  # Ending 2 #
  elif plan2 == int(1):
    print('You wait for the guards to separate, then pick off one of them with your bow')
    time.sleep(3)
    print('Then, you sneak behind another guard and take him out with the machete')
    time.sleep(3)
    print('You turn the corner to get the last guard when you both make eye contact')
    time.sleep(4)
    print('You try to quickly dash at him with the machete, but before you land the killing blow he manages to whack you over the head with his club')
    time.sleep(4)
    print('That hit was pretty hard, but you managed to walk out of it alive, but with your head spinning')
    time.sleep(4)
    print('Wearily, you wait until you think the coast is clear to go inside')
    time.sleep(3)
    print('As you sneak into the shelter, you can hear the two bandits in the other room, as if they are clueing up their raid')
    time.sleep(4)
    print('You charge in and attempt to slash one of them with your machete')
    time.sleep(3)
    print('But due to the hit you just took, you miss')
    time.sleep(3)
    print('The bandits quickly take out their weapons and overwhelm you')
    time.sleep(3)
    print('You perish at the hands of the bandits')
    time.sleep(3)
    print('(Concussion Ending)')
  # Ending 3 #
  elif plan3 == int(1):
    print('Since you are energized, you take out your knife and quietly sprint towards one of the guards, taking him out in one fell swoop')
    time.sleep(4)
    print('Then, you do the same with a second guard and finally the third')
    time.sleep(3)
    print('With the guards swiftly taken care of, you sneak into the shelter')
    time.sleep(3)
    print('As you sneak into the shelter, you can hear the two bandits in the other room, as if they are clueing up their raid')
    time.sleep(4)
    print('Quietly, you creep towards the entrance to the other room')
    time.sleep(3)
    print('Then, you lunge at the first bandit and stab him with your knife, killing him instantly')
    time.sleep(3)
    print('With your other hand, you immediately take out your machete and kill the other bandit before he even knew what was happening')
    time.sleep(4)
    print('You protected your shelter masterfully!')
    time.sleep(3)
    print('(Swift Ninja Ending)')
  # Ending 4 #
  elif plan1 == int(2):
    print('When the guards are separated, you sneak up to one and take him out with your machete')
    time.sleep(3)
    print('You try to sneak to the next guard, but you find yourself surrounded!')
    time.sleep(3)
    print('You try to defend yourself, but the guards call out the other two bandits and they all start to take out their weapons')
    time.sleep(4)
    print('Four against one, you perish at the hands of the bandits')
    time.sleep(3)
    print('(Cornered Ending)')
  elif plan2 == int(2):
    print('When the guards are separated, you sneak up to one and take him out with your machete')
    time.sleep(3)
    print('You try to sneak to the next guard, but you find yourself surrounded!')
    time.sleep(3)
    print('You try to defend yourself, but the guards call out the other two bandits and they all start to take out their weapons')
    time.sleep(4)
    print('Four against one, you perish at the hands of the bandits')
    time.sleep(3)
    print('(Cornered Ending)')
  elif plan3 == int(2):
    print('When the guards are separated, you sneak up to one and take him out with your machete')
    time.sleep(3)
    print('You try to sneak to the next guard, but you find yourself surrounded!')
    time.sleep(3)
    print('You try to defend yourself, but the guards call out the other two bandits and they all start to take out their weapons')
    time.sleep(4)
    print('Four against one, you perish at the hands of the bandits')
    time.sleep(3)
    print('(Cornered Ending)')
  elif plan4 == int(2):
    print('When the guards are separated, you sneak up to one and take him out with your machete')
    time.sleep(3)
    print('You try to sneak to the next guard, but you find yourself surrounded!')
    time.sleep(3)
    print('You try to defend yourself, but the guards call out the other two bandits and they all start to take out their weapons')
    time.sleep(4)
    print('Four against one, you perish at the hands of the bandits')
    time.sleep(3)
    print('(Cornered Ending)')
  # Ending 5 #
  elif plan1 == int(3):
    print('Overwhelmed by the situation, you decide to flee and leave your shelter behind')
    time.sleep(3)
    print('(Coward Ending)')
  elif plan2 == int(3):
    print('Overwhelmed by the situation, you decide to flee and leave your shelter behind')
    time.sleep(3)
    print('(Coward Ending)')
  elif plan3 == int(3):
    print('Overwhelmed by the situation, you decide to flee and leave your shelter behind')
    time.sleep(3)
    print('(Coward Ending)')
  elif plan4 == int(3):
    print('Overwhelmed by the situation, you decide to flee and leave your shelter behind')
    time.sleep(3)
    print('(Coward Ending)')

##############################

quit()