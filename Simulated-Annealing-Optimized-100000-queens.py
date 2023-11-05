import random
import math
import time
import matplotlib.pyplot as plt

def calculate_attack_cost(board, n):
    attacks = 0
    row_mask = [0] * n
    diag_mask = [0] * (2 * n - 1)
    anti_diag_mask = [0] * (2 * n - 1)

    for i in range(n):
        row = board[i]
        diag = i + row
        anti_diag = n - 1 - i + row

        if (row_mask[row] or diag_mask[diag] or anti_diag_mask[anti_diag]):
            attacks += 1

        row_mask[row] = 1
        diag_mask[diag] = 1
        anti_diag_mask[anti_diag] = 1

    return attacks

def simulated_annealing(n, initial_temperature, cooling_rate, list_of_current_costs):
    board = [i for i in range(n)]
    random.shuffle(board)

    current_cost = calculate_attack_cost(board, n)
    list_of_current_costs.append(current_cost)
    temperature = initial_temperature
    iteration = 0

    while current_cost > 0:
        i, j = random.sample(range(n), 2)
        board[i], board[j] = board[j], board[i]

        new_cost = calculate_attack_cost(board, n)
        cost_diff = new_cost - current_cost

        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
            current_cost = new_cost
        else:
            board[j], board[i] = board[i], board[j]

        list_of_current_costs.append(current_cost)
        temperature *= cooling_rate
        iteration += 1

        # print(f"Iteration: {iteration}, current cost: {current_cost}, new cost: {new_cost}")

    return board, iteration

def solve_n_queen(n, initial_temperature, cooling_rate):

    # Tạo list của cost như trục hoành
    y = []

    start_time = time.perf_counter()

    solution, iterations = simulated_annealing(n, initial_temperature, cooling_rate, y)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print(f"Số quân hậu: {n}, Số lần lặp: {iterations}, Thời gian chạy: {execution_time:.5f}s , Solution: {solution}")

    # Tạo list của số lần lặp như trục tung
    x = list(range(iterations + 1))
    #print(x)
    #print(y)
    plt.plot(x, y, label=f"Bài toán {n} con hậu, thời gian chạy: {execution_time:.5f}s")

    plt.xlabel("Số vòng lặp")
    plt.ylabel("Current Cost")
    plt.legend()
    plt.show()

# Đầu vào
n = 500  # Số quân hậu
initial_temperature = 1000.0
cooling_rate = 0.99

solve_n_queen(n, initial_temperature, cooling_rate)