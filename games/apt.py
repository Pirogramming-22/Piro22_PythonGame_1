import random

players = ["준혁", "혜린", "승인", "설아", "진수"]

def hand_shuffle(players):
    hands = []
    for player in players:
        hands.append(f"{player}의 왼손")
        hands.append(f"{player}의 오른손")
    random.shuffle(hands)
    return hands

def apt_game():
    tagger = random.choice(players)
    print(f"술래는 {tagger}!!!!")
    if tagger in ['설아', '진수']:
        print(f"{tagger}가~ 좋아하는 랜덤 게임~ 랜덤 게임~ 게임 스타트! ")
    else:
        print(f"{tagger}이가 좋아하는 랜덤 게임~ 랜덤 게임~ 게임 스타트! ")
    print("아파트 시작~!!!!!")
    print("아파트 아파트~ 아파트 아파트~ 몇층??")

    target_floor = random.randint(5, 30)
    if tagger in ['설아', '진수']:
        print(f"{tagger}가 외친 층수는 {target_floor}층!!!!")
    else:
        print(f"{tagger}이가 외친 층수는 {target_floor}층!!!!")

    hands = hand_shuffle(players)

    print("\n현재 손이 포개진 순서:")
    for i, hand in enumerate(hands, start=1):
        print(f"{i}층: {hand}")

    print("\n손을 빼는 과정:")
    for i in range(1, target_floor + 1):
        hand_remove = hands.pop(0)
        hands.append(hand_remove)
        print(f"{i}층에 있는 {hand_remove}빼기")

    loser_hand = hands[0]
    loser = loser_hand.split('의')[0]
    print(f"\n{target_floor}층에서 뺀 손은~? {loser_hand}!")
    if loser in ['준혁', '혜린', '승인']:
        print(f"게임에서 진 {loser}이는~?")
    else:
        print(f"게임에서 진 {loser}는~?")
    print("마셔라~ 마셔라~ 마셔라~ 술이 들어간다!")

    return loser

# 아래 코드를 추가
if __name__ == "__main__":
    loser = apt_game()
    print(f"술을 마신 사람은~~~ {loser}")
