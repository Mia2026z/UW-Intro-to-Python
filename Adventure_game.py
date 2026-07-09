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
    user_choice3 = input("The sky is now dark, you can either make a fire, or gather berries. Enter 'fire' or 'berries': ")