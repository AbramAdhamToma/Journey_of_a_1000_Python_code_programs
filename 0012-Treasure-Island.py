# very simple Treasure Game

            # Sam is a boy who lives in a small house.
            # He was very poor but very smart.
            # He does not go to school but his parents taught him everything he needed.
            # One day when he was walking he saw his friends playing together and asked them
            # to play with them and they confirmed it. Sam was very happy when he was playing
            # and when he was trying to catch the ball he stumbled and felt that something had hit him,
            # so he looked again to see a brick that Sam had grabbed and he saw inside it a piece of paper
            # that was written on it In front of you there is a lot waiting for you inside Either you get
            # Treasure or you get to die. And before you start in this life, you will not gain everything,
            # but beware that you lose everything
            
            # ''')# The story is modified added to it my qoute " And before you start in this life, you will not gain everything, but beware that you lose everything  "




treasure = ('''**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

win=('''
                   ""                         
8b      db      d8 88 8b,dPPYba,
`8b    d88b    d8' 88 88P'   `"8a
 `8b  d8'`8b  d8'  88 88       88
  `8bd8'  `8bd8'   88 88       88
    YP      YP     88 88       88
''')


game_over = (''' 
                    
                    
 ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba,
a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
8b       88 ,adPPPPP88 88      88      88 8PP"""""""
"8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa
 `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"'
 aa,    ,88
  "Y8bbdP"


 ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,
a8"     "8a `8b     d8' a8P_____88 88P'   "Y8
8b       d8  `8b   d8'  8PP""""""" 88
"8a,   ,a8"   `8b,d8'   "8b,   ,aa 88
 `"YbbdP"'      "8"      `"Ybbd8"' 88


            ''')


congrats = ('''
                
                                                                       ,d     
                                                                       88     
 ,adPPYba,  ,adPPYba,  8b,dPPYba,   ,adPPYb,d8 8b,dPPYba, ,adPPYYba, MM88MMM  
a8"     "" a8"     "8a 88P'   `"8a a8"    `Y88 88P'   "Y8 ""     `Y8   88     
8b         8b       d8 88       88 8b       88 88         ,adPPPPP88   88     
"8a,   ,aa "8a,   ,a8" 88       88 "8a,   ,d88 88         88,    ,88   88,    
 `"Ybbd8"'  `"YbbdP"'  88       88  `"YbbdP"Y8 88         `"8bbdP"Y8   "Y888  
                                    aa,    ,88                                
                                     "Y8bbdP"     
                
                ''')



story = print('''
            
            Sam is a boy who lives in a small house.
            He was very poor but very smart.
            He does not go to school but his parents taught him everything he needed.
            One day when he was walking he saw his friends playing together and asked them
            to play with them and they confirmed it. Sam was very happy when he was playing
            and when he was trying to catch the ball he stumbled and felt that something had hit him,
            so he looked again to see a brick that Sam had grabbed and he saw inside it a piece of paper
            that was written on it In front of you there is a lot waiting for you inside Either you get
            Treasure or you get to die. And before you start in this life, you will not gain everything,
            but beware that you lose everything
            
            ''')# The story is modified added to it my qoute " And before you start in this life, you will not gain everything, but beware that you lose everything  "

######################### Start level one #########################################

start_game =print("welcome in Level 1")
level_one_start_message = print("The way to the treasure may be 'Right' or 'Left', choose one way and be careful ")
level_one = input("Write Right or Left? ").capitalize()
if (level_one == "Right"):
    print(game_over)
elif (level_one == "Left"):
    congrats_message =print("congrats you completed level 1 and crossed to level 2") 
    
######################### End level one ###########################################

######################### Start level Two #########################################

level_two_start_message = print("to get the treasure you must choose to 'swim' or 'wait' as you like but be careful ")
level_two =input("Swim or Wait? ").capitalize()
if (level_two == "Swim"):
    print(game_over)
elif (level_two == "Wait"):
    congrats_message =print("congrats you completed level 1 and crossed to level 2") 
    
######################### End level Two ###########################################

######################### Start level Three #######################################

level_Three_start_message = print("you are very near to the treasure but the danger it is very near too you must choose one of the doors to open it Red or Blue or Yellow Be very careful")
level_three = input("Choose one of doors 'Red' or 'Blue' or 'Yellow' ?").capitalize()
if(level_three == "Red" and "Blue"):
    print(game_over)
elif (level_three =="Yellow" ):
    print(congrats)
    print(treasure)
######################### End level Three ###########################################





