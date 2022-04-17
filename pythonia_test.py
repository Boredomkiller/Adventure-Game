import time
import random

items = []
name = []
profession = []
r = []  # R for Rats!
g = []  # G for Goblins!


def d20_roll():
    d20_dice_roll = random.randint(1, 20)
    r.append(d20_dice_roll)


def d12_roll():
    d12_dice_roll = random.randint(1, 12)
    g.append(d12_dice_roll)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def play_again():
    while True:
        choice = input("Do you want to play again?").lower()
        if choice == 'y':
            print_pause("Of course you do! This game is amazing!")
            intro()
            first_choice()
        elif choice == 'n':
            print_pause("Yeah I don't blame you, this game sucks.")
            exit(0)


def intro():
    print_pause("After months at sea you arrive "
                "to the newfound land of PyThonia!")


def first_choice():  # Entry and Guild Registration.
    choice = input("Do you dare to Seek riches & glory?!\n"
                   "Enter Y/N\n").lower()
    if choice == "y":
        print_pause("Of Course you do! Why else would you have"
                    "come to these mysterious and dangerous lands!?\n")
        print_pause("*Glancing about you see gawdy billboard "
                    "advertising riches and glory at the "
                    "local adventurer's guild*")
        print_pause("You make your way through the flourishing settlement"
                    "from the dock ward to the central square.\n")
        guild_entry()

    elif choice == "n":
        print_pause("Seriously?\n")
        print_pause("Well...\n"
                    "I guess you board the boat "
                    "and head back to a life of peasantry?\n")

        print_pause("*Dungeon master throws his "
                    "game notes out the window*\n")

        print_pause("Congrats, you win at...."
                    "being a peasant or something.\n"
                    "Good luck with serfdom.\n")
        play_again()
    else:
        print_pause("Its a simple 'yes' or 'no' question...")
        print_pause("Try again.")
        first_choice()


def guild_entry():

    print_pause("*You arrive at the Guild hall in the central square.*\n"
                "*All around you are various beings.\n*"
                "*Some humanoids ranging from pointed eared elves"
                "to shorter stronger dwarves*\n"
                "*Some even shorter, much like the sharply dressed gnome"
                "striding through the main guild hall"
                "with an heir of respected authority*\n")  # Description
    print_pause("Welcome to the Pythonia guild hall!")  # Dialogue
    guild_registration()


def guild_registration():   # Choice 'Y'/'N'
    choice = input("Is this your first time here?\n"
                   "Enter Y/N\n").lower()
    if choice == 'y':
        print_pause("Excellent! Always nice to see a new face!\n"
                    "Lets get you registered at the front desk "
                    "so you can start earning"
                    "yourself some gold!\n")  # Dialogue

        print_pause("*The sharply dressed gnome leads you to the front desk "
                    "to a polite and well dressed dragonborne attendent*\n"
                    "*The attendent perks up immediately "
                    "at the sight of her boss and quickly hides "
                    "a small novel she was reading"
                    "behind the desk.\n")  # Description
        print_pause("Welcome to Pythonia Guild Hall, hun!\n"
                    "Here you pickup bounties "
                    "and bring them back upon completion to receive gold.\n"
                    "Now lets get you registered!")  # Dialogue

        print_pause("*The dragonborn quickly ducks under the counter\n"
                    "and strains to lift a large crimson ledger "
                    "that she heaves onto the desk"
                    "with a heavy thud*")  # Description
        print_pause("Now, lets just start with your name."
                    "Who are you?")  # Dialogue
        name = input("Please enter Name: ")
        print_pause(f"So very nice to meet you, {name}!")
        class_selection()

    elif choice == 'n':
        print_pause("Nice try, kid! I know every face in Pythonia!\n"
                    "It's smart to be untrusting of strangers though!\n"
                    "I like your moxie! Have a coupon"
                    "for a free drink at the bar!")  # Dialogue
        items.append("Free Drink Coupon")
        print_pause("*Obtained: Free Drink Coupon*")
        guild_registration()  # Potential exploit! Too bad they're esxpired!
    else:
        print_pause("You're gonna have to speak up"
                    "or use 'Yes' or 'No' questions,\n"
                    "Dragon bit my ear off on day one!")  # Dialogue
        # Description
        print_pause("*He quickly jerks his head to the left"
                    "to show his scarred and gnarwled mess "
                    "of what was once his ear*")  # Description
        guild_registration()


def class_selection():
    print_pause(f"Now that we've been properly introduced."
                " What is your profession?\n")  # Dialogue
    profession = input("Please choose from the following:\n"
                       "Fighter\n"
                       "Cleric\n"
                       "Ranger\n").lower()
    if profession in "fighter":
        print_pause("Well I just knew as soon as you walked in"
                    "that you were mighty fighter!"
                    "please help yourself to our training yard")  # Dialogue
        bounty_board()
    elif profession in "cleric":
        print_pause("I could tell straight away "
                    "you had a holy look about you!"
                    "The temple is just across the street")  # Dialogue

        bounty_board()

    elif profession in "ranger":
        print_pause("Indeed you are, the bow kinda gives it away!"
                    "You should try the hunting in the area!"
                    "Boars as big as horses!")  # Dialogue

        bounty_board()
    else:
        print_pause("Haven't heard of that. Please select the class"
                    "that closely represents "
                    "what your profession is.")  # Dialogue
        class_selection()


def bounty_board():
    print_pause("*You approach the bounty board and see two posters*\n"
                "1. Bounty: Rodents of unusal size in my cellar!\n"
                "2. Bounty: Golbins on the north road!\n")  # Description
    choice = input("Please select '1' or '2'\n")
    if choice == "1":
        print_pause("*Obtained: Easy Bounty ")
        items.append("Easy Bounty")
        easy_bounty()
    elif choice == "2":
        print_pause("*Obtained: Normal Bounty ")
        normal_bounty()
    else:
        print_pause("Please pick from the two bounties")
        bounty_board()


def easy_bounty():
    print_pause("*You grab the bounty paper and follow "
                "the directions to the King's Keep Tower*\n"
                "*You meet the robust dwarven tavern owner*\n")  # Description
    print_pause("GREETINGS! You here for the bounty poster?\n")  # Dialogue
    choice = input("Y/N\n").lower()
    if choice == 'y':
        print_pause("OH Fantastic! "
                    "heres the key to the cellar!")  # Dialogue
        items.append("key")
        print_pause("*Obtained: Cellar Key*")
        rat_cellar()
    elif choice == 'n':
        print_pause("Oh? Well thats unfortunate."
                    "I can't open my tavern until"
                    "all the rats are disposed of.")  # Dialogue
        bounty_board()
    else:
        print_pause("Not really a 'yes' or 'no' "
                    "response...lets try this again!")
        easy_bounty()  # Need to figure out how to skip decription & dialogue.


def rat_cellar():
    print_pause("*You approach the cellar door.*\n"
                "*behind the door you hear the "
                "scurrying and scratching*\n")  # Description
    if "key" in items:
        print_pause("*You use the key the tavern keeper "
                    "gave you to unlock the cellar door.*\n"
                    "*You cautiously enter the cellar."
                    "Barrels stacked high creates a labrynth"
                    " of booze and the smell of cured meats fill the air*")
        rat_encounter()
    else:
        print_pause("*The Door is firmly locked.* \n"
                    "*behind the door you hear the scurrying and scratching"
                    "Perhaps if you had a key you could unlock this door.*")


def rat_encounter():
    print_pause(f"*Suddenly {r} rats leap out at you"
                " from the top of the barrels!*")
    choice = input("Fight!/RUN!").lower()
    if choice == "fight":
        print_pause("Luckily you carry one of the rats' many weaknessess!\n"
                    "A SWORD!\n"
                    f"With dazzeling grace you slay the rats\n")
        items.append("*Obtained: Completed Bounty*")
        reward()

    elif choice == "run":
        print_pause("You bravely flee the hoard of rats."
                    "Maybe adventering isnt quite your thing...\n")
        choice = input("Care to try again?\n"
                       "Y/N\n")
        if choice == 'y':
            print_pause("Thats the spirit!"
                        "Get in there and show those "
                        "unusally sized rodents whose boss!")
            rat_encounter()
        elif choice == 'n':
            print_pause("With that your adventuring career "
                        "comes to a shameful end..."
                        "maybe you can get a job as a "
                        "goat farmer or something? \n")
            play_again()
        else:
            print_pause("Try to keep it as 'yes' or 'no' answers.")


def normal_bounty():
    print_pause("*You grab the bounty paper"
                "and follow the directions to the north road*")
    goblin_encounter_choice()


def goblin_encounter_choice():
    print_pause(f"*Suddenly, {g} Goblins"
                "leap from various hiding spots to ambush you.*")
    choice = input("Do you 'Fight' or 'Run'?\n").lower()
    if choice in 'fight':
        print_pause("You manage to fight off a few goblins"
                    "but more reinforcements arrive.")
        print_pause("Should you press your luck against the goblin horde?")
        choice = input("Y/N\n").lower()
        if choice in 'y':
            print_pause("You fight bravely yet foolishly "
                        "and are quickly overwhelmed"
                        "by the goblin reinforcments.")
            print_pause("GAME OVER")
            play_again()
        elif choice in 'n':
            print_pause("You bravely run away to fight another day!")
            print_pause("*The goblins laugh and taunt you "
                        "as you perform your tactical retreat*")
            bounty_board()
    elif choice in "run":
        print_pause("You bravely run away"
                    "to fight another day!")
        print_pause("*The goblins laugh and taunt you "
                    "as you perform your tactical retreat*")
        bounty_board()
    else:
        print_pause("The goblins don't even know what"
                    "you're trying to accomplish.\n"
                    "They understand fighting and running away\n")
        goblin_encounter_choice()


def reward():
    print_pause("*After completing your bounty you return to the guild hall*\n"
                "*You're greeted by the same dragonborn attendent.*\n"
                "*She beams proudly at you "
                "as you present the completed bounty*")
    print_pause("Now I just knew you had it in you.\n"
                "Keep up the good work "
                "and you'll be a great adventurer in no time!\n")
    print_pause("*Obtained: 25 Gold*")
    items.append("*25 Gold*")
    print_pause("With your first quest completed \n"
                "and many more to go\n"
                "you go to bed with a full purse and a full belly.\n"
                "This adventurering life is working out all right.\n")
    print_pause("CONGRATS! You had a successful first quest!")
    play_again()


def play_game():
    intro()
    first_choice()


play_game()
