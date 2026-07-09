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
    "New item": "You have acquired food so you won't starve."
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
user_choice1 = input("You see a cave to the north and palm trees to the east, enter 'cave' or 'palm trees'(Make sure to type the exact word): ")

if(user_choice1 == "cave"):
    print(room1)
    print("Good job, you found a bow and arrow to defend yourself!")
    print("You go back to the place where you woke up and think about what you want to do next.")
elif(user_choice1 == "palm trees"):
    print(room2)
    print("Oh no, you're spotted by a giant spider and it starts to chase you!")
    print("You frantically look around for a place to hide, and you see a good place where you can camouflage! The spider looks around but can no longer see you and you breathe a sigh of relief.\nYou go back to the place you woke up and think about what to do. BONUS: Bow and arrow for escaping danger!")

user_choice2 = input("The sky is now dark, you have two choices. You can either stay at camp and think about how to escape, or use your newly acquired bow and arrow to hunt for food. 'think' or 'hunt'?: ")
if(user_choice2 == "think"):
    print(room3)
    print("Uh oh! You see a dangerous snake slowly moving towards you!")
    print("You must find someway to distract or escape it!")
elif(user_choice2 == "hunt"):
    print(room4)
    print("Excellant, you've now acquired food!")
    print("You quickly find a sharp rock and prepare the rabbit but you realize that it's raw.")

user_choice3 = input("You can now choose to either light a fire, or run off to pick berries. Enter 'fire' or 'berries': ")
if(user_choice3 == "fire"):
    print(room5)
    print("Oh no, the light from the fire attracted the attention of a bear!")
    print("You are forced to abandon your camp and only managed to save your water, glasses, and phone.")
elif(user_choice3 == "berries"):
    print(room6)
    print("Wow! Today really is your lucky day, you found berries and a saw that will be very useful!")
    print("The berries fill you up and you even have extra! You go back to camp.")
    print("Uh oh, it looks like a wild animal has come to your camp and took almost all your supplies! You only have your water, glasses, and phone... ")

user_choice4 = input("No danger is evident now and you drink the water. You decide to try and leave the island! You can either try and write a message into the sand or build a raft! Enter 'write' or 'build': ")
if(user_choice4 == "write"):
    print("You write a SOS message in the sand with a stick.")
    print("Suddenly, you see a helicopter fly by! You immediently wave your hands and the helicopter spots you!")
    print(wow.upper(),"! YOU HAVE ESCAPED AND SURVIVED THE ISLAND!")
    print("THE END.")
elif(user_choice4 == "build"):
    print("You built a raft and set out to go to the nearest land next to you.")
    print("It's been 3 days and you're starving....suddenly, you see land!")
    print("The villagers are kind and help you, you survive and make it safely home, ", wow.upper(), "!!!")
    print(bye.lower())