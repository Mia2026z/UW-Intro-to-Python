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
