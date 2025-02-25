import argparse
import random
import string

# 메시지 상수
PROG_DESC = "알파벳으로 시작하는 랜덤 식별자 생성기"
PROG_EPILOG = """
예시:
  %(prog)s          # 랜덤 길이({short}, {medium}, {long} 중 하나)로 식별자 생성
  %(prog)s -s       # {short}자리 식별자 생성
  %(prog)s -m       # {medium}자리 식별자 생성
  %(prog)s -l       # {long}자리 식별자 생성
  %(prog)s -s -n 3  # {short}자리 식별자 3개 생성
"""


# 길이 관련 상수
LENGTH_SHORT = 5
LENGTH_MEDIUM = 7
LENGTH_LONG = 11
AVAILABLE_LENGTHS = [LENGTH_SHORT, LENGTH_MEDIUM, LENGTH_LONG]

# 옵션 관련 상수
HELP_SHORT = f"{LENGTH_SHORT}자리 식별자 생성"
HELP_MEDIUM = f"{LENGTH_MEDIUM}자리 식별자 생성"
HELP_LONG = f"{LENGTH_LONG}자리 식별자 생성"
HELP_NUMBER = "생성할 식별자 개수 (기본값: 1)"


def generate_id(length: int) -> str:
    """
    랜덤 식별자를 생성합니다.

    규칙:
    1. 첫 글자는 소문자 알파벳
    2. 나머지는 소문자 알파벳과 숫자 조합
    3. 최소 1개의 숫자 포함

    Args:
        length (int): 생성할 식별자의 길이

    Returns:
        str: 생성된 식별자
    """
    # 첫 글자는 소문자 알파벳
    first_letter = random.choice(string.ascii_lowercase)

    # 최소 1개의 숫자 보장
    guaranteed_number = random.choice(string.digits)

    # 나머지 문자열 생성
    remaining_length = length - 2  # 첫 글자와 숫자 제외
    other_chars = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=remaining_length)
    )

    # 숫자를 2번째 위치 이후 중 랜덤한 위치에 삽입
    char_list = list(other_chars)
    insert_position = random.randint(0, remaining_length)
    char_list.insert(insert_position, guaranteed_number)

    return first_letter + "".join(char_list)


def generate_multiple_ids(length: int, count: int) -> list[str]:
    """
    지정된 개수만큼 랜덤 식별자를 생성합니다.

    Args:
        length (int): 각 식별자의 길이
        count (int): 생성할 식별자의 개수

    Returns:
        list[str]: 생성된 식별자 리스트
    """
    return [generate_id(length) for _ in range(count)]


def get_random_length() -> int:
    """
    사용 가능한 길이 중 하나를 랜덤으로 선택합니다.

    Returns:
        int: 선택된 길이
    """
    return random.choice(AVAILABLE_LENGTHS)


def setup_argument_parser() -> argparse.ArgumentParser:
    """
    명령행 인자 파서를 설정하고 반환합니다.

    Returns:
        argparse.ArgumentParser: 설정된 인자 파서
    """
    parser = argparse.ArgumentParser(
        description=PROG_DESC,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=PROG_EPILOG.format(
            short=LENGTH_SHORT, medium=LENGTH_MEDIUM, long=LENGTH_LONG
        ),
    )

    length_group = parser.add_mutually_exclusive_group(required=False)
    length_group.add_argument(
        "-s",
        "--short",
        action="store_const",
        const=LENGTH_SHORT,
        dest="length",
        help=HELP_SHORT,
    )
    length_group.add_argument(
        "-m",
        "--medium",
        action="store_const",
        const=LENGTH_MEDIUM,
        dest="length",
        help=HELP_MEDIUM,
    )
    length_group.add_argument(
        "-l",
        "--long",
        action="store_const",
        const=LENGTH_LONG,
        dest="length",
        help=HELP_LONG,
    )

    parser.add_argument("-n", "--number", type=int, default=1, help=HELP_NUMBER)

    return parser


def main():
    """
    메인 프로그램 실행 함수
    """
    parser = setup_argument_parser()
    args = parser.parse_args()

    # 길이가 지정되지 않은 경우 랜덤으로 선택
    if args.length is None:
        args.length = get_random_length()

    ids = generate_multiple_ids(args.length, args.number)
    for generated_id in ids:
        print(generated_id)


if __name__ == "__main__":
    main()
