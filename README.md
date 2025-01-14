# 피로그래밍 2주차 1조 과제!
## 1. 파트 분담
- 최준혁: 369 게임, 메인 실행 코드 제작
- 민설아: 더 게임 오브 데스
- 임진수: 업 앤 다운
- 박혜린: 눈치 게임
- 유승인: 아파트 게임

## 2. 게임 코드 로직
### game_369.py
* 1부터 시작하며, 3, 6, 9가 포함되는 숫자엔 '짝'을 입력하고 이외의 숫자는 그대로 숫자를 입력
* 게임 플레이어를 제외한 나머지는 자동으로 값을 입력하고 30% 확률로 오답을 입력하게 구현

### thegameofdeath
* 플레이어가 첫 번째 단계에서 다른 참가자를 선택하고, 숫자 입력을 통해 지목 횟수를 정함(이때 다른 참가자들은 랜덤으로 다른 사람을 선택)
* 플레이어를 시작으로 지목한 사람을 따라 숫자를 세고, 정해진 숫자에 지목된 사람이 패자가 되어 술을 마시게 됨
* 잘못된 이름이나 숫자를 반복해서 입력하면 "바보샷"이 발동하고, 플레이어가 패자가 되어 술을 마시게 됨

### upanddown.py
* 1부터 100까지의 랜덤 숫자를 하나가 지정됨
* 게임 참여자 순서대로 정답을 입력(범위 밖의 숫자를 입력 할 시에는 다시 입력을 받음)
* 앞서 말한 숫자가 정답이 아닐 경우 up, down의 여부에 따라 다음 차례의 인원이 맞출 수 있는 수의 범위를 체크
* 가장 먼저 답을 맞추는 사람을 제외하고 나머지 인원이 모두 술을 마시게 됨

### game_nunchi.py
* play 함수에서 눈치 게임을 진행하며, computer_speak 함수로 초대된 플레이어의 발언 시간을 지정
* spoken_numbers 딕셔너리는 발언된 숫자와 발언자를 기록하여 게임의 결과를 계산하는 데 사용
* process_results 함수는 발언된 숫자를 분석하여 동시 발언자 또는 마지막 발언자를 확인하고, 그에 따라 마신 술을 반영함.

### APT_GAME.py
* hand_shuffle 함수를 통해 각 플레이어의 왼손과 오른손을 리스트에 추가하고 무작위로 섞음
* play 함수로 첫 게임이거나 사용자 차례면 사용자가, 아니면 무작위로 술래를 선정
* 첫 게임이거나 사용자가 술래면 사용자가 5~30 사이의 층수를 입력하여 층수 선정
*  hand_shuffle 함수를 호출하여 참가자들의 손을 무작위로 섞은 후에 선택된 층수만큼 반복하여 손을 빼고 다시 맨 아래에 넣는 과정을 반복 후
   마지막으로 남은 손의 주인이 패자가 되도록 결과 처리.
## 3. 메인 코드
* 기본적으로 모든 게임 코드는 play라는 실행 함수로 묶음
* games/ 폴더안에 게임 코드를 넣어두고 import해와서 메인코드에서 작동될 수 있게 구현
* 제일 처음 게임을 진행하는 플레이어(ex. 준혁)가 게임을 선택하면(ex.369게임) 처음 게임 종료 후엔 게임과 첫번째 플레이어가 랜덤으로 지정되서 게임 진행
* 주량과 마신 횟수 카운트는 메인 코드에서 정의하고 각 게임의 Play함수의 매개변수로 넣어서 게임이 끝날 때 마다 계속 업데이트 될 수 있도록 함

## 4. 회의 일정
- 1월 5일 (오후 12시): 각자 브랜치를 파서 게임 업로드 및 게임 로직 설명 -> 메인 코드 기획
- 1월 6일 (오후 11시): 변수명, 함수 로직 메인 코드와 동기화 -> 테스트 후 버그 수정, 메인 코드 로직 추가 및 변경

## 5. 참고 링크
* https://drive.google.com/file/d/1aAXK3ZICofg_z6f50OsNtOacNLBxOB2H/view

* https://wepplication.github.io/tools/asciiArtGen/
