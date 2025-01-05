import random

#멤버는 병합할 때 바꿀 예정 임시로 만든 리스트임
members = ["준혁","혜린","승인","설아","진수"]  

def up_and_down_game():
    print("==========업 앤 다운 게임==========")
    print("1부터 100사이의 랜덤 숫자가 정해졌습니다!")
    print("그 숫자를 맞춰보세요!")

    # 랜덤 숫자 생성
    target_num = random.randint(1,100)

    while True:  # 게임이 끝날 때까지 반복
        for member in members:
            print(f"\n=========={member}님의 차례입니다!==========")

             # 올바른 입력을 받을 때까지 반복
            while True:  
                user_input = input("숫자를 입력하세요 (1~100): ")

                # 숫자인지 확인
                if not user_input.isdigit():
                    print("올바른 숫자를 입력해주세요!")
                    continue

                # 숫자면 정수로 변환
                guess = int(user_input)

                # 범위에 맞는 숫자인지 확인
                if guess < 1 or guess > 100:
                    print("1부터 100 사이의 숫자를 입력해주세요!")
                    continue

                # 입력이 올바르게 됐으면 반복 탈출
                break
        
            # 업 앤 다운 판명
            if guess > target_num:
                print("\nDOWN! 더 작은 숫자를 입력하세요!")

            elif guess < target_num:
                print("\nUP! 더 큰 숫자를 입력하세요!")

            else: # 정답을 맞췄을 경우
                print(f"\n🥳🎊 {member}님이 정답을 맞췄습니다~")
                print(f"정답은 {target_num}이었습니다~")
                print(f"맞춘 사람 빼고 나머지 다 마셔!🍺")
                return member

up_and_down_game_winner = up_and_down_game()
