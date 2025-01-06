import time
import random

def play(player_name, opponents_with_limits, player_lives, starting_player=None, first_game=False):
    participants = [player_name] + list(opponents_with_limits.keys())

    # 첫 번째 게임 이후 랜덤으로 새로운 첫 번째 플레이어 선택
    if not first_game:
        starting_player = random.choice(participants)

    # 인트로 출력
    print("\n🎉 아싸 신난다 🎵 재미난다 🎵 🎉")
    time.sleep(1)
    print("✨✨ 더 게임 오브 데쓰 ✨✨")
    time.sleep(2)
    print("\n🃏 규칙 안내:")
    time.sleep(1)
    print("1️⃣ 한 명을 선택하세요!")
    time.sleep(1)
    print("2️⃣ 1 이상의 숫자를 입력하여 순서를 설정합니다.")
    time.sleep(1)
    print("3️⃣ 마지막으로 지목된 사람이 패자가 됩니다.")
    print("-----------------------------------\n")
    time.sleep(2)

    print("\n========== 더 게임 오브 데스 ==========")
    time.sleep(2)

    print("\n참여자 목록:")
    for participant in participants:
        print(f"- {participant} (남은 주량: {player_lives[participant]}잔)")
    time.sleep(2)

    bsShot = 3
    selected_person = None

    # 첫 번째 단계: 한 명 선택
    while bsShot > 0:
        print("\n참여자 목록:")
        for participant in participants:
            if participant != player_name:
                print(f"- {participant}")
        selected_person = input(f"{player_name}님, 한 명을 선택하세요: ").strip()

        if selected_person not in participants or selected_person == player_name:
            print("⚠️ 잘못된 선택입니다. 다른 사람을 선택해주세요!")
            bsShot -= 1
        else:
            print(f"\n✨ {selected_person}님이 선택되었습니다! ✨")
            time.sleep(1)
            break

    if bsShot == 0:
        print("\n🎵🎵 바보샷! 바보샷! 바보샷은 인트로도 없어요 🎵🎵")
        return player_name

    # 두 번째 단계: 숫자 입력
    bsShot = 3
    while bsShot > 0:
        num_input = input(f"{player_name}님, 1 이상의 숫자를 입력해주세요: ").strip()
        if not num_input.isdigit() or int(num_input) <= 0:
            print("⚠️ 1 이상의 정수를 입력해주세요!")
            bsShot -= 1
        else:
            num = int(num_input)
            print(f"\n🎯 {num}번의 지목을 시작합니다! 🎯")
            time.sleep(1)
            break

    if bsShot == 0:
        print("\n🎵🎵 바보샷! 바보샷! 바보샷은 인트로도 없어요 🎵🎵")
        return player_name

    # 세 번째 단계: 게임 진행
    result_of_choose = []
    for _ in range(num):
        random_person = random.choice(participants)
        result_of_choose.append(random_person)

    current_person = selected_person
    for idx, next_person in enumerate(result_of_choose):
        print(f"{current_person} 👉🏻 {next_person}   \"{idx + 1}\"")
        time.sleep(0.5)
        current_person = next_person

    looser = current_person
    print(f"\n🎉 {looser}님이 패자가 되었습니다! 🍺")
    print(f"{looser}님은 1잔 마십니다!")
    player_lives[looser] -= 1

    # 현재 상태 출력
    print("\n현재 목숨 상태:")
    for player, lives in player_lives.items():
        print(f"- {player}: {lives}잔 남음")

    print("\n-----------------------------------")
    print("게임 선택 화면으로 돌아갑니다.")
    return looser