code1="100"
code2="50"
score=int(code1)
score2=int(code2)
total_score=int(score+score2)
ending_score=(total_score*2)
print("Your final code is",ending_score)
a=40
b="5"
c=a+int(b)
print("Answer:",c)
print("Hello!")
user_name=input("Please verify your name: ")
user_input=input("Please type in your ID: ")
user_password=input("Please type in your password: ")
print("Is this you?"+user_name+user_input+user_password+"")
print("Verification Successful, Welcome "+user_name+"!")


print("It was a hot summer day and all of the neighboorhood children were burning in the sunlight.")
print("Suddenly, they all heard the sound any kid would recognize;it was the ice cream truck.")
print("\"Hooray!\" they all shouted as the truck pulled up next to the apartments.")
print("Each parent got their kid an ice cream and everyone was happy...")
print("But, Lucy accidently dropped her ice cream and started crying but the truck already pulled away.")
print("Lucy's mom didn't know what to do and could only look around, desperate to find something to cheer her up.")
print("Just as she finally ran out of ideas, each kid chipped in with some candy from their candy stash!")
print("Everyone got the ice cream they wanted, and Lucy got candy even though she dropped her ice cream.")
print("Everyone lived happily ever after.THE END")
print("('~')(^_^)(*-*)(-_-)(^,^)(*v*)(>o<)")

level=12
has_gear=True
health=70
has_armor=False
has_magic_ring=True
if level < 10:
    print("Level up before entering this area.")
elif (not has_gear) or (has_armor):
    print("You need a weapon or armor to fight!")
elif health < 50:
    print("Heal up before the fight!")
elif health == 50:
    print("You're ready for battle!!")
else:
    (has_magic_ring)
    print("The ring grants you access!")


user_name=input("Please enter your name: ")
user_id=input("Please enter your ID: ")
user_password=input("Please enter your password: ")
print(f"""This is your info:
      Name: {user_name}
      ID: {user_id}
      Password: {user_password}""")
user_choice=input("Is this information right?")
print(f"VERIFICATION SUCCESSFUL, WELCOME {user_name}!")

user_name=input("Enter your full name: ")
user_bday=input("Enter your DOB: ")
user_school=input("Enter your school: ")
user_number=input("Enter you favorite number: ")
print(f"""Here is what I gathered:"
      Name: {user_name}
      DOB: {user_bday}
      School: {user_school}
      Number: {user_number}""")
user_choice=input("Is this your information?")
print("Thank you for your free information! :P ")
      
running = True

import pygame

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
