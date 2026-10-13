import member

def do_save():
    print("do_save()")
    
    is_saved = member.do_save('pcwk01', "이상무", "jamesol@paran.com")

    if is_saved:
        print("등록 성공")
    else:
        print("등록 실패")

    print(f"등록 회원 조회: {member.do_retrieve()}")

def main():
    print("main()")

    do_save()

if __name__ == "__main__":
    main()

    print(member.do_select_one('pcwk01'))