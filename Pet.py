print("Welcome to the Digital Pet game where you can care for your very own virtual companion!")
pet_name = input("What would you like to name your pet? ")
while True:
    try:
        pet_type = int(input("What type of pet would you like to have? 1. Dog 2. Cat 3. Dragon:  "))
        if 1 <= pet_type <= 3:
            break
        else:
            print("Number must be 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
if pet_type == 1:
    pet_type = "Dog"
elif pet_type == 2:
    pet_type = "Cat"
elif pet_type == 3:
    pet_type = "Dragon"
else:
    while pet_type not in [1, 2, 3]:
        pet_type = input("Confirm, what type of pet would you like to have? 1. Dog 2. Cat 3. Dragon:  ")
    if pet_type == 1:
        pet_type = "Dog"
    elif pet_type == 2:
        pet_type = "Cat"
    elif pet_type == 3:
        pet_type = "Dragon"
hunger=int(80)
happiness=int(80)
health=int(80)
energy=int(80)
cleanliness=int(80)
print("Now, it's time to hatch your pet!")
print(f"Congratulations! You now have a {pet_type} named {pet_name}. ")
if(pet_type == "Dog"):
    pet_emoji=("🐶")
elif(pet_type == "Cat"):
    pet_emoji=("🐱")
elif(pet_type == "Dragon"):
    pet_emoji=("🐉")
else:
    pet_emoji=(" ")
print(f"Pet Moji:{pet_emoji}")

while health > 0:
    i=0
    if(i < 5):
        print("Turn: ", i+1)
        turn = i+1
        hunger-= 10
        happiness-= 5
        
    elif i > 5:
        break
if(pet_type == "3"):
    hunger-=10
print(f"{pet_name} is currently {hunger}% hungry, {happiness}% happy, {health}% healthy, {energy}% energetic, and {cleanliness}% clean.")
while True:
            print("Choose a number, you can: 1.Feed  2.Play  3.Sleep")
            user_choice = input("Enter 1, 2, or 3: ")
            if user_choice == "1":
                    hunger += 25
                    happiness += 10
                    health -= 5
            elif user_choice == "2":
                happiness+= 10
                hunger -= 15
                health += 5
            elif pet_type == "1":
                happiness += 25
            elif user_choice == "3":
                    health += 20
                    happiness += 10
                    hunger -= 10
            elif pet_type == "2":
                health += 10
            while user_choice not in ("1", "2", "3"):
                user_choice = input("Invalid choice, please put in 1, 2, or 3: ")
            if(hunger > 100):
                hunger = 100
            if(happiness > 100):
                happiness = 100
            if(health > 100):
                health = 100
            if(energy > 100):
                energy = 100
            if(cleanliness > 100):
                cleanliness = 100  
            if(hunger <= 0):
                health -= 15
                print("Your pet is starving!")
            if(hunger<20):
                print("Warning, your pet is hungry!")
            elif(happiness<20):
                print("Warning, your pet is sad!")
            elif(health):
                print("Warning, your pet's health is low!")
            elif(energy):
                print("Warning, your pet is feeling tired!")
            elif(cleanliness):
                print("Warning, it's time to clean your pet!")
            hunger_bar=""
            j=(hunger//10)
            while(j>0):
                hunger_bar=hunger_bar+"X"
                #print(hunger_bar)
                j-=1
            print(f"Hunger is {hunger}%: "+hunger_bar)
            happiness_bar=""
            k=(happiness//10)
            while(k > 0):
                happiness_bar=happiness_bar+"X"
                #print(happiness_bar)
                k-=1
            print(f"Happiness is {happiness}%: "+happiness_bar)
            health_bar=""
            l=(health//10)
            while(l>0):
                health_bar=health_bar+"X"
                #print(health_bar)
                l-=1
            print(f"Health is {health}%: "+health_bar)
            print("Your pet's current stats are: ")
            print(f"Hunger: {hunger}%")
            print(f"Happiness: {happiness}%")
            print(f"Health: {health}%")
            print(f"Energy: {energy}%")
            print(f"Cleanliness: {cleanliness}%")
            if(happiness>=80):
                print(f"""{pet_name} is feeling Ecstatic!""")
            elif(79>= happiness>=60):
                print(f"""{pet_name} is happy!""")
            elif(59>=happiness>=40):
                print(f"""{pet_name} is feeling okay.""")
            elif(20>=happiness>=39):
                print(f"""{pet_name} is feeling sad.""")
            elif(0>=happiness>=19):
                print(f"""{pet_name} is feeling miserable, cheer them up.""")
            if health == 0:
                print("STOP, GAME OVER, YOUR PET HAS DIED.")
                break
i+=1    

average = (hunger + happiness + health) // 3
score = average * turn

print("Final Score is: ", score)
if (score > 400):
    print("Congratulations, you're a legendary Owner!")
elif(400 > score >= 300):
    print("Congratulations, you're a great owner!")
elif(300 > score >= 200):
    print("Congratulations, you're a good owner.")
else:
    (score < 200)
    print("Nice try, keep practicing on being a good owner.")
