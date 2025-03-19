# id-gen: A Simple ID Generator

`id-gen`은 다양한 옵션을 지원하는 간단한 식별자 생성 도구입니다. CLI 도구로 사용하거나 Python 패키지로 임포트하여 사용할 수 있습니다.

## 기능

- **기본 기능**: 소문자 알파벳으로 시작하고, 최소 1개의 숫자를 포함하는 ID 생성
- **추가 기능**:
  - 대문자 포함 (`-u` 옵션)
  - 특수문자 포함 (`-s` 옵션)
  - 왼손 단독 타이핑 최적화 (`-f` 옵션)
  - CVCV 패턴 (자음-모음-자음-모음)

## 설치

```bash
# 로컬 설치
cd id-gen
pip install -e .

# 또는 PyPI에서 설치 (배포 후)
pip install id-gen
```

## CLI 사용법

기본 사용법:

```bash
# 기본 5자리 ID 생성
id-gen

# 지정된 길이의 ID 생성
id-gen 13

# 여러 개의 ID 생성
id-gen 7 -n 5

# 대문자 포함
id-gen 5 -u

# 특수문자 포함
id-gen 5 -s

# 대문자와 특수문자 모두 포함
id-gen 5 -u -s

# 왼손 단독 타이핑 최적화
id-gen 5 -f

# CVCV 패턴 사용 (다른 옵션과 함께 사용 불가)
id-gen cvcv
```

### 옵션

- `length_or_pattern`: ID 길이 또는 'cvcv' 패턴 (기본값: 5)
- `-n, --count`: 생성할 ID 개수 (기본값: 1)
- `-u, --uppercase`: 대문자 포함
- `-s, --special`: 특수문자 포함
- `-f, --fast`: 왼손 단독 타이핑 최적화

## 패키지로 사용하기

`id-gen`을 Python 패키지로 임포트하여 사용할 수 있습니다:

```python
import id_gen

# 기본 ID 생성 (소문자 + 숫자)
basic_id = id_gen.generate_basic_id(8)
print(f"Basic ID: {basic_id}")

# 복잡한 ID 생성 (대문자 + 특수문자 포함)
complex_id = id_gen.generate_complex_id(10)
print(f"Complex ID: {complex_id}")

# 왼손 단독 타이핑용 ID 생성
fast_id = id_gen.generate_fast_typing_id(7)
print(f"Fast typing ID: {fast_id}")

# CVCV 패턴 ID 생성
cvcv_id = id_gen.generate_cvcv_id(8)
print(f"CVCV pattern ID: {cvcv_id}")

# 여러 개의 ID 생성
ids = id_gen.generate_multiple_ids(
    length=6,
    count=5,
    uppercase=True,
    special_chars=True
)
print("Multiple IDs:")
for id_str in ids:
    print(f"  - {id_str}")
```

## 고급 사용법

더 세밀한 제어가 필요한 경우, 저수준 API를 사용할 수 있습니다:

```python
from id_gen import create_id_generator, generate_ids

# 커스텀 ID 생성기 생성
generator = create_id_generator(
    include_uppercase=True,
    include_special=False,
    left_hand_only=False,
    cvcv_pattern=False
)

# 생성기를 사용하여 ID 생성
custom_id = generator(12)
print(f"Custom ID: {custom_id}")

# 여러 ID 생성
custom_ids = generate_ids(generator, length=9, count=3)
print("Custom IDs:")
for id_str in custom_ids:
    print(f"  - {id_str}")
```

## 프로젝트 구조

```sh
id-gen/
├── id_gen/
│   ├── __init__.py  # 주요 기능 및 API 정의
│   └── cli.py       # 명령행 인터페이스
├── setup.py         # 패키지 설치 설정
└── README.md        # 문서
```

## 기타

X를 제외한 인간 접근/수정 금지, 인간은 난독화 및 바이너리화 된 툴로써만 접근 허용
