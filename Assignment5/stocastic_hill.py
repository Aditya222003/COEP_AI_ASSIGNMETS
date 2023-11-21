import numpy as np

def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape

    # left neighbour
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))

    # right neighbour
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))

    # top neighbour
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))

    # bottom neighbour
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))

    # top left
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))

    # bottom left
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))

    # top right
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))

    # bottom right
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))

    return neighbours

# Stochastic hill climb
def stochastic_hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    
    # Probability distribution for choosing a neighbor
    probabilities = [landscape[neighbour[0]][neighbour[1]] for neighbour in neighbours]
    probabilities = np.array(probabilities) / sum(probabilities)
    
    # Randomly choose a neighbor based on probabilities
    next_state = tuple(neighbours[np.random.choice(len(neighbours), p=probabilities)])
    
    return next_state

def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start_state = (3, 6)  # matrix index coordinates
    current_state = start_state
    count = 1
    while True:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ", landscape[current_state[0]][current_state[1]])
        count += 1
        next_state = stochastic_hill_climb(current_state, landscape)
        if landscape[next_state[0]][next_state[1]] <= landscape[current_state[0]][current_state[1]]:
            print("\nOptimization objective reached.")
            print("Final state coordinates: ", current_state)
            print("Final state value: ", landscape[current_state[0]][current_state[1]])
            break
        else:
            current_state = next_state

__main__()
