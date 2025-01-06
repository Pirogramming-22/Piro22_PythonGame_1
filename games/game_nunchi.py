import random
import time
from threading import Timer, Lock

lock = Lock()

def play(player_name, opponents_with_limits, player_lives, first_game=False):
    players = [player_name] + list(opponents_with_limits.keys())  
    player_timers = {player: round(random.uniform(0.1, 5.0), 1) for player in opponents_with_limits.keys()} 
    current_number = 1  

    while True:
        print(f"\n💕 {player_name}님, 셋 세고 눈치게임을 시작합니다!💕\n")
        print("하나!")
        time.sleep(1)
        print("둘!")
        time.sleep(1)
        print("셋!")
        time.sleep(1)
        print("\n🎲 눈치게임 시작! 🎲\n")

        spoken_numbers = {}  

        # AI 플레이어가 발언할 타이머 설정
        for player, timer in player_timers.items():
            Timer(timer, computer_speak, args=(player, current_number, spoken_numbers)).start()

        # 사용자 입력 처리
        start_time = time.time()
        user_spoken = False

        while not user_spoken and time.time() - start_time < 5.0:
            try:
                user_input = int(input(f"{player_name}님, 숫자를 입력하세요!\n"))
                with lock:
                    spoken_numbers[time.time()] = (player_name, user_input)
                print(f"{player_name}: {user_input}!!!!!!!!!")
                user_spoken = True
            except ValueError:
                print("⚠️ 숫자를 입력해주세요!⚠️")

        # 5초 대기
        time.sleep(5)

        # 결과 처리
        if process_results(spoken_numbers, player_lives, current_number):  
            # 목숨이 깎였으면 현재 상태 출력 후 종료
            print("\n-----------------------------------")
            print("현재 목숨 상태:")
            for player, lives in player_lives.items():
                print(f" - {player}: {lives}잔 남음🥴")
            print("\n-----------------------------------")
            print("게임 선택 화면으로 돌아갑니다.\n")
            return  

        current_number += 1

        print("\n현재 상황:")
        for player, lives in player_lives.items():
            print(f" - {player}: {lives}잔 남음🥴")
        time.sleep(1)

def computer_speak(player, current_number, spoken_numbers):
    with lock:
        max_number = max((num for _, num in spoken_numbers.values()), default=0)
        next_number = max(current_number, max_number + 1)
        spoken_numbers[time.time()] = (player, next_number)
    print(f"{player}: {next_number}!!!!!!!!!")

def process_results(spoken_numbers, player_lives, current_number):
    occurrences = {}
    for _, (player, number) in spoken_numbers.items():
        if number not in occurrences:
            occurrences[number] = []
        occurrences[number].append(player)

    for number, players in occurrences.items():
        if len(players) > 1: 
            print(f"✅ 숫자 {number}를 동시 발언! {' '.join(players)} 모두 1잔 추가!✅")
            for player in players:
                player_lives[player] -= 1
                return True  # 목숨이 깎였으므로 게임 종료

    # 마지막으로 숫자를 외친 플레이어를 가져옴
    if spoken_numbers:
        last_spoken_time = max(spoken_numbers.keys())  # 가장 최근 시간
        last_spoken_player, last_number = spoken_numbers[last_spoken_time]  # 해당 시간의 플레이어와 숫자
        print(f"✅ 마지막으로 숫자를 외친 {last_spoken_player}님이 1잔 추가!✅")
        player_lives[last_spoken_player] -= 1
        return True  # 목숨이 깎였으므로 게임 종료

    return False  # 목숨이 깎이지 않음