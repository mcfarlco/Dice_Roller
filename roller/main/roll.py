import random


def r_num(max):
    random.seed()
    result = random.randint(1, max)
    return result

def roll_dice(arr, modifiers):
    if len(arr) == 1:
        for die in arr:
            if die == "d4":
                arr = [0, 0, 1, 0, 0, 0, 0, 0, 0]

            elif die == "d6":
                arr = [0, 0, 0, 1, 0, 0, 0, 0, 0]

            elif die == "d8":
                arr = [0, 0, 0, 0, 1, 0, 0, 0, 0]

            elif die == "d10":
                arr = [0, 0, 0, 0, 0, 1, 0, 0, 0]

            elif die == "d12":
                arr = [0, 0, 0, 0, 0, 0, 1, 0, 0]

            elif die == "d20":
                arr = [0, 0, 0, 0, 0, 0, 0, 1, 0]

            elif die == "d100":
                arr = [0, 0, 0, 0, 0, 0, 0, 0, 1]

    # Modifiers [advantage, disadvantage, explode, cheater]
    

    rolls = [[], [], [], [], [], [], [], [], []]
    high_num = [2, 3, 4, 6, 8, 10, 12, 20, 100]
    sum_val = 0
    n_die = sum(arr)
    for i, die in enumerate(arr):
        if int(die) > 0:
            for j in range(int(die)):
                if modifiers[3]:
                    val = high_num[i]
                    rolls[i].append(val)
                    sum_val += val
                    continue

                elif modifiers[0] and modifiers[1]:
                    val = r_num(high_num[i])

                elif modifiers[0]:
                    val_1 = r_num(high_num[i])
                    val_2 = r_num(high_num[i])

                    if(val_1 < val_2):
                        val = val_2
                    
                    else:
                        val = val_1

                elif modifiers[1]:
                    val_1 = r_num(high_num[i])
                    val_2 = r_num(high_num[i])

                    if(val_1 > val_2):
                        val = val_2

                    else:
                        val = val_1
                
                else:
                    val = r_num(high_num[i])
                
                rolls[i].append(val)
                sum_val += val

                if modifiers[2]:
                    while(val == high_num[i]):
                        if modifiers[0] and modifiers[1]:
                            val = r_num(high_num[i])

                        elif modifiers[0]:
                            val_1 = r_num(high_num[i])
                            val_2 = r_num(high_num[i])

                            if(val_1 < val_2):
                                val = val_2

                            else:
                                val = val_1

                        elif modifiers[1]:
                            val_1 = r_num(high_num[i])
                            val_2 = r_num(high_num[i])

                            if(val_1 > val_2):
                                val = val_2

                            else:
                                val = val_1

                        else:
                            val = r_num(high_num[i])
                        
                        rolls[i].append(val)
                        sum_val += val

                        

    return arr, rolls, n_die, sum_val
