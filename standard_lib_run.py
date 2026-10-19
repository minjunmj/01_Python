import random
from datetime import datetime, date

now = datetime.now()
today = date.today()

print(now.strftime("%Y-%m-%d %H:%M:%S"))

from pathlib import Path

path = Path("data/students.json")
print("파일 이름:", path.name)
print("확장자:", path.suffix)
print("상위 폴더:", path.parent)


file_path = Path("data") / "pcwk.txt"
file_path.parent.mkdir(parents=True, exist_ok=True)