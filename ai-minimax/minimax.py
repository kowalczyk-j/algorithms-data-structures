from two_player_games.games.Pick import Pick, PickMove, PickState
from numpy import Infinity
from copy import deepcopy
import matplotlib.pyplot as plt
from itertools import combinations


def heuristic(node):
    score = 0
    for number in node.current_player_numbers:
        if node.get_current_player().char == '2':
            score = score + node.max_number - abs(node.aim_value/4-number)
        else:
            score = score - node.max_number + abs(node.aim_value/4-number)
    possible_moves = [move.number for move in node.get_moves()]

    for number in possible_moves:
        opponent_nums = deepcopy(node.current_player_numbers)
        opponent_nums.append(number)
        player_nums = deepcopy(node.other_player_numbers)
        player_nums.append(number)
        if node._check_if_sums_to_aim_value(opponent_nums):
            score = 200 if node.get_current_player().char == '2' else -200
        if node._check_if_sums_to_aim_value(player_nums):
            score = max(100, score) if node.get_current_player(
            ).char == '2' else min(-100, score)

    if node.get_winner():
        return 300 if node.get_winner().char == '2' else -300
    return score


def create_heuristic_dict():
    hdict = {}
    for c in list(el for el in combinations(range(1, 17), 4) if sum(el) == 34):
        for number in c:
            if number not in hdict.keys():
                hdict[number] = 1
            else:
                hdict[number] += 1
    return hdict


def heuristic2(node, hdict):
    if node.get_winner():
        return 1000 if node.get_winner().char == '2' else -1000
    max_score = sum([hdict[number] for number in node.other_player_numbers])
    return max_score if node.get_current_player().char == '2' else -max_score


def minimax(node, depth=1, alpha=-Infinity, beta=Infinity,
            maximizingPlayer=True):

    if depth == 0 or node.is_finished():
        return heuristic2(node, HDICT)

    if maximizingPlayer:
        value = -Infinity
        for child in node.get_children():
            value = max(minimax(child, depth - 1,
                        alpha, beta, False), value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = Infinity
        for child in node.get_children():
            value = min(minimax(child, depth - 1,
                                alpha, beta, True), value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


def play_game(depth_max, depth_min):
    game = Pick()
    state = game.state
    while not state.is_finished():
        best_score = -Infinity if state.get_current_player().char == '1' else Infinity
        for child in state.get_children():
            if state.get_current_player().char == '1':
                score = minimax(child, depth_max)
                if score > best_score:
                    best_score = score
                    best_move = child
            else:
                score = minimax(child, depth_min)
                if score < best_score:
                    best_score = score
                    best_move = child
        state = best_move
    return state


def choose_winner(state):
    print(state)
    if state.get_winner():
        print(f"Player {state.get_winner().char}. won.")
    else:
        print("Draw.")


def plotter(depths=6):
    moves_values = [len(play_game(i+1, i+1).selected_numbers)
                    for i in range(depths)]
    plt.plot([i+1 for i in range(depths)], moves_values, 'ro')
    plt.xlabel('Głębokość algorytmu')
    plt.ylabel('Liczba ruchów w rozgrywce')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    HDICT = create_heuristic_dict()
    state = play_game(5, 2)
    choose_winner(state)
    # for i in range(6):
    #     choose_winner(play_game(i+1, 1))
    # plotter(6)
