from random import randint, choice
import numpy as np

name = 'marupaka'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    

def weighted_choice(_arr, weights):
    x = []
    k = 100
    for i in range(len(_arr)):  
        prob = weights[i]
        n = int(prob * k)  
        for j in range(n):
            x.append(_arr[i])

    return choice(x)


def spread(pirate) :
    sorted_pir = int(pirate.getID()) % 3
    if pirate.getSignal() == '' :
        return 0
    if pirate.getSignal() == 'ul' :
        dir_opn = [[3,2],[3,3,2],[3,2,2]]
        return choice(dir_opn[sorted_pir])
    if pirate.getSignal() == 'ur' :
        dir_opn = [[3,4],[3,3,4],[3,4,4]]
        return choice(dir_opn[sorted_pir]) 
    if pirate.getSignal() == 'dl' :
        dir_opn = [[1,2],[1,1,2],[1,2,2]]
        return choice(dir_opn[sorted_pir])
    if pirate.getSignal() == 'dr' :
        dir_opn = [[1,4],[1,1,4],[1,4,4]]
        return choice(dir_opn[sorted_pir])
    # x, y = pirate.getPosition()
    # prevx,prevy,ud,lr = pirate.getSignal().split(',')
    # quad = pirate.getTeamSignal()[0]
    # print("QUAD", quad)
    # dirs = [1, 2, 3, 4]
    # w = 1000
    # if quad == "1":
    #     weights = [1, w, w, 1]

    # elif quad == "2":
    #     weights = [1, 1, w, w]
        
    # elif quad == "3":
    #     weights = [w, w, 1, 1] 
    # else:
    #     weights = [w, 1, 1, w]
    # weights = np.array(weights, dtype='f')
    # s = np.sum(weights)
    # weights /= s
    
    # return weighted_choice(dirs, weights)

    # choices = [1, 2, 3, 4]

    # if ud != "":
    #     choices.remove(int(ud))
    # if lr != "":
    #     choices.remove(int(lr))
        
    # if prevx == x:
    #     if prevy > y:
    #         choices.remove(1)
    #         return choice(choices)
    #     elif prevy < y:
    #         choices.remove(3)
    #         return choice(choices)

    # elif prevy == y:
    #     if prevx < x:
    #         choices.remove(2)
    #         return choice(choices)
    #     elif prev > y:
    #         choices.remove(4)
    #         return choice(choices)

    # return randint(1, 4)

def create_msg(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]

    dont_go = ["", ""]
    if up == 'wall':
        dont_go[0] = 1
    elif down == 'wall':
        dont_go[0] = 3
    if right == 'wall':
        dont_go[1] = 2
    elif left == 'wall':
        dont_go[1] = 4

    pirate_x, pirate_y = pirate.getPosition()
    msg = f"{pirate_x},{pirate_y},{dont_go[0]},{dont_go[1]}"
    pirate.setSignal(msg)
    return

def ActPirate(pirate):

    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    
    # set signal
    if up == 'wall' and left == 'wall' :
        pirate.setSignal('ul')
    elif up == 'wall' and right == 'wall':
        pirate.setSignal('ur')
    elif down == 'wall' and left == 'wall' :
        pirate.setSignal('dl')
    elif down == 'wall' and right == 'wall':
        pirate.setSignal('dr')

    # print('signal set successfully to ', pirate.getSignal())
    s = pirate.trackPlayers()
    team_s = pirate.getTeamSignal()
    split = team_s.split(',')
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(up[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] != "-1":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x)
            split[island_status_index + 2] = str(y - 1)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)
            pirate.setSignal('')

        
    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(down[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] != "-1":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x)
            split[island_status_index + 2] = str(y + 1)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)
            pirate.setSignal('')


    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(left[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] != "-1":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x - 1)
            split[island_status_index + 2] = str(y)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)
            pirate.setSignal('')

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        island_no = int(right[-1])
        island_status_index = island_no * 3 - 2
        if split[island_status_index] != "-1":
            split[island_status_index] = "-1" 
            split[island_status_index + 1] = str(x + 1)
            split[island_status_index + 2] = str(y)
            team_s = ','.join(split)
            pirate.setTeamSignal(team_s)
            pirate.setSignal('')

    if (right == 'wall' and pirate.getSignal() == 'ul') :
        pirate.setSignal('ur')
    if (right == 'wall' and pirate.getSignal() == 'dl') :
        pirate.setSignal('dr')
    if (left == 'wall' and pirate.getSignal() == 'ur') :
        pirate.setSignal('ul')
    if (left == 'wall' and pirate.getSignal() == 'dr') :
        pirate.setSignal('dl')
    if (up == 'wall' and pirate.getSignal() == 'dl') :
        pirate.setSignal('ul')
    if (up == 'wall' and pirate.getSignal() == 'dr') :
        pirate.setSignal('ur')
    if (down == 'wall' and pirate.getSignal() == 'ul') :
        pirate.setSignal('dl')
    if (down == 'wall' and pirate.getSignal() == 'ur') :
        pirate.setSignal('dr')

    # print("signal is ", pirate.getSignal())
    # if some island is not ours, move part of our forces there
    island1_status = split[1] 
    island2_status = split[4] 
    island3_status = split[7] 

    discover_thresh = 1 # figure optimum
    stall_thresh = 1

    if island1_status == '-1':
        pirate_x, pirate_y = pirate.getPosition()
        x = int(split[2])
        y = int(split[3])
        reqPirates = (abs(pirate_x - x + pirate_y - y) + abs(pirate_y - y - pirate_x + x) < 2 * discover_thresh)
        if reqPirates:
            return moveTo(x, y, pirate)
    elif island1_status == '2':
        if split[2] != "" and split[3] != "":
            pirate_x, pirate_y = pirate.getPosition()
            x = int(split[2])
            y = int(split[3])
            reqPirates = (abs(pirate_x - x + pirate_y - y) + abs(pirate_y - y - pirate_x + x) < 2 * stall_thresh)
            if reqPirates:
                return moveTo(x, y, pirate)

        
    
    if island2_status == '-1':
        pirate_x, pirate_y = pirate.getPosition()
        x = int(split[5])
        y = int(split[6])
        reqPirates = (abs(pirate_x - x + pirate_y - y) + abs(pirate_y - y - pirate_x + x) < 2 * discover_thresh)
        if reqPirates:
            return moveTo(x, y, pirate)
    elif island2_status == '2':
        if split[5] != "" and split[6] != "":
            pirate_x, pirate_y = pirate.getPosition()
            x = int(split[5])
            y = int(split[6])
            reqPirates = (abs(pirate_x - x + pirate_y - y) + abs(pirate_y - y - pirate_x + x) < 2 * stall_thresh)
            if reqPirates:
                return moveTo(x, y, pirate)
        
    if island3_status == '-1':
        pirate_x, pirate_y = pirate.getPosition()
        x = int(split[8])
        y = int(split[9])
        reqPirates = (abs(pirate_x - x + pirate_y - y) + abs(pirate_y - y - pirate_x + x) < 2 * discover_thresh)
        if reqPirates:
            return moveTo(x, y, pirate)
    elif island3_status == '2':
        if split[8] != "" and split[9] != "":
            pirate_x, pirate_y = pirate.getPosition()
            x = int(split[8])
            y = int(split[9])
            reqPirates = (abs(pirate_x - x + pirate_y - y) + abs(pirate_y - y - pirate_x + x) < 2 * stall_thresh)
            if reqPirates:
                return moveTo(x, y, pirate)
        
    # create_msg(pirate)
    a = spread(pirate)
    # print(a)
    return a


def ActTeam(team):
    island_status = team.trackPlayers()

    signal = team.getTeamSignal()
    if signal == "":
        signal = "," * 9

    spawn_x, spawn_y = team.getDeployPoint()
    if spawn_x == 0 and spawn_y == 0:
        quad = 1
    if spawn_x != 0 and spawn_y == 0:
        quad = 2
    if spawn_x == 0 and spawn_y != 0:
        quad = 3
    if spawn_x != 0 and spawn_y != 0:
        quad = 4

    split = signal.split(',')
    split[0] = str(quad)
    # print(island_status)
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if island_status[0] == 'myCaptured':
        split[1] = "1"
    if island_status[1] == 'myCaptured':
        split[4] = '1'
    if island_status[2] == 'myCaptured':
        split[7] = '1'
    if (island_status[3] == 'oppCapturing') or (island_status[3] == 'oppCaptured'):
        split[1] = "2"
    if (island_status[4] == 'oppCapturing') or (island_status[4] == 'oppCaptured'):
        split[4] = "2"
    if (island_status[5] == 'oppCapturing') or (island_status[5] == 'oppCaptured'):
        split[7] = "2"
    
    
    signal = ','.join(split)
    # print(signal)
    team.setTeamSignal(signal)