import time
from cfonts import render, say


output = render('Welcome', colors=['blue', 'blue'], align='center')
print(output)
time.sleep(1)

output = render('To The', colors=['red', 'red'], align='center')
print(output)
time.sleep(1)

output = render('Story', colors=['white', 'white'], align='center')
print(output)
time.sleep(2)

# Story starts here ----------------------

def option_check(option):
  updated = option
  while True:
      valid_values = ["saiyan", "mage", "human", "hero", "villian"]
      if updated.lower() in valid_values:
          break
      else:
          updated = input("Sorry we didn't catch that: ").lower()
  return updated

def num_check(value):
  updated = value
  while True:
      if updated.isdigit():
          break
      else:
          updated = input("Invalid planet!\n Try again: ")
  return int(updated)


print("You just woke up ... ")
time.sleep(1.5)

name = input("Your name is ")
time.sleep(1)

species = option_check(input("\nI am a (Saiyan, Human, Villian): "))

print("\nYou chose the ")
time.sleep(1)

output = render(species.capitalize(), colors=['green', 'green'], align='center')
print(output)
time.sleep(1)

output = render("story", colors=['red', 'red'], align='center')
print(output)
time.sleep(1)

# Story splits here ----------------------

if species == "saiyan":
  print("Grief washes upon you as you witness your home planet gets turned into space dust. Luckly, you was able to barely escape via a space capsule.")

  time.sleep(1)
  print("You've heard from a fellow saiyan before that there are two planets in this universe that possess seven wishing granting balls.")

  time.sleep(1)
  print("Determined to wish your home planet back to life, you began to setting your cordinates.")

  time.sleep(1)
  print("Suddlenly a thought raises in your head. Should you go to planet-789 where the beings there have lower power levels and the wishing balls only grant one wish?")

  time.sleep(1)
  print("Or should you go to planet-781 where the beings there are much stronger however, the wishing balls grant three wishes rather than on?") 

  time.sleep(2)
  planet_choice = num_check(input("Enter planet coordinates(781 or 789): "))
  
  print("Knowing that the trip will take some time, you rest as the ship slowly flies towards your destination.")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")

  if planet_choice == 789: 
    print("The green planet, filled with beautiful clear blue water seemed like a site to be untold of. Capitvated by its beauty, you quickly brushed those distractions aside, fixated on obtaining your wish to save your home planet.")
    time.sleep(1)
    print("You landed in the of a middle urbanize city which seem to be in the admidts of an attack. You get out of your space pod an you notice a small bunker underneath where your pod landed.")
    time.sleep(1)
    print("This bunker was holding captive dozens of people whom seem to have a blank expression. One seem to have notice you and as you began to approach them a thunderous clap zoomed by your ears.")
    time.sleep(1)
    print("Alerted by the commotion you quickly fly towards the site of noise, leaving a cloud of dust and debris for the people to inhale. Arriving at the scence faster than never before, you watch in amazement as two fighters clash their fists together.")
    time.sleep(1)
    print("You grind your teeth and clench your fists in excitement as you see a potential challenge. You approach   ")


  elif planet_choice == 781:
    print("Your ship crash landed into the planet causing a huge crater in the ground. As you slowly open your pod a barrage of energy blasts come across your way.")
    time.sleep(1)
    print("You brushed those attacks off and demand to use the dragon balls. \n The habitants on the planet ignores your requests and continues their assault")
    time.sleep(1)
    print("A long and brutal battle ensues. You barely defeat these powerful beings as their technique far outclasses yours.")
    time.sleep(1)
    print("Badly battle damaged, you limp towards the site of the wishing granting orbs. The orbs luminosity spread across the outskirts of the sky and you begin to cite your wishes.")
    time.sleep(1)
    print("Suddenly your hit in the head by a stray blast, causing the wishes you made to be negated. As you slowly lose consciousness you curse yourself for failing to save your home planet. Everything goes dark as you accept your fate.") 

  
    
  else:
    print("It appears that you've put in a wrong coordinate, sending you off course.")
    time.sleep(1)
    print("After being sometime in space, your capsule runs out of fuel")
    time.sleep(1)
    print("You soon disappear in the empty vacuum of space")
    
    output = render("Bad", colors=['red', 'red'], align='center')
    print(output)
    output = render("Ending", colors=['red', 'red'], align='center')
    print(output)   



elif species == "human":
  print("You get up from your bed and get ready for work.") 
  time.sleep(2)
  print("As you walk to the bathroom, you get a strange feeling slowly crawling up your spine.")
  time.sleep(2)
  off_day = input("Should you take the day off?: ")
  if off_day == "Yes":
    time.sleep(2)
    print("\nYou let your manager know that you didn't feel too well. You go back to bed and watch TV. You fall asleep soon after for a few hours")
    time.sleep(1)
    print(".")
    
    time.sleep(1)
    print("..")

    time.sleep(1)
    print("...")
    time.sleep(1)
    print("You wake up in the middle of the night.")
    print("As you go to check what time it is you notice you've recieved 50 new messages from your bestfriend Jeff 4 hours ago.")
    time.sleep(1)
    print("You open the messages up.")
    time.sleep(1)
    print("They all say the same the thing for some reason, '" + name + " ... --- ...'")
    print("You think nothing of it, considering your phone is always glitching out.")
    print("So you get up from bed and make yourself food, then go back to bed.")
    time.sleep(1)
    print(".")
    
    time.sleep(1)
    print("..")

    time.sleep(1)
    print("...")
    time.sleep(1)
    print("You wake up the next day and find out that so many things has happened while you slept")
    print("Apparently, Mathew the Villian attacked the city and was defeated by Marieke as well as an unknown hero called Semaab")
    print("Crazy Huh! It's probably all a lie anyways, who believes the news these days.")
    print("You also found it crazy that Jeff never messaged you again")
    print("Thats fine, friends come and go anyways.")



  else:  
    print("You shake it off... for now and you finish getting ready for work.")
    print("As you walk to the front door, every thing goes dark... ")
    print(".")
    
    time.sleep(1)
    print("..")

    time.sleep(1)
    print("...")

    time.sleep(1)
    print("Slowly but surely your vision comes back. You don't really know where you're at as the room you're in has little to no lighting. You do however, feel the ominious arua you've felt before at your house. ")
    
    time.sleep(1)
    print("Suddenly...")
    
    time.sleep(1)
    print("BANG!!!!!!!!!!!!!!")
    
    print("A huge ball came crashing from the ceiling, almost destroying the room entirely, luckily you was at a corner and survived it")
    time.sleep(2)

    print("As you reinspect your surroundings you notice that the crash open up a crack in one of the walls, believe it or not, you think you can crawl your way out through it. So you choose to do so since the room was collapsing anyways.")
    time.sleep(2)
    
    print("After crawling for what seemed to be an eterinty you finally poke your head out, revealing that the huge ball was actually a space pod that caused an enormous crater to appear")
    time.sleep(2)
    
    print("You see the worlds most famous hero, Marieke the Greatest, interacting with an unknown being")
    time.sleep(2)
    
    print("They seemlessly disappear for a few minutes, then reappear.")
    print("The mysterious being seems to be in sync with Marieke, I wonder who she is")
    print("On the spur of the moment, another stranger appears and simultaneously takes them both on. ")
    print("Oddly enough, this reminds me of a familiar boss fight. I wonder if thats what its based off.any.")

elif species.lower() == "villian":
  print(name + ": Finally after 20 so years, my plan of controlling the entire human race will be initiated today.")
  time.sleep(1)
  print(name + ": Cookie set up the preparations NOW!!!!")
  print(name + ": I will never forgive these vile creatures for excommunicating me and my minion. We were only trying to better the planet with our... -")
  time.sleep(1)
  print("Cookie : Lord " + name + ", that fiend(hero) is trying to sabotage with our plans!!!!  Woof")
  mind_choice = input("Cookie: Should we continue with our plans lord " + name + "?Woof: ")
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")
  time.sleep(1)
  if mind_choice == "Yes":
    print(name + ": I've waited to long for this, we shall still continue with our plans \nNOW GET BACK TO SETTING UP MY DEVICE!!!!")

  else:
    print(name + ": Darn it we must not let that hero get with our plans!!!! Mage set up our defensive measures NOW!!!!")


else:
  print("I wonder how you got here.")



output = render("The End", colors=['white', 'white'], align='center')
print(output)   