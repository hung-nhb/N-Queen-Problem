import math
import random

TEMPERATURE = 100
SCH = 0.999
MAXIMUM_ITERATION = 1000000


def calculate_conflict(board_state):
    conflict = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(board_state[i] - board_state[j]) == j - i:
                conflict += 1
    return conflict


def simulated_annealing():
    board_state = [i for i in range(N)]
    random.shuffle(board_state)

    temperature = TEMPERATURE

    for i in range(MAXIMUM_ITERATION):
        new_board_state = board_state[:]
        pos1 = random.randint(0, N - 1)
        pos2 = random.randint(0, N - 1)
        new_board_state[pos1], new_board_state[pos2] = new_board_state[pos2], new_board_state[pos1]
        dw = calculate_conflict(new_board_state) - calculate_conflict(board_state)

        if dw < 0 or random.random() < math.exp(-dw / temperature):
            board_state = new_board_state
            print(f'Turn {i}: {calculate_conflict(board_state)} - Temperature: {temperature}')

        if calculate_conflict(board_state) == 0:
            print('Solved: ', board_state)
            break

        if temperature > 0.1:
            temperature *= SCH
        else:
            temperature = 0.1
    else:
        print(f'Can not solve with {MAXIMUM_ITERATION} iterations')


if __name__ == "__main__":
    N = int(input('Number of queens: '))
    simulated_annealing()
