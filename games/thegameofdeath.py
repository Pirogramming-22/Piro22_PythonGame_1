import time
import random

def chooserPerson(participants):
    result_of_choose = {}
    for person in participants:
        while True:
            random_person = random.choice(participants)
            if random_person != person:  # 자신을 선택하지 않도록 설정
                result_of_choose[person] = random_person
                break
    return result_of_choose

def startPoint(participants, result_of_choose, starting_player, selected_person, num):
    current_person = starting_player  # 첫 번째 플레이어는 게임의 시작 플레이어
    result_of_choose[starting_player] = selected_person  # 첫 번째 선택된 사람으로 설정
    count = 1

    while count <= num:
        next_person = result_of_choose[current_person]
        print(f"{current_person} 👉 {next_person}  \"{count}\"")  # 출력 형식
        time.sleep(0.5)
        current_person = next_person  # 다음 지목된 사람으로 업데이트
        count += 1

    return current_person  # 마지막 지목된 사람이 반환됨

def play(player_name, opponents_with_limits, player_lives, drink_count, starting_player=None, first_game=False):
    participants = [player_name] + list(opponents_with_limits.keys())

    # 첫 번째 게임에서는 사용자가 지정한 플레이어가 스타팅
    if not first_game:
        starting_player = random.choice(participants)
    print(f"\n========== {starting_player}님이 이번 더 게임 오브 데스의 첫 번째 플레이어로 시작합니다! ==========")

    # 규칙 설명
    print("\n🎉 아싸 신난다 🎵 재미난다 🎵 🎉")
    time.sleep(1)
    print("✨✨ 더 게임 오브 데쓰 ✨✨")
    time.sleep(2)
    print("\n🃏 규칙 안내:")
    print("1️⃣ 한 명을 선택하세요!")
    print("2️⃣ 1 이상의 숫자를 입력하여 순서를 설정합니다.")
    print("3️⃣ 마지막으로 지목된 사람이 패자가 됩니다.")
    print("-----------------------------------\n")
    time.sleep(2)

    bsShot = 3
    selected_person = None

    # 첫 번째 단계: 한 명 선택
    while bsShot > 0:
        print("\n참여자 목록:")
        for participant in participants:
            if participant != starting_player:
                print(f"- {participant}")
        selected_person = input(f"{starting_player}님, 한 명을 선택하세요: ").strip()
        if selected_person not in participants or selected_person == starting_player:
            print("⚠️ 잘못된 이름입니다! 다시 선택하세요.\n")
            bsShot -= 1
        else:
            print(f"\n✨ {selected_person}님이 선택되었습니다! ✨")
            time.sleep(1)
            break

    if bsShot == 0:
        print("\n🎵🎵 바보샷! 바보샷! 바보샷은 인트로도 없어요 🎵🎵")
        time.sleep(1)
        looser = starting_player
        print(f"\n🎉 {looser}님이 패자가 되었습니다! 🍺")
        player_lives[looser] -= 1
        drink_count[looser] += 1
        return looser

    # 두 번째 단계: 숫자 입력
    while True:
        num_input = input(f"{starting_player}님, 1 이상의 숫자를 입력해주세요: ").strip()
        if not num_input.isdigit() or int(num_input) <= 0:
            print("⚠️ 1 이상의 정수를 입력해주세요!\n")
        else:
            num = int(num_input)
            print(f"\n🎯 {num}번의 지목을 시작합니다! 🎯\n")
            time.sleep(1)
            break

    # 세 번째 단계: 게임 진행
    result_of_choose = chooserPerson(participants)  # 지목 순서 설정
    looser = startPoint(participants, result_of_choose, starting_player, selected_person, num)

    # 패자 처리
    print(f"\n🎉 {looser}님이 패자가 되었습니다! 🍺")
    player_lives[looser] -= 1
    drink_count[looser] += 1

    # 현재 상태 출력
    print("\n현재 목숨 상태:")
    for player, lives in player_lives.items():
        print(f"- {player}: {lives}잔 남음")

    print("\n-----------------------------------")
    print("게임 선택 화면으로 돌아갑니다.")
    return looser