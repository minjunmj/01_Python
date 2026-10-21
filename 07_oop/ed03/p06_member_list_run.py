class Member:

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def show_info(self):
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print("-"*20)