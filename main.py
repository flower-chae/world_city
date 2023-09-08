import pandas as pd
import re

# CSV 파일 읽기
df = pd.read_csv('csk_city.csv')

# 정규 표현식 패턴 생성
pattern_dict = {} # 정규 표현식 패턴을 저장할 딕셔너리

for index, row in df.iterrows():
    expected = row['Expected']
    pattern_str = row['ExpectedReRef']
    pattern = re.compile(pattern_str, re.IGNORECASE)
    pattern_dict[expected] = pattern

user_input = None

while True:

    # 사용자 입력받기
    user_input = input("도시 이름을 입력하세요(종료:quit입력): ")

    # 사용자 입력이 'quit'인지 확인하고 종료
    if user_input.lower() == 'quit':
        break
    # 입력된 도시 이름을 대응하는 패턴으로 변환
    for expected, pattern in pattern_dict.items():
        if pattern.search(user_input):
            user_input = expected
            break

    # 변환된 결과 출력
    print(user_input)
