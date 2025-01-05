import random

def play(player_name, opponents, player_lives, starting_player):
    participants = [player_name] + list(opponents.keys())  
    current_number = 1  
    turn = participants.index(starting_player)

    print("-----------------------------------")
    print("삼~육구 삼육구! 삼~육구 삼육구!")
    print("\n룰 설명: 숫자에 3, 6, 9가 포함되면 그 개수만큼 '짝'을 입력해주세요.")
    print("예를들면, 1 -> 2 -> 짝 // 33의 경우 '짝짝' 입력")
    print("-----------------------------------")

    while True:
        current_player = participants[turn % len(participants)]  

        clap_count = str(current_number).count("3") + str(current_number).count("6") + str(current_number).count("9")
        correct_answer = "짝" * clap_count if clap_count > 0 else str(current_number)

        if current_player == player_name:
            try:
                player_input = input(f"{current_player}: ").strip()

                if player_input != correct_answer:
                    print(f"{current_player}: {player_input} (오답!)")
                    player_lives[current_player] -= 1  
                    print(f"\n누가 술을 마셔~ {current_player}(이)가 술을 마셔~ 원~~샷!!")
                    print("-----------------------------------")
                    print(f"남은 주량: {player_lives}")

                    print("\n-----------------------------------")
                    print("게임 선택 화면으로 돌아갑니다.")
                    return  

            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
        else:
            if random.random() < 0.7:
                player_input = correct_answer
            else:
                if correct_answer.isdigit():
                    player_input = "짝"
                else:
                    player_input = str(current_number)
            print(f"{current_player}: {player_input}")

            if player_input != correct_answer:
                player_lives[current_player] -= 1  
                print(f"\n누가 술을 마셔~ {current_player}(이)가 술을 마셔~ 원~~샷!!")
                print("-----------------------------------")
                print(f"남은 주량: {player_lives}")

                print("\n-----------------------------------")
                print("게임 선택 화면으로 돌아갑니다.")
                return  

        current_number += 1
        turn += 1