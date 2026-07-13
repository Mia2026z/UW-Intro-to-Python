welcome = "start"
bye = "THE END"
wow = "congratulations"
room1 = {
    "Name": "Cave",
    "Description": "A small cave",
    "New item aquired": "Bow and arrow"
}
room2 = {
    "Name": "Palm trees",
    "Description": "Very tall",
    "New enemy spotted": "Giant spider"
}
room3 = {
    "Name": "Think about plan",
    "Description": "You're laying down, and suddenly see a snake moving towards you",
    "New enemy spotted": "Venemous snake"
    }
room4 = {
    "Name": "Hunting",
    "Description": "You go out and shoot a rabbit, then come back to camp.",
    "New item": "Food"
}
room5 = {
    "Name": "Making fire",
    "Description": "You go collect sticks and come back, successfully lighting a fire.",
    "Danger incoming": "A giant bear"
}
room6 = {
    "Name": "Picking berries",
    "Description": "You walk and see a blueberry bush, you're feeling very lucky!",
    "New item": "Rusty saw"
}
print("This is an adventure game where you can explore and choose where you want to go!")
character_name = input("First, you must choose a name for your character that you would like to have: ")
print(f"Welcome to the game {character_name}!")
user_confirm = input("Enter any key to begin: ")

print(welcome.upper(),": It is almost dawn when you wake up, and you find out that you're stuck on an island with the following items in your inventory: ")
inventory = ["A single match", "A bottle of water", "A bag of trail mix", "A pair of glasses","A phone with no battery"]
print(inventory)
print("There are no boats anywhere on the island and you have no way of escape. The only thing you can do is to explore around the island\nand find supplies you can use to call for help.")
user_choice1 = input("You see a cave to the north and palm trees to the east, enter 'cave' or 'palm trees': ")

if(user_choice1 == "cave"):
    print(room1)
    print("Excellant choice, bow and arrow acquired.")
    print("You go back to the place where you woke up, it is now your camp.")

    user_choice2 = input("The sky is now dark, you can either hunt with your bow + arrow, or make a fire. Enter. 'hunt' or 'fire': ")
    if user_choice2 == "hunt":
        print("Uh oh, you run into bears.")
        user_choice3 = input("You can choose to 'run' or 'fight': ")
        if user_choice3 == "run":
            print("You choose to run and narrowly escape being eaten.")
            print("You continue to run back to camp and think about what to do next.")
            user_choice4 = input("You can choose to 'sleep' or 'explore': ")
            if user_choice4 == "sleep":
                print("You're terrified but you choose to sleep.")
                print("You wake up the next day, finding that your trail mix is gone.")
                print("You only have your matches, water, glasses, and phone now.")
                user_choice5 = input("You're starving and need food. You can either pick berries or make a fishing rod. Enter 'berries' or 'rod': ")
                if user_choice5 == "berries":
                    print("You go out to pick berries.")
                    print("You find a huge bush of edible berries and you bring extra with you back to the camp.")
                    print("Now, you decide that you should try starting to call for help.")
                    user_choice6 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice6 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                       
                    elif user_choice6 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
                elif user_choice5 == "rod":
                    print("You successfully make a rod using sticks and vines.")
                    print("You catch 2 fish and go back to camp.")
                    print("You decide that you should try to escape the island.")
                    user_choice7 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice7 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice7 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
            elif user_choice4 == "explore":
                print("You choose to explore the territory next to you.")
                print("You look around and surprisingly find a compass!")
                print("You go back to camp with your findings and think about what to do.")
                user_choice5 = input("You're starving and need food. You can either pick berries or make a fishing rod. Enter 'berries' or 'rod': ")
                if user_choice5 == "berries":
                    print("You go out to pick berries.")
                    print("You find a huge bush of edible berries and you bring extra with you back to the camp.")
                    print("Now, you decide that you should try starting to call for help.")
                    user_choice6 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice6 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice6 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
                elif user_choice5 == "rod":
                    print("You successfully make a rod using sticks and vines.")
                    print("You catch 2 fish and go back to camp.")
                    print("You decide that you should try to escape the island.")
                    user_choice7 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice7 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice7 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
        elif user_choice3 == "fight":
            print("You decide to fight but you're powerless against the bears.")
            print("Your bow + arrow are wasted and you're now in horrible condition.")
            print("You return to your camp.")
            user_choice4 = input("You can choose to 'sleep' or 'explore': ")
            if user_choice4 == "sleep":
                print("You're terrified but you choose to sleep.")
                print("You wake up the next day, finding that your trail mix is gone.")
                print("You only have your matches, water, glasses, and phone now.")
                user_choice5 = input("You're starving and need food. You can either pick berries or make a fishing rod. Enter 'berries' or 'rod': ")
                if user_choice5 == "berries":
                    print("You go out to pick berries.")
                    print("You find a huge bush of edible berries and you bring extra with you back to the camp.")
                    print("Now, you decide that you should try starting to call for help.")
                    user_choice6 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice6 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice6 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
                elif user_choice5 == "rod":
                    print("You successfully make a rod using sticks and vines.")
                    print("You catch 2 fish and go back to camp.")
                    print("You decide that you should try to escape the island.")
                    user_choice7 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice7 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice7 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
            elif user_choice4 == "explore":
                print("You choose to explore the territory next to you.")
                print("You look around and surprisingly find a compass!")
                print("You go back to camp with your findings and think about what to do.")
                user_choice5 = input("You're starving and need food. You can either pick berries or make a fishing rod. Enter 'berries' or 'rod': ")
                if user_choice5 == "berries":
                    print("You go out to pick berries.")
                    print("You find a huge bush of edible berries and you bring extra with you back to the camp.")
                    print("Now, you decide that you should try starting to call for help.")
                    user_choice6 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice6 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice6 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
                elif user_choice5 == "rod":
                    print("You successfully make a rod using sticks and vines.")
                    print("You catch 2 fish and go back to camp.")
                    print("You decide that you should try to escape the island.")
                    user_choice7 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice7 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice7 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
    elif user_choice2 == "fire":
        print("You use your matches and successfully make a fire.")
        print("You are warm for the night but you must find food tomorrow.")
        user_choice5 = input("You're starving and need food. You can either pick berries or make a fishing rod. Enter 'berries' or 'rod': ")
        if user_choice5 == "berries":
                    print("You go out to pick berries.")
                    print("You find a huge bush of edible berries and you bring extra with you back to the camp.")
                    print("Now, you decide that you should try starting to call for help.")
                    user_choice6 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
                    if user_choice6 == "sand":
                        print("You write an SOS message into the sand and wait.")
                        print("After one day, you suddenly see a helicopter and wave your hands.")
                        print("The helicopter sees you, and you are rescued.")
                        print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                        print(bye.lower())
                    elif user_choice6 == "raft":
                        print("You build a raft and set sail from the island.")
                        print("Just as you're losing hope, you suddenly see land.")
                        print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                        print(bye.lower())
        elif user_choice5 == "rod":
            print("You successfully make a rod using sticks and vines.")
            print("You catch 2 fish and go back to camp.")
            print("You decide that you should try to escape the island.")
            user_choice7 = input("You have two choices. You can either write a help message in the sand, or build a raft to escape. Enter 'sand' or 'raft': ")
            if user_choice7 == "sand":
                print("You write an SOS message into the sand and wait.")
                print("After one day, you suddenly see a helicopter and wave your hands.")
                print("The helicopter sees you, and you are rescued.")
                print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
                print(bye.lower())
            elif user_choice7 == "raft":
                print("You build a raft and set sail from the island.")
                print("Just as you're losing hope, you suddenly see land.")
                print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
                print(bye.lower())
        
elif(user_choice1 == "palm trees"):
    print(room2)
    print("Oh no, spotted by giant spider.")
    print("You hide and escape being eaten.")
    print("You go back to the place you woke up, it is now your camp.")
    user_choice8 = input("The sky is now dark, you can either make a fire, or gather berries. Enter 'fire' or 'berries': ")
    if user_choice8 == "fire":
        print("You make a fire with your matches.")
        print("You decide to sleep for the night.")
        user_choice9 = input("You can now either explore or sleep more. Enter 'explore' or 'sleep': ")
        if user_choice9 == "explore":
            print("You go out and explore.")
            print("You find a rusty knife while exploring.")
            print("You go back to camp.")
            user_choice12 = input("You can either go explore near the water, or sleep at camp. Enter 'water' or 'sleep': ")
            if user_choice12 == "water":
                print("You go to the water and rinse off your wounds.")
                print("You find fireworks which could save you.")
                print("You think it's time to escape.")
                user_choice15 = input("You will now shoot the firework into the sky in hopes of someone seeing it. Are you ready? Enter yes/no: ")
                if user_choice15 == "yes" or "y" or "yea" or "yeah" or "Yes" or "Yep" or "yep":
                    print("You set off the firework.")
                    print("A helicopter sees you.")
                    print(wow.upper(),"! YOU HAVE SURVIVED AND ESCAPED THE ISLAND!")
                else:
                    print("You don't set off the firework, you starve to death on the island.")
                    print("You failed to escape the island, try again next time!")
            if user_choice12 == "sleep":
                print("You start sleeping.")
                print("You wake up finding everything burning with fire.")
                print("You nearly escape burning yourself.")
            user_choice16= input("You now have two choices, go to the water or look for other items. Enter 'water' or 'items': ")
            if user_choice16 == "water":
                print("You go to the water and rinse off your wounds.")
                print("You find fireworks which could save you.")
                print("You think it's time to escape.")
                user_choice17 = input("You will now shoot the firework into the sky in hopes of someone seeing it. Are you ready? Enter yes/no: ")
                if user_choice17 == "yes" or "y" or "yea" or "yeah" or "Yes" or "Yep" or "yep":
                    print("You set off the firework.")
                    print("A helicopter sees you.")
                    print(wow.upper(),"! YOU HAVE SURVIVED AND ESCAPED THE ISLAND!")
                else:
                    print("You don't set off the firework, you starve to death on the island.")
                    print("You failed to escape the island, try again next time!")

        elif user_choice9 == "sleep":
            print("You keep sleeping.")
            print("You wake up finding everything burning with fire.")
            print("You nearly escape burning yourself.")
            user_choice13 = input("You now have two choices, go to the water or look for other items. Enter 'water' or 'items': ")
            if user_choice13 == "water":
                print("You go to the water and rinse off your wounds.")
                print("You find fireworks which could save you.")
                print("You think it's time to escape.")
                user_choice14 = input("You will now shoot the firework into the sky in hopes of someone seeing it. Are you ready? Enter yes/no: ")
                if user_choice14 == "yes" or "y" or "yea" or "yeah" or "Yes" or "Yep" or "yep":
                    print("You set off the firework.")
                    print("A helicopter sees you.")
                    print(wow.upper(),"! YOU HAVE SURVIVED AND ESCAPED THE ISLAND!")
                else:
                    print("You don't set off the firework, you starve to death on the island.")
                    print("You failed to escape the island, try again next time!")
            elif user_choice13 == "items":
                print("You don't find any more items.")
                print("You don't have anymore energy to walk.")
                print("You collapse on the cold wet jungle floor.")
                print("You failed to escape the island, it's okay, try again next time!")
    elif user_choice8 == "berries":
        print("You decide to go pick berries.")
        print("You encounter bears.")
        print("You are now injured and lose all of your supplies.")
        user_choice10 = input("You can now go back to camp or go in the water. Enter 'camp' or 'water': ")
        if user_choice10 == "camp":
            print("You go back to camp.")
            print("You find that your camp is already taken over by snakes.")
            print("You are bitten, you die.")
            print("You failed to escape the island. It's okay, try again next time!")
        elif user_choice10 == "water":
            print("You go to the water and rinse off your wounds.")
            print("You find fireworks which could save you.")
            print("You think it's time to escape.")
            user_choice11 = input("You will now shoot the firework into the sky in hopes of someone seeing it. Are you ready? Enter yes/no: ")
            if user_choice11 == "yes" or "y" or "yea" or "yeah" or "Yes" or "Yep" or "yep":
                print("You set off the firework.")
                print("A helicopter sees you.")
                print(wow.upper(),"! YOU HAVE SURVIVED AND ESCAPED THE ISLAND!")
            else:
                print("You don't set off the firework, you starve to death on the island.")
                print("You failed to escape the island, try again next time!")