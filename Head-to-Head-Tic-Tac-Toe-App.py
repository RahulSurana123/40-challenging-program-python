def draw_tic_tac_toe(inputs):
    if len(inputs) == 9:
        print("\n\t   Tic Tac Toe")
        print(f"\t {inputs[0]}  ||  {inputs[1]}  ||  {inputs[2]}")
        print("\t~~~~~~~~~~~~~~~~~")
        print(f"\t {inputs[3]}  ||  {inputs[4]}  ||  {inputs[5]}")
        print("\t~~~~~~~~~~~~~~~~~")
        print(f"\t {inputs[6]}  ||  {inputs[7]}  ||  {inputs[8]}\n")
    else:
        print("i think you have error with the inputs")


def row_column_equality_check(a, b, c):
    return a == b and b == c


def winner_decide(inputs):
    if len(inputs) == 9:
        winner = "_"
        for i in range(3):
            if inputs[i] != "_" and row_column_equality_check(inputs[(i * 3)], inputs[(i * 3) + 1], inputs[(i * 3) + 2]):
                winner = inputs[(i * 3) + 1]
        for i in range(3):
            if inputs[i] != "_" and row_column_equality_check(inputs[i], inputs[(i + 3)], inputs[(i + 6)]):
                winner = inputs[i]
        if inputs[i] != "_" and (row_column_equality_check(inputs[0], inputs[4], inputs[8]) or
                                 row_column_equality_check(inputs[2], inputs[4], inputs[6])):
            winner = inputs[4]
        return winner
    else:
        return "_"


print("Welcome to Tic Tac Toe App")
game_on = True

while game_on:

    position_shower = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_inputs = ["_", '_', "_", "_", "_", "_", "_", "_", "_"]
    player_input_tracker = []

    turn = "O"

    while len(player_input_tracker) < 9 and game_on:

        draw_tic_tac_toe(position_shower)
        draw_tic_tac_toe(player_inputs)

        turn = "O" if turn == "X" else "X"
        position = int(input(f"{turn}: Where would you like to put your piece (1-9) : "))

        while position > 9 or position < 1:
            print("invalid move you can put piece between 1 and 9 position")
            position = int(input(f"{turn}: Where would you like to put your piece (1-9) : "))

        while position in player_input_tracker:
            print("piece already present please choose other position")
            position = int(input(f"{turn}: Where would you like to put your piece (1-9) : "))

        if position not in player_input_tracker:
            player_inputs[position - 1] = turn
            player_input_tracker.append(position)
        winner_player = winner_decide(player_inputs)
        # print(winner_player)

        if winner_player == "X" or winner_player == "O":
            draw_tic_tac_toe(player_inputs)
            print(f"Player with {winner_player} pieces Win")
            game_on = False
        elif len(player_input_tracker) == 9 and winner_player == "_":
            draw_tic_tac_toe(player_inputs)
            print("The game has tied")
