import random
import time

def play(player_name, opponents_with_limits, player_lives, starting_player=None, first_game=False):
    participants = [player_name] + list(opponents_with_limits.keys())

    # 첫 번째 게임 이후 랜덤으로 새로운 첫 번째 플레이어 선택
    if not first_game:
        starting_player = random.choice(participants)

    current_number = 1
    print(f"\n========== {starting_player}님이 이번 369 게임의 첫 번째 플레이어로 시작합니다! ==========")
    time.sleep(2)

    # 현재 플레이어의 차례를 계산
    turn = participants.index(starting_player)

    print("\n-----------------------------------")
    print("삼~육구 삼육구! 삼~육구 삼육구!")
    time.sleep(2)
    print("\n룰 설명: 숫자에 3, 6, 9가 포함되면 그 개수만큼 '짝'을 입력해주세요.")
    print("예를들면, 1 -> 2 -> 짝 // 33의 경우 '짝짝' 입력")
    print("-----------------------------------\n")
    time.sleep(2)

    while True:
        current_player = participants[turn % len(participants)]

        # 정답 계산
        clap_count = str(current_number).count("3") + str(current_number).count("6") + str(current_number).count("9")
        correct_answer = "짝" * clap_count if clap_count > 0 else str(current_number)

        if current_player == player_name:
            # 사용자 입력
            try:
                player_input = input(f"{current_player}: ").strip()

                if player_input != correct_answer:
                    print(f"\n{current_player} >>>>> {player_input} (오답!)")
                    player_lives[current_player] -= 1
                    print(f"\n누가 술을 마셔~ {current_player}(이)가 술을 마셔~ 원~~샷!!")
                    print("-----------------------------------")
                    print(f"남은 주량: {player_lives}")

                    time.sleep(2)
                    print("\n-----------------------------------")
                    print("게임 선택 화면으로 돌아갑니다.\n")
                    return  # 게임 종료 후 메인으로 돌아감

            except ValueError:
                print("\n⚠️ 잘못된 입력입니다. 다시 입력해주세요.\n")
                time.sleep(1)
                continue
        else:
            # AI 플레이어의 입력
            if random.random() < 0.7:
                player_input = correct_answer  # 정답 선택
            else:
                # 일부러 오답 선택
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

                time.sleep(2)
                print("\n-----------------------------------")
                print("게임 선택 화면으로 돌아갑니다.\n")
                return  # 게임 종료 후 메인으로 돌아감

        # 다음 차례와 숫자 진행
        current_number += 1
        turn += 1

        # 턴 간 대기
        time.sleep(1)