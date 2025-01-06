import time
import random

def choosePerson(players):
    result_of_choose = {}
    for person in players:
        while True:
            random_person = random.choice(players)
            if random_person != person:  # 자기 자신 제외
                result_of_choose[person] = random_person
                break
    return result_of_choose

def startPoint(players, result_of_choose, user_name, point_person, num):
    current_person = user_name  # 사용자가 선택한 사람부터 시작
    result_of_choose[user_name] = point_person  # 사용자가 지목한 사람 설정
    count = 1

    while count <= num:
        next_person = result_of_choose[current_person]  # 고정된 지목 대상
        print(current_person, "👉🏻", next_person, f" \"{count}\"")
        time.sleep(0.5)
        current_person = next_person
        count += 1

    looser = current_person  # 최종 패자
    print(looser, "당첨 !!!")
    return looser

def theGameOfDeath(user_name, opponents_with_limits, player_lives, starting_player):
    players = list(opponents_with_limits.keys()) + [user_name]  # 모든 플레이어 목록
    print("\n아싸 신난다 🎵 재미난다 🎵\n")
    time.sleep(1)
    print("더 게임 오브 데쓰 ❕❕\n")

    bsShot = 3
    point_person = None

    # 첫 번째 단계: 사람 선택
    while bsShot > 0:
        print("게임 참여자 목록:", ", ".join(opponents_with_limits.keys()))
        point_person = input("한 명을 가리키세요! : ").strip()
        if point_person not in players or point_person == user_name:
            if point_person == user_name:
                print("자신을 선택할 수 없습니다! 다시 선택하세요!\n")
            else:
                print("잘못된 이름입니다! 다시 선택하세요!\n")
            bsShot -= 1
        else:
            break


    # 두 번째 단계: 숫자 입력
    num = None
    while bsShot > 0:
        num_input = input("지목할 횟수를 입력해주세요: ")
        if not num_input.isdigit():  # 숫자가 아닌 경우
            print("정수를 입력해주세요!\n")
            bsShot -= 1
        else:
            num = int(num_input)
            if num <= 0:
                print("0보다 큰 숫자를 입력해주세요!\n")
                bsShot -= 1
            else:
                break

    if bsShot == 0:
        print("🎵 바보샷! 바보샷! 바보샷은 인트로도 없어요 🎵\n\n")
        return user_name  # 바보샷 소진 시 현재 사용자 반환

    # 세 번째 단계: 게임 진행
    result_of_choose = choosePerson(players)  # 지목 대상 설정
    looser = startPoint(players, result_of_choose, user_name, point_person, num)  # 게임 실행
    return looser
