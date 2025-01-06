import random
import time
def play(player_name, opponents, player_lives, starting_player):
    print("==========업 앤 다운 게임==========")
    time.sleep(2)

    participants = [player_name] + list(opponents.keys())

    # 스타팅 플레이어 결정
    print(f"\n{starting_player}님이 첫 번째 플레이어로 시작합니다!")
    turn = participants.index(starting_player)

    print("\n1부터 100사이의 랜덤 숫자가 정해졌습니다! 그 숫자를 맞춰보세요!")
    time.sleep(2)

    target_number = random.randint(1, 100)
    guess_range = [1, 100]

    while True:
        current_player = participants[turn % len(participants)]
        print(f"\n=========={current_player}님의 차례입니다!==========")
        time.sleep(2)

        if current_player == player_name:
            while True:
                player_input = input(f"{player_name}님, 숫자를 입력하세요! ({guess_range[0]} ~ {guess_range[1]}): ").strip()
                if not player_input.isdigit():
                    print("⚠️ 올바른 숫자를 입력해주세요!")
                    continue
                guess = int(player_input)
                if guess < guess_range[0] or guess > guess_range[1]:
                    print(f"⚠️ {guess_range[0]}부터 {guess_range[1]} 사이의 숫자를 입력해주세요!")
                    continue
                break
        else:
            guess = random.randint(guess_range[0], guess_range[1])
            print(f"{current_player}님이 {guess}을(를) 선택했습니다!")

        if guess > target_number:
            print("\nDOWN! 더 작은 숫자를 입력하세요!")
            guess_range[1] = guess - 1
        elif guess < target_number:
            print("\nUP! 더 큰 숫자를 입력하세요!")
            guess_range[0] = guess + 1
        else:
            print(f"\n🎉 {current_player}님이 정답을 맞췄습니다! 🎉")
            print(f"정답은 {target_number}이었습니다!")
            print(f"맞춘 사람은 면제, 다른 모든 사람들이 마셔야 합니다! 🍺")

            for participant in participants:
                if participant != current_player:
                    player_lives[participant] -= 1

            print("\n현재 목숨 상태:")
            for player, lives in player_lives.items():
                print(f" - {player}: {lives}잔 남음")
            
            print("\n-----------------------------------")
            print("게임 선택 화면으로 돌아갑니다.\n")
            return
        turn += 1
        time.sleep(1)