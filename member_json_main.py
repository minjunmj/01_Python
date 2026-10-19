from member_service import load_members, register_member, save_members

def main():
    members = load_members()
    print(f"members: {members}")

    result = register_member(members, "pcwk01", "이상무")
    print(f"result: {result}")
    print(f"members: {members}")

    if result:
        save_members(members)
        print("회원등록 완료")
    else:
        print("이미 등록된 회원입니다")


if __name__ == "__main__":
    main()