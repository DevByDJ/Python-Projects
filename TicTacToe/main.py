import random
first_Row = "   1   |    2    |   3   "
second_Row = "   4   |    5    |   6   "
third_Row = "   7   |    8    |   9   "
divider = "-------------------------"
print("Welcome to Tic Tac Toe!")
print("========================")
print("")
print(first_Row)
print(divider)
print(second_Row)
print(divider)
print(third_Row)
print("\nChoose 3 connecting tiles to win")

game_over = 0
player_has_decided = []
cpu_has_decided = []
available_tile = []

winning_combo_1 = ["1", "2", "3"]
winning_combo_2 = [1, 4, 7]
winning_combo_3 = [1, 5, 9]
winning_combo_4 = [2, 5, 8]
winning_combo_5 = [3, 5, 7]
winning_combo_6 = [3, 6, 9]
winning_combo_7 = [4, 5, 6]
winning_combo_8 = [7, 8, 9]

winning_combo_list = [winning_combo_1, winning_combo_2, winning_combo_3, winning_combo_4, winning_combo_5,
                      winning_combo_6, winning_combo_7, winning_combo_8]


while game_over == 0:
    cpu_Decision = 0
    player_Decision = 0
    def search(list, decision):
        for i in range(len(list)):
            if list[i] == decision:
                return True
            return False
    player_Decision = input("\nChoose a tile: ")
    decision = str(player_Decision)

    while decision in available_tile:
        if decision in available_tile:
            print("This is not an available move, Please Try Again")
            player_Decision = input("\nChoose a tile: ")
            decision = str(player_Decision)
            print(available_tile)

    print("Decision not found")
    available_tile.append(player_Decision)
    if int(player_Decision) < 10:
        if int(player_Decision) == 1:
            replaced_first_row = first_Row.replace("1", "X")
            first_Row = replaced_first_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 2:
            replaced_first_row = first_Row.replace("2", "X")
            first_Row = replaced_first_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 3:
            replaced_first_row = first_Row.replace("3", "X")
            first_Row = replaced_first_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 4:
            replaced_second_row = second_Row.replace("4", "X")
            second_Row = replaced_second_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 5:
            replaced_second_row = second_Row.replace("5", "X")
            second_Row = replaced_second_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 6:
            replaced_second_row = second_Row.replace("6", "X")
            second_Row = replaced_second_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 7:
            replaced_third_row = third_Row.replace("7", "X")
            third_Row = replaced_third_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 8:
            replaced_third_row = third_Row.replace("8", "X")
            third_Row = replaced_third_row
            player_has_decided.append(player_Decision)
        if int(player_Decision) == 9:
            replaced_third_row = third_Row.replace("9", "X")
            third_Row = replaced_third_row
            player_has_decided.append(player_Decision)  # Creates a list that stores the previous player decisions

    while decision in available_tile:
        number_of_elements = len(player_has_decided)
        if number_of_elements > 1:
            print(winning_combo_1)
            print(player_has_decided)
            res = [ele for ele in winning_combo_1]
            for a in winning_combo_1:
                if a in player_has_decided:
                    res.remove(a)
            cpu_Decision = res
            decision = cpu_Decision

        else:
            random_num = random.randint(0, 7)
            winning_combo_choice = winning_combo_list[random_num]
            winning_element = random.choice(winning_combo_choice)
            cpu_Decision = winning_element
            decision = str(cpu_Decision)



    available_tile.append(str(cpu_Decision))
    print("cpu decision " + str(cpu_Decision))

    for decisions in cpu_Decision:
        if decisions == 1:
            replaced_first_row = first_Row.replace("1", "O")
            print("\n" + replaced_first_row)
            print(divider)
            print(second_Row)
            print(divider)
            print(third_Row)
            first_Row = replaced_first_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 2:
            replaced_first_row = first_Row.replace("2", "O")
            print("\n" + replaced_first_row)
            print(divider)
            print(second_Row)
            print(divider)
            print(third_Row)
            first_Row = replaced_first_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 3:
            replaced_first_row = first_Row.replace("3", "O")
            print("\n" + replaced_first_row)
            print(divider)
            print(second_Row)
            print(divider)
            print(third_Row)
            first_Row = replaced_first_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 4:
            replaced_second_row = second_Row.replace("4", "O")
            print(first_Row)
            print(divider)
            print("\n" + replaced_second_row)
            print(divider)
            print(third_Row)
            second_Row = replaced_second_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 5:
            replaced_second_row = second_Row.replace("5", "O")
            print(first_Row)
            print(divider)
            print("\n" + replaced_second_row)
            print(divider)
            print(third_Row)
            second_Row = replaced_second_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 6:
            replaced_second_row = second_Row.replace("6", "O")
            print(first_Row)
            print(divider)
            print("\n" + replaced_second_row)
            print(divider)
            print(third_Row)
            second_Row = replaced_second_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 7:
            replaced_third_row = third_Row.replace("7", "O")
            print(first_Row)
            print(divider)
            print(second_Row)
            print(divider)
            print("\n" + replaced_third_row)
            third_Row = replaced_third_row
            cpu_has_decided.append(cpu_Decision)
        if decisions == 8:
            replaced_third_row = third_Row.replace("8", "O")
            print(first_Row)
            print(divider)
            print(second_Row)
            print(divider)
            print("\n" + replaced_third_row)
            third_Row = replaced_third_row
            cpu_has_decided.append(int(cpu_Decision))
        if decisions == 9:
            replaced_third_row = third_Row.replace("9", "O")
            print(first_Row)
            print(divider)
            print(second_Row)
            print(divider)
            print("\n" + replaced_third_row)
            third_Row = replaced_third_row
            cpu_has_decided.append(int(cpu_Decision))

    print("\nPlayer Choices: " + str(player_has_decided))
    print("Cpu Choices: "+str(cpu_has_decided))

    check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_1))
    if check is True:
        game_over = 1
    else:
        check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_2))
        if check is True:
            game_over = 1
        else:
            check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_3))
            if check is True:
                game_over = 1
            else:
                check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_4))
                if check is True:
                    game_over = 1
                else:
                    check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_5))
                    if check is True:
                        game_over = 1
                    else:
                        check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_6))
                        if check is True:
                            game_over = 1
                        else:
                            check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_7))
                            if check is True:
                                game_over = 1
                            else:
                                check = all(numbers in str(player_has_decided) for numbers in str(winning_combo_8))
                                if check is True:
                                    game_over = 1

    check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_1))
    if check is True:
        game_over = 1
    else:
        check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_2))
        if check is True:
            game_over = 1
        else:
            check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_3))
            if check is True:
                game_over = 1
            else:
                check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_4))
                if check is True:
                    game_over = 1
                else:
                    check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_5))
                    if check is True:
                        game_over = 1
                    else:
                        check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_6))
                        if check is True:
                            game_over = 1
                        else:
                            check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_7))
                            if check is True:
                                game_over = 1
                            else:
                                check = all(numbers in str(cpu_has_decided) for numbers in str(winning_combo_8))
                                if check is True:
                                    game_over = 1











