import time
import random

# 전역 변수
user_list_without_me = []
user_list_include_me = []
result_of_choose = []

# 지목 함수
def choosePerson(num):
    global result_of_choose
    result_of_choose = []  # 초기화

    # 무작위로 num만큼 지목
    for _ in range(num):
        random_person = random.choice(user_list_include_me)
        result_of_choose.append(random_person)

# TIME을 주어 시간차를 두고 한 명씩 지목
def startPoint(num):
    current_person = userName  # 사용자(`userName`)부터 시작
    count = 1
    while count <= num:
        next_person = result_of_choose[count - 1]  # 무작위로 지목된 사람 사용
        print(current_person, "👉🏻", next_person, "   \"", count, "\"")
        time.sleep(0.5)
        current_person = next_person  # 다음 사람으로 업데이트
        count += 1

    looser = current_person
    print(looser, "당첨 !!!")  # 최종 패자 출력
    return looser

def theGameOfDeath(listWithoutUser, user):
    global user_list_without_me, user_list_include_me, userName

    userName = user
    user_list_without_me = listWithoutUser[:]
    user_list_include_me = listWithoutUser[:]
    user_list_include_me.append(userName)

    print("아싸 신난다 🎵 재미난다 🎵")
    time.sleep(1)
    print("더 게임 오브 데쓰 ❕❕")

    bsShot = 3
    looser = None

    # 첫 번째 단계: 사람 선택
    pointPerson = None
    while bsShot > 0:
        print("게임 참여자 목록 : ", user_list_without_me)
        pointPerson = input("한 명을 가리키세요! : ").strip()  # 공백 제거
        if pointPerson not in user_list_without_me:
            print("잘못된 이름입니다!\n")
            bsShot -= 1
        elif pointPerson == userName:
            print("자신을 선택할 수 없습니다!\n")
            bsShot -= 1
        else:
            break

    if bsShot == 0:
        print("🎵🎵 바보샷! 바보샷! 바보샷은 인트로도 없어요 🎵🎵")
        return userName

    # 두 번째 단계: 숫자 입력
    num = None
    while bsShot > 0:
        num_input = input("숫자를 입력해주세요! : ")
        if not num_input.isdigit():  # 숫자가 아닐 경우
            print("정수를 입력해주세요!")
            bsShot -= 1
        else:
            num = int(num_input)
            if num <= 0:  # 0 이하일 경우
                print("0보다 큰 숫자를 입력해주세요!")
                bsShot -= 1
            else:
                break

    if bsShot == 0:
        print("🎵🎵 바보샷! 바보샷! 바보샷은 인트로도 없어요 🎵🎵")
        return userName

    # 세 번째 단계: 게임 진행
    choosePerson(num)  # 사용자 입력을 기반으로 지목 순서 생성
    looser = startPoint(num)  # 게임 시작

    return looser

# 게임 실행
print("최종 패자: ", theGameOfDeath(["수연", "준혁", "설아"], "기훈"))
