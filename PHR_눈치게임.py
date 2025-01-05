import random
import time
from threading import Timer, Lock

lock = Lock()  


def start_game():
    print("🎉 혼자하는 Python 술게임: 눈치게임 🎉")
    
    user_name = input("당신의 이름을 입력하세요: ")
    while True:
        try:
            user_capacity_input = int(input(f"""🍺 소주 기준 당신의 주량은?🍺
                                      🍺 1. 소주 반병(2잔)
                                      🍺 2. 소주 반병에서 한 병(4잔)
                                      🍺 3. 소주 한병에서 한병 반(6잔)
                                      🍺 4. 소주 한병 반에서 두병(8잔)
                                      🍺 5. 소주 두병 이상(10잔)                      
                                      {user_name}님의 주량을 입력하세요 (1~5를 선택해주세요): """))
            if user_capacity_input < 1 or user_capacity_input > 5:
                raise ValueError
            capacity_mapping = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
            user_capacity = capacity_mapping[user_capacity_input]
            break
        except ValueError:
            print("⚠️ 1번부터 5번 중에 골라주세요!")
    
    players = ["설아", "승인", "진수", "진혁", "혜린"]
    while True:
        try:
            invited_count = int(input("초대할 인원 수를 입력하세요 (최대 5명): "))
            if invited_count < 1 or invited_count > 5:
                raise ValueError
            break
        except ValueError:
            print("⚠️ 1부터 3 사이의 정수를 입력해주세요! ⚠️")
    
    invited_players = random.sample(players, invited_count)
    invited_info = {player: random.choice([2, 4, 6, 8, 10]) for player in invited_players}
    print("\n오늘 함께 취할 친구들:")
    for player, capacity in invited_info.items():
        print(f" - {player}: 🍺주량 {capacity}잔")
    print(f" - {user_name}: 🍺주량 {user_capacity}잔")
    
    play_nunchi_game(user_name, user_capacity, invited_info)


def play_nunchi_game(user_name, user_capacity, invited_info):
    players = [user_name] + list(invited_info.keys())  
    player_caps = {user_name: user_capacity, **invited_info}  
    drink_count = {player: 0 for player in players} 
    player_timers = {player: round(random.uniform(0.1, 5.0), 1) for player in invited_info.keys()} 
    current_number = 1  

    while not any(drink_count[player] >= player_caps[player] for player in players):  
        time.sleep(3)
        print(f"\n💕{user_name}님, 셋 세고 눈치치게임을 시작합니다!💕\n")
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
                user_input = int(input(f"{user_name}님, 숫자를 입력하세요!\n"))  
                with lock:
                    spoken_numbers[time.time()] = (user_name, user_input) 
                print(f"{user_name}: {user_input}!!!!!!!!!")
                user_spoken = True
            except ValueError:
                print("⚠️ 숫자를 입력해주세요!⚠️")
                time.sleep(1)  
        
        time.sleep(5)  

        process_results(spoken_numbers, drink_count, player_caps, current_number)  
        current_number = 1  

        print("\n현재 상황:")
        for player, count in drink_count.items():
            remaining = player_caps[player] - count  
            print(f" - {player}: {count}잔 마심🥴 (치사량까지 {remaining}잔 남음)")
        time.sleep(1)

    print("\n❗ 게임 종료! ❗")
    for player, count in drink_count.items():
        if count >= player_caps[player]:
            print(f" - 😵 {player}님이 치사량에 도달했습니다!😵")
    print("오늘은 여기까지!! 다음에 또 만나요! 🥂💕")


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

def process_results(spoken_numbers, drink_count, player_caps, current_number):
    occurrences = {}
    for timestamp, (player, number) in spoken_numbers.items():
        if number not in occurrences:
            occurrences[number] = []
        occurrences[number].append(player)
    
    for number, players in occurrences.items():
        if len(players) > 1: 
            print(f"✅ 숫자 {number}를 동시 발언! {' '.join(players)} 모두 1잔 추가!✅")
            for player in players:
                drink_count[player] += 1
            time.sleep(1)  

    if len(occurrences[current_number]) == 1:  
        last_spoken_player = get_last_spoken_player(spoken_numbers)  
        if last_spoken_player:  
            print(f"✅ 마지막으로 숫자를 외친 {last_spoken_player}님이 1잔 추가!✅")
            drink_count[last_spoken_player] += 1
            time.sleep(1)

start_game() 