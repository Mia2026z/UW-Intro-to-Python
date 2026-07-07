def build_reinforced_wall():
     for position in range(1, 21):
          if position % 4 == 0:
               block_type = "COBBLESTOME"
          else:
               block_type = "PLANK"





def night_patrol(time):
    while(time>0):
        energy=100
        while(energy>=30):
                print("Patrolling")
                energy-=12
                print(energy)
        if(energy<30):
            print("Warning: Low power!")
            break
        if(energy==0):
            print("Shutdown...")
            break
    time-=1
night_patrol(10)
