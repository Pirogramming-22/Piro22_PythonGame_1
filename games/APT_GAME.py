import random
import time

def hand_shuffle(players):
    hands = []
    for player in players:
        hands.append(f"{player}의 왼손")
        hands.append(f"{player}의 오른손")
    random.shuffle(hands)
    return hands

def play(player_name, opponents_with_limits, player_lives):
    participants = [player_name] + list(opponents_with_limits.keys())

    # 술래 선정
    tagger = random.choice(participants)
    print(f"술래는 {tagger}!!!!")
    if tagger in ['설아', '진수']:
        print(f"{tagger}가~ 좋아하는 랜덤 게임~ 랜덤 게임~ 게임 스타트! ")
    else:
        print(f"{tagger}이가 좋아하는 랜덤 게임~ 랜덤 게임~ 게임 스타트! ")
    print("아파트 시작~!!!!!")
    time.sleep(2)
    print("아파트 아파트~ 아파트 아파트~ 몇층??")
    time.sleep(2)

    # 층수 설정
    target_floor = random.randint(5, 30)
    if tagger in ['설아', '진수']:
        print(f"{tagger}가 외친 층수는 {target_floor}층!!!!")
    else:
        print(f"{tagger}이가 외친 층수는 {target_floor}층!!!!")
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

    # 패자 목숨 감소
    player_lives[loser] -= 1
    print(f"\n현재 목숨 상태:")
    for player, lives in player_lives.items():
        print(f"- {player}: {lives}잔 남음")
    time.sleep(2)

    print("\n-----------------------------------")
    print("게임 선택 화면으로 돌아갑니다.\n")
    return loser