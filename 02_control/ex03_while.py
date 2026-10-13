print("="*50)
print("메뉴 프로그램 만들기")
print("="*50)

while True:
    print("=== 메뉴 ===")
    print("1. 회원 조회")
    print("2. 회원 등록")
    print("3. 종료")
    menu = int(input("메뉴 선택: "))
    if menu == 1:
        print("회원 조회를 선택했습니다\n")
    elif menu == 2:
        print("회원 등록을 선택했습니다\n")
    elif menu == 3:
        print("프로그램을 종료합니다")
        break
    else:
        print("잘못된 메뉴입니다")

