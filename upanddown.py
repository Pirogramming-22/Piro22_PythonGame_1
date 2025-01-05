import random
import time

def up_and_down_game(player_name, members, starting_player):
    print("==========업 앤 다운 게임==========")
    time.sleep(2)
    print(f"\n1부터 100사이의 랜덤 숫자가 정해졌습니다! {starting_player}부터 시작합니다.")
    time.sleep(2)
    print("\n그 숫자를 맞춰보세요!")
    time.sleep(2)

    # 랜덤 숫자 생성
    target_num = random.randint(1,100)

    #숫자 선택 범위
    range = [1,100]

    #starting_player를 시작으로 순서 설정
    members_order = members[members.index(starting_player):] + members[:members.index(starting_player)]


    while True:  # 게임이 끝날 때까지 반복
        for member in members_order:
            print(f"\n=========={member}님의 차례입니다!==========")
            time.sleep(2)

            if member == player_name:
                # 올바른 입력을 받을 때까지 반복
                while True:  
                    user_input = input(f"{player_name}님, 숫자를 입력하세요! ({range[0]} ~ {range[1]}): ")

                    # 숫자인지 확인
                    if not user_input.isdigit():
                        print("올바른 숫자를 입력해주세요!")
                        continue

                    # 숫자면 정수로 변환
                    guess = int(user_input)

                    # 범위에 맞는 숫자인지 확인
                    if guess < range[0] or guess > range[1]:
                        print(f"{range[0]}부터 {range[1]} 사이의 숫자를 입력해주세요!")
                        continue

                    # 입력이 올바르게 됐으면 반복 탈출
                    break

            # player가 아닌 다른 사람일 경우 자동으로 답 말하기
            else:
                guess = random.randint(range[0],range[1])
                print(f"\n{member}님이 {guess}를 선택하셨습니다!")

        
            # 업 앤 다운 판명
            if guess > target_num:
                print("\nDOWN! 더 작은 숫자를 입력하세요!")
                range[1] = guess - 1

            elif guess < target_num:
                print("\nUP! 더 큰 숫자를 입력하세요!")
                range[0] = guess + 1

            else: # 정답을 맞췄을 경우
                print(f"\n🥳🎊 {member}님이 정답을 맞췄습니다~")
                print(f"정답은 {target_num}이었습니다~")
                print(f"맞춘 사람 빼고 나머지 다 마셔!🍺")
                return member

