import random
from rich import print
from rich.console import Console

console = Console()

first_Row = "   1   |    2    |   3   "                               # Defining the TicTacToe game board..
second_Row = "   4   |    5    |   6   "
third_Row = "   7   |    8    |   9   "
divider = "-------------------------"
console.print("Welcome to Tic Tac Toe!", style="bold underline red")
print("========================")
print("")
print(first_Row)
print(divider)
print(second_Row)
print(divider)
print(third_Row)
print("\nChoose 3 connecting tiles to win")

true = 1
false = 0

game_over = 0                                                       # Game Over variable controls game ON/OFF
player_has_decided = []                                             # List that will contain player decisions
cpu_has_decided = []                                                # List that will contain cpu decisions for comparing
all_cpu_decisions = []                                              # List that will check for CPU combo's
available_tile = []                                                 # List that will contain available play areas

winning_combo_1 = ["1", "2", "3"]                                   # List of all possible winning combinations..
winning_combo_2 = ["1", "4", "7"]
winning_combo_3 = ["1", "5", "9"]
winning_combo_4 = ["2", "5", "8"]
winning_combo_5 = ["3", "5", "7"]
winning_combo_6 = ["3", "6", "9"]
winning_combo_7 = ["4", "5", "6"]
winning_combo_8 = ["7", "8", "9"]

winning_combo_1_blocked = false                               # Establishing that no combinations have been triggered...
winning_combo_2_blocked = false
winning_combo_3_blocked = false
winning_combo_4_blocked = false
winning_combo_5_blocked = false
winning_combo_6_blocked = false
winning_combo_7_blocked = false
winning_combo_8_blocked = false

while game_over == false:                                           # While the game is running...
    cpu_Decision = 0
    player_Decision = 0

    def search(list, decision):                                     # Defining the search function to verify
        for i in range(len(list)):
            if list[i] == decision:
                return True
            return False

    player_Decision = input("\nChoose a tile: ")                    # Assign player choice input to a variable..
    decision = str(player_Decision)

    while decision in available_tile:                               # While the player choice is available on board.
        player_Decision = 0
        cpu_Decision = 0
        if decision in available_tile:                             # If the player chooses a space that's not available.
            print("This is not an available move, Please Try Again")
            player_Decision = input("\nChoose a tile: ")
            decision = str(player_Decision)

    available_tile.append(player_Decision)                          # Removes the player decision off the game board.
    if int(player_Decision) < 10 and game_over == false:                                   # Handles Board Change based off player decision
        if int(player_Decision) == 1:
            replaced_first_row = first_Row.replace("1", "[green]X[/green]")        # Replaces the number on the board with an X
            first_Row = replaced_first_row                          # Saves the change.
            player_has_decided.append(player_Decision)              # Saves all the player choices.
        if int(player_Decision) == 2:
            replaced_first_row = first_Row.replace("2", "[green]X[/green]")
            first_Row = replaced_first_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 3:
            replaced_first_row = first_Row.replace("3", "[green]X[/green]")
            first_Row = replaced_first_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 4:
            replaced_second_row = second_Row.replace("4", "[green]X[/green]")
            second_Row = replaced_second_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 5:
            replaced_second_row = second_Row.replace("5", "[green]X[/green]")
            second_Row = replaced_second_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 6:
            replaced_second_row = second_Row.replace("6", "[green]X[/green]")
            second_Row = replaced_second_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 7:
            replaced_third_row = third_Row.replace("7", "[green]X[/green]")
            third_Row = replaced_third_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 8:
            replaced_third_row = third_Row.replace("8", "[green]X[/green]")
            third_Row = replaced_third_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 9:
            replaced_third_row = third_Row.replace("9", "[green]X[/green]")
            third_Row = replaced_third_row
            player_has_decided.append(player_Decision)

    if game_over == false:
        check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_1))           # Checks if any player decisions match the winning combo...
        if check is True:
            print(first_Row)
            print(divider)
            print(second_Row)
            print(divider)
            print(third_Row)
            game_over = 1
        else:
            check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_2))
            if check is True:
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                game_over = 1
            else:
                check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_3))
                if check is True:
                    print(first_Row)
                    print(divider)
                    print(second_Row)
                    print(divider)
                    print(third_Row)
                    game_over = 1
                else:
                    check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_4))
                    if check is True:
                        print(first_Row)
                        print(divider)
                        print(second_Row)
                        print(divider)
                        print(third_Row)
                        game_over = 1
                    else:
                        check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_5))
                        if check is True:
                            print(first_Row)
                            print(divider)
                            print(second_Row)
                            print(divider)
                            print(third_Row)
                            game_over = 1
                        else:
                            check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_6))
                            if check is True:
                                print(first_Row)
                                print(divider)
                                print(second_Row)
                                print(divider)
                                print(third_Row)
                                game_over = 1
                            else:
                                check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_7))
                                if check is True:
                                    print(first_Row)
                                    print(divider)
                                    print(second_Row)
                                    print(divider)
                                    print(third_Row)
                                    game_over = 1
                                else:
                                    check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_8))
                                    if check is True:
                                        print(first_Row)
                                        print(divider)
                                        print(second_Row)
                                        print(divider)
                                        print(third_Row)
                                        game_over = 1

    while decision in available_tile:                            # Controls the CPU logic when choosing a position.
        number_of_elements = len(player_has_decided)             # Verifies the number of choices the players made.
        if number_of_elements > 1:                               # After 2 player decisions...
            check_player_combo = false
            player_has_decided_as_set = set(player_has_decided)  # Converts player choices to a set..
            while check_player_combo == 0:                       # Logic to check winning combo & block player moves.
                checking_combo = player_has_decided_as_set.intersection(winning_combo_1)    # Compares matching elements
                number_of_winning_elements = len(checking_combo)            # stores how many matching elements.
                if number_of_winning_elements >= 2 and winning_combo_1_blocked == false:
                    res = [ele for ele in winning_combo_1]
                    for a in winning_combo_1:
                        if a in player_has_decided:
                            res.remove(a)                        # Removes the matching winning combo for players choices to create final choice.
                    cpu_Decision = res                           # Result stored.
                    decision = cpu_Decision
                    winning_combo_1_blocked = true;              # Prevents system from checking this combo again.
                    check_player_combo = 1                       # Breaks loop
                else:
                    checking_combo = player_has_decided_as_set.intersection(winning_combo_2)
                    number_of_winning_elements = len(checking_combo)
                    if number_of_winning_elements >= 2 and winning_combo_2_blocked == false:
                        res = [ele for ele in winning_combo_2]
                        for a in winning_combo_2:
                            if a in player_has_decided:
                                res.remove(a)
                        cpu_Decision = res
                        decision = cpu_Decision
                        winning_combo_2_blocked = true;
                        check_player_combo = 1
                    else:
                        checking_combo = player_has_decided_as_set.intersection(winning_combo_3)
                        number_of_winning_elements = len(checking_combo)
                        if number_of_winning_elements >= 2 and winning_combo_3_blocked == false:
                            res = [ele for ele in winning_combo_3]
                            for a in winning_combo_3:
                                if a in player_has_decided:
                                    res.remove(a)
                            cpu_Decision = res
                            decision = cpu_Decision
                            winning_combo_3_blocked = true;
                            check_player_combo = 1
                        else:
                            checking_combo = player_has_decided_as_set.intersection(winning_combo_4)
                            number_of_winning_elements = len(checking_combo)
                            if number_of_winning_elements >= 2 and winning_combo_4_blocked == false:
                                res = [ele for ele in winning_combo_4]
                                for a in winning_combo_4:
                                    if a in player_has_decided:
                                        res.remove(a)
                                cpu_Decision = res
                                decision = cpu_Decision
                                winning_combo_4_blocked = true;
                                check_player_combo = 1
                            else:
                                checking_combo = player_has_decided_as_set.intersection(winning_combo_5)
                                number_of_winning_elements = len(checking_combo)
                                if number_of_winning_elements >= 2 and winning_combo_5_blocked == false:
                                    res = [ele for ele in winning_combo_5]
                                    for a in winning_combo_5:
                                        if a in player_has_decided:
                                            res.remove(a)
                                    cpu_Decision = res
                                    decision = cpu_Decision
                                    winning_combo_5_blocked = true;
                                    check_player_combo = 1
                                else:
                                    checking_combo = player_has_decided_as_set.intersection(winning_combo_6)
                                    number_of_winning_elements = len(checking_combo)
                                    if number_of_winning_elements >= 2 and winning_combo_6_blocked == false:
                                        res = [ele for ele in winning_combo_6]
                                        for a in winning_combo_6:
                                            if a in player_has_decided:
                                                res.remove(a)
                                        cpu_Decision = res
                                        decision = cpu_Decision
                                        winning_combo_6_blocked = true;
                                        check_player_combo = 1
                                    else:
                                        checking_combo = player_has_decided_as_set.intersection(winning_combo_7)
                                        number_of_winning_elements = len(checking_combo)
                                        if number_of_winning_elements >= 2 and winning_combo_7_blocked == false:
                                            res = [ele for ele in winning_combo_7]
                                            for a in winning_combo_7:
                                                if a in player_has_decided:
                                                    res.remove(a)
                                            cpu_Decision = res
                                            decision = cpu_Decision
                                            winning_combo_7_blocked = true;
                                            check_player_combo = 1
                                        else:
                                            checking_combo = player_has_decided_as_set.intersection(winning_combo_8)
                                            number_of_winning_elements = len(checking_combo)
                                            if number_of_winning_elements >= 2 and winning_combo_8_blocked == false:
                                                res = [ele for ele in winning_combo_8]
                                                for a in winning_combo_8:
                                                    if a in player_has_decided:
                                                        res.remove(a)
                                                cpu_Decision = res
                                                decision = cpu_Decision
                                                winning_combo_8_blocked = true;
                                                check_player_combo = 1

        else:                                                       # If player only made one decision, randomize pick.
            random_num = random.randint(0, 9)
            cpu_Decision = random_num
            decision = str(cpu_Decision)

    available_tile.append(str(cpu_Decision))                        # Updates board logic with CPU Decision.

    if number_of_elements > 1 and game_over == false:                                      # If player has already gone twice.
        if int(cpu_Decision[0]) < 10:
            if int(cpu_Decision[0]) == 1:
                replaced_first_row = first_Row.replace("1", "[red]O[/red]")    # Replaces the number on the board with an X
                first_Row = replaced_first_row                      # Saves the change.
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))        # Saves all the CPU choices.
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 2:
                replaced_first_row = first_Row.replace("2", "[red]O[/red]")
                first_Row = replaced_first_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 3:
                replaced_first_row = first_Row.replace("3", "[red]O[/red]")
                first_Row = replaced_first_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 4:
                replaced_second_row = second_Row.replace("4", "[red]O[/red]")
                second_Row = replaced_second_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 5:
                replaced_second_row = second_Row.replace("5", "[red]O[/red]")
                second_Row = replaced_second_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 6:
                replaced_second_row = second_Row.replace("6", "[red]O[/red]")
                second_Row = replaced_second_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 7:
                replaced_third_row = third_Row.replace("7", "[red]O[/red]")
                third_Row = replaced_third_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 8:
                replaced_third_row = third_Row.replace("8", "[red]O[/red]")
                third_Row = replaced_third_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))
            if int(cpu_Decision[0]) == 9:
                replaced_third_row = third_Row.replace("9", "[red]O[/red]")
                third_Row = replaced_third_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision[0]))
                all_cpu_decisions.append(int(cpu_Decision[0]))

    if number_of_elements == 1 and game_over == false:
        if int(cpu_Decision) < 10:
            if int(cpu_Decision) == 1:
                replaced_first_row = first_Row.replace("1", "[red]O[/red]")
                first_Row = replaced_first_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 2:
                replaced_first_row = first_Row.replace("2", "[red]O[/red]")
                first_Row = replaced_first_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 3:
                replaced_first_row = first_Row.replace("3", "[red]O[/red]")
                first_Row = replaced_first_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 4:
                replaced_second_row = second_Row.replace("4", "[red]O[/red]")
                second_Row = replaced_second_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 5:
                replaced_second_row = second_Row.replace("5", "[red]O[/red]")
                second_Row = replaced_second_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 6:
                replaced_second_row = second_Row.replace("6", "[red]O[/red]")
                second_Row = replaced_second_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 7:
                replaced_third_row = third_Row.replace("7", "[red]O[/red]")
                third_Row = replaced_third_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 8:
                replaced_third_row = third_Row.replace("8", "[red]O[/red]")
                third_Row = replaced_third_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))
            if int(cpu_Decision) == 9:
                replaced_third_row = third_Row.replace("9", "[red]O[/red]")
                third_Row = replaced_third_row
                print(first_Row)
                print(divider)
                print(second_Row)
                print(divider)
                print(third_Row)
                cpu_has_decided.append(int(cpu_Decision))
                all_cpu_decisions.append(int(cpu_Decision))

    if game_over == false:
        check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_1))    # Checks if any CPU decisions match the winning combo...
        if check is True:
            game_over = 1
        else:
            check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_2))
            if check is True:
                game_over = 1
            else:
                check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_3))
                if check is True:
                    game_over = 1
                else:
                    check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_4))
                    if check is True:
                        game_over = 1
                    else:
                        check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_5))
                        if check is True:
                            game_over = 1
                        else:
                            check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_6))
                            if check is True:
                                game_over = 1
                            else:
                                check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_7))
                                if check is True:
                                    game_over = 1
                                else:
                                    check = all(numbers in str(all_cpu_decisions) for numbers in str(winning_combo_8))
                                    if check is True:
                                        game_over = 1

    if game_over == true:
        console.print("\nGAME OVER!", style="bold red")











