import pandas as pd
import re

# CSV 파일 읽기
df = pd.read_csv('csk_nation_city.csv')

# 정규 표현식 패턴 생성
pattern_dict = {} # 정규 표현식 패턴을 저장할 딕셔너리

for index, row in df.iterrows():
    expected = row['Expected']
    pattern_str = row['ExpectedReRef']

    # 패턴에 \b를 추가하여 단어 경계를 지정
    # dallas를 검색하니 dallas의 la를 보고 로스앤젤레스가 나와 추가

    pattern_str = r'\b' + pattern_str + r'\b' # 이 패턴은 `New York` 라는 도시 이름이 정확히 일치하는 경우만 매치 `New York City` 같은건 불일치
    # pattern_str = r'\b' + pattern_str.replace(' ', r'\s*') + r'\b' #요건 `New York City` 같은것도 일치

    
    pattern = re.compile(pattern_str, re.IGNORECASE)
    pattern_dict[expected] = pattern

user_input = None

while True:

    # 사용자 입력받기
    user_input = input("도시 이름을 입력하세요(종료:quit입력): ")

    # 사용자 입력이 'quit'인지 확인하고 종료
    if user_input.lower() == 'quit':
        break

    matched = False

    # 입력된 도시 이름을 띄어쓰기를 제거한 문자열로 변환하여 검색
    sanitized_input = user_input.replace(' ', '')
    for expected, pattern in pattern_dict.items():
        if pattern.search(sanitized_input):
            user_input = expected
            matched = True
            break

    # 입력된 도시 이름을 대응하는 패턴으로 변환
    for expected, pattern in pattern_dict.items():
        if pattern.search(user_input):
            user_input = expected
            matched = True
            break

    if not matched:
        print("일치하는 도시를 찾을 수 없습니다.")

    # 변환된 결과 출력
    print(user_input)
