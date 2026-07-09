def build_reinforced_wall():
     for position in range(1, 21):
          if position % 4 == 0:
               block_type = "COBBLESTOME"
          else:
               block_type = "PLANK"



def night_patrol(time): 
    energy=100
    while(time>0):
        while(energy>=30):
            print("Patrolling")
            energy-=12
            print(energy)
            time-=1
        if(energy<30):
            print("Warning: Low power!")
            energy-=12
            time-=1
        if(energy<=0):
            print("Shutdown...")
            break
night_patrol(10)

def happy_birthday(name, age):
    print(f"Happy Birthday, {name}!")
    print(f"You are {age} years old!")
    print("Happpy Birthday to you!")
happy_birthday("America", "250")


def add(x,y):
    z = x + y
    return z
print(add(1,2))

def subtract(x,y):
    z = x - y
    return z
print(subtract(1,2))

def multiply(x,y):
    z = x * y
    return z
print(multiply(1,2))

def divide(x,y):
    z = x / y
    return z
print(divide(1,2))

def full_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
z = full_name("mei mei", "da")
print(z)


f = int(input("Type in a temperature for me to calculate to Celsius: "))
def temperature_cal(f):
    c = (f - 32) * 5 / 9
    return c

print(f"{f} Farenheit is equal to {temperature_cal(f)} Celsius!")
    