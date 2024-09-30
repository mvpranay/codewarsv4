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

    
def start(team):

    pirates = team.__pirate_list
    quad_x = pirates[0].getPosition()[0] // 20
    quad_y = pirates[1].getPosition()[1] // 20
    if quad_x == 0 and quad_y == 0:
        quad = 'tl'
    elif quad_x == 1 and quad_y == 0:
        quad = 'tr'
    elif quad_x == 0 and quad_y == 1:
        quad = 'bl'
    else:
        quad = 'br'

    if quad == 'tl':
        n = 1
        for pirate in pirates:
            if n > 5:
                moveTo()
            else:
                moveTo(2 * n - 1, 0, Pirate)






def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
    if (
        (up == "island1" and s[0] != "myCaptured" and s[0] != "myCapturing")
        or (up == "island2" and s[1] != "myCaptured" and s[0] != "myCapturing")
        or (up == "island3" and s[2] != "myCaptured" and s[0] != "myCapturing")
    ):

        

def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")