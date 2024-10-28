

def cub_1 (a,b):
    c = (a - 4) * " "
    for i in range (0, a):
        for j in range (0, a):
            if i == 0 or i == a-1 or j == 0 or j == 4:
                print(f"{b}",end="  ")
            else:
                print(f"{c}",end="  ")
        print("")

def cub_2(a,b):
    for i in range(a):
        for j in range(a):
            print(f"{b}", end="  ")
        print("")

