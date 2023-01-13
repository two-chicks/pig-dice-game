# pig-dice-game
~

# How to Start
```
$ python pig-dice-game.py
```

# 기능 구현 사항
## 입력 기능
- [ ] 이름을 입력 받는다
    - [ ] 입력값이 공백인 경우 예외처리한다
    - [ ] 입력값이 문자가 아닌 숫자나 기호인 경우 예외처리한다
- [ ] 사용자로부터 주사위를 돌릴 것인지 턴을 넘길 것인지에 대한 의사를 입력 받는다
    - [ ] 입력값이 공백인 경우 예외처리한다
    - [ ] 입력값이 문자가 아닌 숫자나 기호인 경우 예외처리한다
    - [ ] 입력값이 'Go' 또는 'Exit'이 아닌 경우 예외처리한다
- [ ] 게임이 끝난 경우 재시도 여부에 대해 입력 받는다
    - [ ] 입력값이 공백인 경우 예외처리한다
    - [ ] 입력값이 문자가 아닌 숫자나 기호인 경우 예외처리한다
    - [ ] 입력값이 'Retry' 또는 'Exit'이 아닌 경우 예외처리한다

## 출력 기능
- [ ] '게임을 시작합니다' 문장을 출력한다
- [ ] 사용자가 주사위를 돌릴 때마다 갱신된 현재 점수를 출력한다
- [ ] 이긴 경우 축하하는 메시지를 출력한다
- [ ] 진 경우 안타까운 메시지를 출력한다

## 기능
- [ ] 사용자가 'Go' 를 입력하면 주사위를 돌린다
- [ ] 나온 주사위 값만큼 현재 점수를 갱신한다
- [ ] 나온 주사위 값이 1이면 현재 점수는 초기화된다
- [ ] 나온 주사위 값이 1이면 자동으로 턴이 바뀐다
- [ ] 컴퓨터가 주사위를 돌리는 횟수는 random 라이브러리로 결정한다 
- [ ] 컴퓨터의 턴일 때 sleep 라이브러리를 사용한다
- [ ] Exit 눌렀을 때는 현재 점수를 최종 점수에 반영한다
- [ ] 100점인 경우 게임을 종료한다
- [ ] 게임 종료 후 사용자가 게임을 재시작하면 모든 점수를 초기화한다

# 게임 진행 예시
```
주사위 게임을 시작합니다
이름을 입력해주세요: Sujin Jo

[ Sujin Jo의 최종 점수: 0 | 상대방(컴퓨터)의 최종 점수: 0 ]
[ 이번 턴의 Sujin Jo의 점수 : 0 ]
주사위를 돌리려면 'Go'를, 턴을 넘기려면 'Exit'을 입력해주세요: Go

3점이 나왔습니다!
[ Sujin Jo의 최종 점수: 3 | 상대방(컴퓨터)의 최종 점수: 0 ]
[ 이번 턴의 Sujin Jo의 점수 : 3 ]
주사위를 돌리려면 'Go'를, 턴을 넘기려면 'Exit'을 입력해주세요: Go

5점이 나왔습니다!
[ Sujin Jo의 최종 점수: 5 | 상대방(컴퓨터)의 최종 점수: 0 ]
[ 이번 턴의 Sujin Jo의 점수 : 2 ]
주사위를 돌리려면 'Go'를, 턴을 넘기려면 'Exit'을 입력해주세요: Exit

----- 컴퓨터의 차례입니다 -----

6점이 나왔습니다!
[ Sujin Jo의 최종 점수: 5 | 상대방(컴퓨터)의 최종 점수: 0 ]
[ 이번 턴의 컴퓨터의 점수 : 6 ]

6점이 나왔습니다!
[ Sujin Jo의 점수: 5 | 상대방(컴퓨터)의 점수: 0 ]
[ 이번 턴의 컴퓨터의 점수 : 12 ]

1점이 나왔습니다!
이번 턴의 점수가 초기화됩니다.
[ Sujin Jo의 점수: 5 | 상대방(컴퓨터)의 점수: 0 ]
[ 이번 턴의 컴퓨터의 점수 : 0 ]

----- Sujin Jo의 차례입니다 -----

(100점을 Sujin Jo가 얻게 된 상황)

축하합니다! 게임에 이기셨습니다!
게임 재시작을 원하면 'Retry'를, 종료를 원하면 'Exit'을 입력해주세요: Exit
게임을 종료합니다.

(컴퓨터가 이긴 경우)

안타깝네요. 컴퓨터가 이겼습니다..
게임 재시작을 원하면 'Retry'를, 종료를 원하면 'Exit'을 입력해주세요: Exit
게임을 종료합니다.

```