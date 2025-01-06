import random
import time
from threading import Timer, Lock

lock = Lock()

def play(player_name, opponents_with_limits, player_lives, drink_count):
    players = [player_name] + list(opponents_with_limits.keys())  
    player_timers = {player: round(random.uniform(0.1, 5.0), 1) for player in opponents_with_limits.keys()} 
    current_number = 1  

    while not any(drink_count[player] > 0 for player in players):
        print(f"\n💕 {player_name}님, 셋 세고 눈치게임을 시작합니다!💕\n")
        print("하나!")
        time.sleep(1)
        print("둘!")
        time.sleep(1)
        print("셋!")
        time.sleep(1)
        print("\n🎲 눈치게임 시작! 🎲\n")

        spoken_numbers = {}  

        for player, timer in player_timers.items():
            Timer(timer, computer_speak, args=(player, current_number, spoken_numbers)).start()

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

        time.sleep(5)  

        process_results(spoken_numbers, drink_count, player_lives, current_number)  
        current_number = 1  


    print("\n❗ 눈치게임 종료! ❗")

def computer_speak(player, current_number, spoken_numbers):
    with lock:
        max_number = max((num for _, num in spoken_numbers.values()), default=0)
        next_number = max(current_number, max_number + 1)
        spoken_numbers[time.time()] = (player, next_number)
    print(f"{player}: {next_number}!!!!!!!!!")

def get_last_spoken_player(spoken_numbers):
    if spoken_numbers:
        last_spoken_time = max(spoken_numbers.keys())
        last_spoken_player = spoken_numbers[last_spoken_time][0]
        return last_spoken_player
    return None

def process_results(spoken_numbers, drink_count, player_lives, current_number):
    occurrences = {}
    for _, (player, number) in spoken_numbers.items():
        if number not in occurrences:
            occurrences[number] = []
        occurrences[number].append(player)

    for number, players in occurrences.items():
        if len(players) > 1: 
            print(f"✅ 숫자 {number}를 동시 발언! {' '.join(players)} 모두 1잔 추가!✅")
            for player in players:
                drink_count[player] += 1
    time.sleep(1)

    if current_number in occurrences and len(occurrences[current_number]) == 1:
        last_spoken_player = get_last_spoken_player(spoken_numbers)
        if last_spoken_player:
            print(f"✅ 마지막으로 숫자를 외친 {last_spoken_player}님이 1잔 추가!✅")
            drink_count[last_spoken_player] += 1
    time.sleep(1)
