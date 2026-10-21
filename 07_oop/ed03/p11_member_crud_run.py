class Member:

    def __init__(self, member_id, name, email, reg_date, password, role="USER"):

        if not member_id.strip():
            raise ValueError("회원ID는 필수입니다.")

        if not name.strip():
            raise ValueError("이름은 필수입니다.")

        if "@" not in email:
            raise ValueError("이메일 형식이 올바르지 않습니다.")

        self.member_id = member_id
        self.name = name
        self.email = email
        self.reg_date = reg_date
        self.role = role
        self.password = password

    def show_info(self):
        print(
            f"{self.member_id}/{self.name}/{self.email}/{self.reg_date}/{self.role}/{self.password}"
        )

def do_save(members, add_member):
    for member in members:
        if member.member_id == add_member.member_id:
            print("기존 회원ID가 존재 합니다.\n등록 불가")
            return 0
        
    members.append(add_member)
    return 1

def do_retrieve(members):
    for member in members:
        member.show_info()

def do_delete(members, member_id):
    for idx, member in enumerate(members):
        if member.member_id == member_id:
            del members[idx]
            return 1
    return 0

def do_select_one(members, member_id):
    for member in members:
        if member.member_id == member_id:
            return member
    return None

def do_update(members, mod_member):
    existing_member = do_select_one(members, mod_member.member_id)

    if existing_member is None:
        return 0

    existing_member.name = mod_member.name
    existing_member.email = mod_member.email
    existing_member.role = mod_member.role
    existing_member.password = mod_member.password
    return 1
            
def main():
    members = [
        Member("user01", "이상무", "jamesol9@naver.com", "2026-10-19", "USER", "4321a"),
        Member("user02", "이영희", "jamesol8@naver.com", "2026-10-20", "USER", "4321a"),
        Member("user03", "김철수", "jamesol7@naver.com", "2026-10-21", "USER", "4321a")
    ]

    new_member = Member("user13", "김철수11", "jamesol11@naver.com", "2026-10-21", "USER", "4321a")
    flag = do_save(members, new_member)
    if flag:
        print("회원 등록 성공")
    else:
        print("회원 등록 실패")

    print("===== 전체 회원 목록 =====")

    do_retrieve(members)

    flag = do_delete(members, "user01")
    if flag:
        print("회원 삭제")
    else:
        print("회원 삭제 실패")

    do_retrieve(members)

    one_member = do_select_one(members, member_id="user03")
    print("===== 단건 조회 =====")
    one_member.show_info()

    new_member = Member("user03", "김철수_U", "jamesol7_U@naver.com", "2026-10-21", "ADMIN", "4321aU")
    flag = do_update(members, new_member)
    if flag:
        print("수정 성공")
    else:
        print("수정 실패")

    one_member = do_select_one(members, member_id="user03")
    print("===== 단건 조회 =====")
    one_member.show_info()
           
    print("전체 회원 수:", len(members))

if __name__ == "__main__":
    main()
