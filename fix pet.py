# Welcome banner and pet names + type
print("Welcome to the digital pet game where you can care for your own virtual companion!")
pet_name = input("Enter a name for your pet: ")
pet_type = input("Enter which pet you would like to have;  dog, cat, or dragon:  ")
# Validate pet type
while pet_type not in ("dog", "cat", "dragon"):
    print("Must enter a pet type: dog, cat, or dragon: ")
    pet_type = input("Enter which pet you would like to have;  dog, cat, or dragon: ")
# Pet emoji
pet_emoji = ""
if (pet_type == "dog"):
    pet_emoji = ("🐶")
elif (pet_type == "cat"):
    pet_emoji = "🐱"
elif (pet_type == "dragon"):
    pet_emoji = "🐉"
# Starting stats
hunger=int(80)
happiness=int(80)
health=int(80)
energy=int(80)
cleanliness=int(80)
# Pet has hatched
print(f"Congratulations! Your pet {pet_type} named {pet_name} has now hatched! Pet emoji: {pet_emoji}")
# Display bar variables
hunger_bar = ""
happiness_bar = ""
health_bar = ""
# Turn variable
turn = 5
# Loop code
for l in range(1, turn+1):
    print("Turn: ", l)
# Display bar
    hunger_bar = "X" * (hunger//10)
    print("Hunger:",hunger, hunger_bar)
    happiness_bar = "X" * (happiness//10)
    print("Happiness:",happiness, happiness_bar)
    health_bar = "X" * (health//10)
    print("Health",health, health_bar)
# Menu choices
    user_choice = input("Choose a number from the menu: 1.Feed  2.Play  3.Sleep  4.Vet: ")
    while user_choice not in ("1", "2", "3", "4"):
        print("Must enter a number: 1, 2, 3, or 4: ")
        user_choice = input("Choose a number from the menu: 1.Feed  2.Play  3.Sleep  4.Vet: ")
# Results corresponding to user menu choice
    if user_choice == "1":
        health -= 5
        happiness += 10
        hunger += 25
    elif user_choice == "2":
        health += 5
        happiness += 25
        hunger -= 15
        if pet_type == "dog":
            happiness += 10
    elif user_choice == "3":
        health += 20
        happiness += 10
        hunger -= 10
        if pet_type == "cat":
            health += 10
    elif user_choice == "4":
        health += 30
        happiness -= 15
        hunger += 5
# Natural decay
    happiness -= 5
    hunger -= 10
    if (pet_type == "dragon"):
        hunger -= 10
# No stat higher than 100 and lower than 0
    if(hunger >= 100):
        hunger = 100
    elif(hunger <= 0):
        hunger = 0

    if(happiness >= 100):
        happiness = 100
    elif(happiness <= 0):
        happiness = 0

    if(health >= 100):
        health = 100
    elif(health <= 0):
        health = 0

    if(energy >= 100):
        energy = 100
    elif(energy <= 0):
        energy = 0

    if(cleanliness >= 100):
        cleanliness = 100
    elif(cleanliness <= 0):
        cleanliness = 0
# Health penalty if pet is starving
    if(hunger <= 0):
        health -= 15
# Health is 0 and user game over, break
    if(health <= 0):
        print("GAME OVER, MAYBE NEXT TIME...")
        break
# Stat lower than 20 warning
    if(hunger < 20):
        print("Warning, your pet is getting hungry!!!")
    
    if(happiness < 20):
        print("Warning, your pet is getting sad!!!")
    
    if(health < 20):
        print("Warning, your pet's health is plummeting!!!")
# Mood scale
    if (happiness >= 80):
        print(f"""{pet_name} is feeling Ecstatic!""")
    elif (79 >= happiness and happiness >= 60):
        print(f"""{pet_name} is happy!""")
    elif (59 >= happiness and happiness >= 40):
        print(f"""{pet_name} is feeling okay.""")
    elif (20 >= happiness and happiness >= 39):
        print(f"""{pet_name} is feeling sad.""")
    elif (0 >= happiness and happiness >= 19):
        print(f"""{pet_name} is feeling miserable, cheer them up.""")
# Final score calculation
average = (hunger + happiness + health) // 3
score = average * turn
if (score >= 400):
    print("AMAZING JOB, LEGENDARY OWNER!!!")
elif (score >= 300):
    print("Nice job, you're a Great Owner!")
elif (score >= 200):
    print("Okay, you're a pretty good owner!")
else:
    print("Keep practising, maybe try again?")


