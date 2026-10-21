class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def show_info(self):
        print(f"{self.member_id} / {self.name} / {self.email}")


def main():
    member_data = [
        ("user01", "이상무", "jamesol9@naver.com"),
        ("user02", "이영희", "jamesol8@naver.com"),
        ("user03", "김철수", "jamesol7@naver.com"),
    ]

    members = []

    for member_id, name, email in member_data:
        # print(member_id, name, email)
        member = Member(member_id, name, email)
        members.append(member)

    print("회원 추가")

    members.append(Member("user11", "상순11", "jamesol11@naver.com"))
    members.append(Member("user12", "상순12", "jamesol12@naver.com"))
    members.append(Member("user13", "상순13", "jamesol13@naver.com"))

    print("===== 전체 회원 목록 =====")

    for member in members:
        member.show_info()

    print("전체 회원 수:", len(members))


if __name__ == "__main__":
    main()
