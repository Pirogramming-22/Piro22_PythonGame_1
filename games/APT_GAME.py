import random
import time

def hand_shuffle(players):
    hands = []
    for player in players:
        hands.append(f"{player}의 왼손")
        hands.append(f"{player}의 오른손")
    random.shuffle(hands)
    return hands

def play(player_name, opponents_with_limits, player_lives, drink_count, first_game=True):
    participants = [player_name] + list(opponents_with_limits.keys())

    # 술래 설정
    if first_game:
        tagger = player_name
    else:
        tagger = random.choice(participants)

    print(f"술래는 {tagger}!!!!")
    if tagger in ['설아', '진수']:
        print(f"{tagger}가~ 좋아하는 랜덤 게임~ 랜덤 게임~ 게임 스타트! ")
    else:
        print(f"{tagger}이가 좋아하는 랜덤 게임~ 랜덤 게임~ 게임 스타트! ")
    print("아파트 시작~!!!!!")
    time.sleep(2)

    # 층수 설정
    if first_game or tagger == player_name:
        while True:
            try:
                target_floor = int(input(f"{tagger}님, 몇 층으로 할까요? (5~30층): ").strip())
                if 5 <= target_floor <= 30:
                    break
                else:
                    print("⚠️ 5층에서 30층 사이의 숫자를 입력해주세요!")
            except ValueError:
                print("⚠️ 올바른 숫자를 입력해주세요!")
    else:
        target_floor = random.randint(5, 30)
        print(f"{tagger}님이 외친 층수는 {target_floor}층!!!!")
    time.sleep(2)

    # 손 섞기
    hands = hand_shuffle(participants)

    print("\n현재 손이 포개진 순서:")
    for i, hand in enumerate(hands, start=1):
        print(f"{i}층: {hand}")
    time.sleep(2)

    print("\n손을 빼는 과정:")
    for i in range(1, target_floor + 1):
        hand_remove = hands.pop(0)
        hands.append(hand_remove)
        print(f"{i}층에 있는 {hand_remove}빼기")
        time.sleep(0.5)

    loser_hand = hands[0]
    loser = loser_hand.split('의')[0]
    print(f"\n{target_floor}층에서 뺀 손은~? {loser_hand}!")
    if loser in ['준혁', '혜린', '승인']:
        print(f"게임에서 진 {loser}이는~?")
    else:
        print(f"게임에서 진 {loser}는~?")
    print("마셔라~ 마셔라~ 마셔라~ 술이 들어간다!")
    time.sleep(2)

    # 패자 목숨 감소 및 drink_count 업데이트
    player_lives[loser] -= 1
    drink_count[loser] += 1

    print("\n-----------------------------------")
    print("게임 선택 화면으로 돌아갑니다.\n")
    return loser