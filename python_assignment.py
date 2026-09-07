"""AX 2회차 Ch 1: Python 기초 과제. Python 3, 외부 라이브러리 불필요."""

from pathlib import Path

SENTENCE = """
파이썬 공부는 재미있다
파이썬 공부는 어렵지만 재미있다
데이터 분석에도 파이썬을 사용한다
파이썬 공부를 계속하면 실력이 늘어난다
"""


def count_words(sentence):
    """공백으로 나눈 단어를 key, 등장 횟수를 value로 반환한다."""
    if not isinstance(sentence, str):
        raise TypeError("문장은 문자열이어야 합니다.")
    word_counts = {}
    for word in sentence.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def print_frequent_words(word_counts, minimum):
    """기준 횟수 이상인 단어만 출력한다."""
    if type(minimum) is not int or minimum < 1:
        raise ValueError("기준 횟수는 1 이상의 정수여야 합니다.")
    found = False
    for word, count in word_counts.items():
        if count >= minimum:
            print(f"{word} : {count}회")
            found = True
    if not found:
        print("조건에 맞는 단어가 없습니다.")


def main():
    print("[Part 1] 리스트와 반복문을 이용한 데이터 처리")
    # 문제에서 데이터와 기준을 지정하지 않아 점수와 80점 기준을 선택했다.
    scores = [65, 90, 78, 88, 100, 54, 80]
    selected_scores = []
    selected_count = 0
    total = 0
    for score in scores:
        total += score
        if score >= 80:
            selected_scores.append(score)
            selected_count += 1
    print("전체 점수:", scores)
    print("80점 이상:", selected_scores)
    print("80점 이상 개수:", selected_count)
    print("총점:", total)
    print(f"평균: {total / len(scores):.2f}")

    print("\n[Part 2] 딕셔너리로 단어 빈도 분석")
    # 먼저 직접 반복문으로 작성한 다음 Part 3에서 함수로 분리한다.
    word_counts = {}
    for word in SENTENCE.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    for word, count in word_counts.items():
        print(f"{word} : {count}회")
    print("2회 이상 등장한 단어:")
    for word, count in word_counts.items():
        if count >= 2:
            print(f"{word} : {count}회")

    print("\n[Part 3] 함수로 정리")
    result = count_words(SENTENCE)
    print("함수 반환값:", result)
    print("2회 이상 등장한 단어:")
    print_frequent_words(result, 2)

    print("\n[Part 4] 오류 확인 및 검증")
    # 아래 오류는 예외처리 동작을 확인하기 위해 의도적으로 발생시킨다.
    try:
        count_words(123)
    except TypeError as error:
        print("입력 자료형 오류 처리:", error)
    try:
        minimum = int("두 번")
        print_frequent_words(result, minimum)
    except ValueError:
        print("기준 입력 오류 처리: 숫자로 된 정수를 입력해주세요.")
    print("정상 입력으로 다시 실행:")
    print_frequent_words(result, 2)
    # 예시와 달리 split()은 '파이썬'과 '파이썬을'을 별개로 센다.
    assert result == word_counts
    assert result["파이썬"] == 3
    assert result["파이썬을"] == 1
    assert sum(result.values()) == 16
    assert count_words("") == {}
    print("검증 통과: 함수 결과 일치, 파이썬 3회, 파이썬을 1회, 전체 16단어, 빈 문자열 처리")

    print("\n[도전 문제] 최빈 단어, 최소 빈도 단어, 검색, 파일 저장")
    maximum = max(result.values())
    minimum = min(result.values())
    for word, count in result.items():
        if count == maximum:
            print(f"가장 많이 등장: {word} ({count}회)")
    least_words = []
    for word, count in result.items():
        if count == minimum:
            least_words.append(word)
    print(f"가장 적게 등장 ({minimum}회):", ", ".join(least_words))
    search_word = "공부는"
    print(f"검색: {search_word} → {result.get(search_word, 0)}회")
    output_path = Path(__file__).with_name("word_frequency.txt")
    with output_path.open("w", encoding="utf-8") as file:
        for word, count in result.items():
            file.write(f"{word} : {count}회\n")
    print("분석 결과 저장:", output_path.name)


if __name__ == "__main__":
    main()
