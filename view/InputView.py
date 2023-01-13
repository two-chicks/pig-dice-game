class InputView:
    
    def validate_username():
        while True:
            username = input("이름을 입력하세요: ")
            try:
                username = int(username)
                print(('이름에 숫자 혹은 공백을 입력하셨습니다.'))
                continue
            except ValueError:
                if len(username) == 0:
                    print(('이름에 숫자 혹은 공백을 입력하셨습니다.'))
                    continue
                return username
    
    def go_stop():
        while True:
            choice = input("주사위를 돌리려면 'Go'를, 턴을 넘기려면 'Exit'을 입력해주세요: ")
            if choice.lower() == 'go' or choice.lower() == 'exit':
                return choice
            print('Go 혹은 Exit를 입력해주세요.')
