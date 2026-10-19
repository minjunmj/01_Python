members = []

def do_save(user_id, name, email):
    """
        회원을 등록 합니다

        Args:
            user_id(str) : 회원ID
            name(str) : 이름
            email(str) : 이메일
        
        Return:
            True : 등록성공
            False : 등록실패
    """

    #기존 회원ID 존재 확인
    for member in members:
        if(member["user_id"] == user_id):
            return False

    #회원정보
    member = {
        "user_id": user_id,
        "name": name,
        "email": email
    }
    members.append(member)

    return True

def do_select_one(user_id):
    """
        회원 아이디로 조회합니다
        Args:
            user_id(str): 회원ID

        Return:
            member: {'user_id': 'pcwk01', 'name': '이상무', 'email': 'jamesol@paran.com'}
    """
    #전체 리스트 순회
    #user_id가 있는지 찾는다 있으면 member를 돌려 준다
    #없으면 None을 돌려준다

    for member in members:
        if(member['user_id'] == user_id):
            return member

    return None

def do_delete(user_id):
    """회원 아이디를 삭제합니다"""

    member = do_select_one(user_id)

    if member is None:
        return False

    members.remove(member)

    return True

def do_retrieve():
    """
        전체 회원 목록을 반환 합니다
    """
    return members.copy()

if __name__ == "__main__":
    print(f"members: {members}")

    is_saved01 = do_save('pcwk01', "이상무", "jamesol@paran.com")
    is_saved02 = do_save('pcwk02', "이순희", "jamesol02@paran.com")
    is_saved03 = do_save('pcwk01', "이상무", "jamesol@paran.com")

    print(f"is_saved01: {is_saved01}")
    print(f"is_saved02: {is_saved02}")
    print(f"is_saved03: {is_saved03}")
