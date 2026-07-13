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