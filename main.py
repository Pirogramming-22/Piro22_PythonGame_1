import random
from games import game_369  # 369 게임
from games import upanddown  # 업앤다운 게임
from games import game_nunchi  # 눈치게임
from games import thegameofdeath
from games import APT_GAME

users = ["준혁", "설아", "승인", "혜린", "진수"]

def start_game():
    print("게임을 시작하시겠습니까? (y/n)")
    while True:
        choice = input(">> ").strip().lower()
        if choice == 'y':
            print("-----------------------------------")
            return True
        elif choice == 'n':
            print("게임을 종료합니다.")
            exit()
        else:
            print("잘못된 입력입니다. y 또는 n을 입력해주세요.")

def get_player_name():
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

def select_drinking_limit():
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

def invite_opponents(player_name):
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

def show_game_list():
    print("-----------------------------------")
    print("게임 목록:")
    print("1) 369 게임")
    print("2) 업앤다운 게임")
    print("3) 눈치 게임")
    print("4) 더 게임 오브 데스")
    print("5) 아파트 게임")
    while True:
        choice = input("플레이할 게임을 선택해주세요 (번호 입력): ").strip()
        if choice == '1':
            return "369 게임"
        elif choice == '2':
            return "업앤다운 게임"
        elif choice == '3':
            return "눈치 게임"
        elif choice == '4':
            return "더 게임 오브 데스"
        elif choice == '5':
            return "아파트 게임"
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    if not start_game():
        exit()
    player_name = get_player_name()
    player_limit = select_drinking_limit()
    player_lives = {player_name: player_limit}
    opponents_with_limits = invite_opponents(player_name)

    for opponent, limit in opponents_with_limits.items():
        player_lives[opponent] = limit

    first_game = True

    while True:
        selected_game = show_game_list()
        print(f"\n{selected_game}이(가) 선택되었습니다.")
        if selected_game == "369 게임":
            starting_player = random.choice([player_name] + list(opponents_with_limits.keys())) if not first_game else player_name
            game_369.play(player_name, opponents_with_limits, player_lives, starting_player, first_game)
        elif selected_game == "업앤다운 게임":
            # 첫 번째 게임이 아닌 경우 새로운 시작 플레이어 선택
            starting_player = random.choice([player_name] + list(opponents_with_limits.keys())) if not first_game else player_name
            upanddown.play(player_name, opponents_with_limits, player_lives, starting_player)
        elif selected_game == "눈치 게임":
            game_nunchi.play(player_name, opponents_with_limits, player_lives, first_game)
        elif selected_game == "더 게임 오브 데스":
            starting_player = random.choice([player_name] + list(opponents_with_limits.keys())) if not first_game else player_name
            thegameofdeath.play(player_name, opponents_with_limits, player_lives, starting_player, first_game)
        elif selected_game == "아파트 게임":
            APT_GAME.play(player_name, opponents_with_limits, player_lives)

        first_game = False

        for player, lives in player_lives.items():
            if lives <= 0:
                print(f"\n{player}(이)가 만취해서 잠들어버렸습니다... 술 게임 종료~!")
                exit()