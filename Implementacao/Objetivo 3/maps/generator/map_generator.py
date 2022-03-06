from lib.plan.probmod.PlanState import PlanState
from lib.world.real_world import RealWorld


def generate_map(map):
    print("> Generating map...")
    f = open("maps/" + str(map), "r")
    words = f.read().splitlines()

    map_width = len(words[0])
    map_height = len(words)

    print("Dimensions: (" + str(map_width) + ", " + str(map_height) + ")")

    initial_state = None
    goal = None
    blocks = []

    y = 0
    for line in words:
        x = 0
        for c in line:
            if c == '>':
                initial_state = PlanState(y, x)
            elif c == 'A':
                goal = PlanState(y, x)
            elif c == 'O':
                blocks.append(PlanState(y, x))
            x += 1
        y += 1

    print("Initial State:", initial_state)
    print("Objective:", goal)
    print("Blocks:", blocks)
    print("> Map Generated!")

    return RealWorld(map_width, map_height, initial_state, goal, blocks)
