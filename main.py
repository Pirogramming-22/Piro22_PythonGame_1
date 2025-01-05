import random
from games import game_369

users = ["준혁", "설아", "승인", "혜린", "승민"]

def start_game(): # 게임 시작 여부 함수!
    print("게임을 시작하시겠습니까? (y/n)")
    while True:
        choice = input(">> ").strip().lower()
        if choice == 'y':
            print("-----------------------------------")
            return True
        elif choice == 'n':
            return False
        else:
            print("잘못된 입력입니다. y 또는 n을 입력해주세요.")
    

def get_player_name(): #첫번째 게임 시작 유저 정하는 함수!
    print("사용자 이름을 선택해주세요:")
    for name in users:
        print(f"- {name}")
    while True:
        name = input(">> ").strip()
        if name in users:
            return name
        else:
            print("-----------------------------------")
            print("잘못된 이름입니다. 다시 선택해주세요.")

def select_drinking_limit(): #유저 주량(목숨) 선택 함수!
    print("-----------------------------------")
    print("본인의 주량을 선택해주세요 (목숨 개수):")
    options = {
        1: 2,
        2: 4,
        3: 6,
        4: 8,
        5: 10
    }
    for key, value in options.items():
        print(f"{key}) 주량 {value}잔")
    while True:
        try:
            choice = int(input(">> "))
            if choice in options:
                return options[choice]
            else:
                print("-----------------------------------")
                print("잘못된 선택입니다. 1~5 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("-----------------------------------")
            print("숫자를 입력해주세요.")

def invite_opponents(player_name): #플레이어를 제외하고 게임할 유저와 주량 랜덤으로 고르는 함수!
    while True:
        try:
            print("-----------------------------------")
            num_opponents = int(input("초대할 인원 수 (1~3명): "))
            if 1 <= num_opponents <= 3:
                break
            else:
                print("-----------------------------------")
                print("잘못된 입력입니다. 1~3 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("-----------------------------------")
            print("숫자를 입력해주세요.")
    
    available_opponents = [name for name in users if name != player_name]
    opponents = random.sample(available_opponents, num_opponents)

    drinking_options = [2, 4, 6, 8, 10]
    opponents_with_limits = {opp: random.choice(drinking_options) for opp in opponents}

    print("-----------------------------------")
    print("초대된 사람들:")
    for opp, limit in opponents_with_limits.items():
        print(f"- {opp} (주량: {limit}잔)")
    return opponents_with_limits

def show_game_list(): #게임 목록, 게임 선택 함수
    print("-----------------------------------")
    print("게임 목록:")
    print("1) 369 게임")
    print("2) 숫자야구 (예시)")
    while True:
        choice = input("플레이할 게임을 선택해주세요 (번호 입력): ").strip()
        if choice == '1':
            return "369 게임"
        elif choice == '2':
            return "숫자야구"
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

# 게임 실행 코드
if __name__ == "__main__":
    if not start_game(): 
        print("게임을 종료합니다.")
    else: # y를 입력한 경우
        player_name = get_player_name() # 사용자가 선택한 플레이어 이름 받아오기
        player_limit = select_drinking_limit() # 사용자가 선택한 플레이어 주량 받아오기
        player_lives = {player_name: player_limit}
        opponents_with_limits = invite_opponents(player_name) # 다른 플레이어 이름, 주량 받아오기

        for opponent, limit in opponents_with_limits.items():
            player_lives[opponent] = limit #player_lives 딕셔너리에 나머지 플레이어의 "이름":주량 추가

        starting_player = player_name # 사용자가 고른 플레이어가 첫번째 게임의 처음 시작을 맡음

        while True:
            print(f"\n{starting_player}이(가) 이번 게임의 첫 번째 플레이어로 시작합니다!")

            selected_game = show_game_list()
            print(f"\n{selected_game}이(가) 선택되었습니다.")

            if selected_game == "369 게임":
                game_369.play(player_name, opponents_with_limits, player_lives, starting_player)
            elif selected_game == "숫자야구(예시)":
                game_other.play(player_name, opponents_with_limits, player_lives, starting_player)
            
            starting_player = random.choice([player_name] + list(opponents_with_limits.keys())) #첫번째 게임이 끝나고 처음 게임을 시작한 플레이어를 제외한 나머지 플레이어에서 한명이 랜덤으로 다음게임에서 처음 시작을 맡음

            for player, lives in player_lives.items(): 
                if lives <= 0: # 주량이 0이 된 경우 출력됨
                    print(f"\n{player}(이)가 만취해서 잠들어버렸습니다... 술 게임 종료~!")
                    exit()